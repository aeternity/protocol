
#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 3,
    "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
    "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
    "deposit": "1",
    "vm_version": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
        "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
        "deposit": "1",
        "vm_version": 7
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
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 3,
    "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
    "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
    "deposit": 10,
    "vm_version": "1"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
        "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
        "deposit": 10,
        "vm_version": "1"
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
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": "1",
    "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
    "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
    "deposit": 10,
    "vm_version": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": "1",
        "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
        "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
        "deposit": 10,
        "vm_version": 7
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
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 3,
    "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
    "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
    "deposit": 10,
    "vm_version": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53SKBBk+UuMoIeYrKywob2KM+2w3BjAJ/dat7U9f1q+vLdSk1IIQs=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
          "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "vm_version": 7
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
  "id": -576460752303421803,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECRHUjRQmoz/npVkbxYuOImFt67sevp/+jYHqwbmNMNqLaSnCQGgxoI5MReaG1aLnxjLrueuqx/E7uSm1Eq3fAMuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0igQZPlLjKCHmKyssKG9ijPtsNwYwCf3Wre1PX9avry3Ur93HhJ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421803,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuECRHUjRQmoz/npVkbxYuOImFt67sevp/+jYHqwbmNMNqLaSnCQGgxoI5MReaG1aLnxjLrueuqx/E7uSm1Eq3fAMuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0igQZPlLjKCHmKyssKG9ijPtsNwYwCf3Wre1PX9avry3Ur93HhJ",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
          "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "vm_version": 7
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
  "id": -576460752303421802,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECRHUjRQmoz/npVkbxYuOImFt67sevp/+jYHqwbmNMNqLaSnCQGgxoI5MReaG1aLnxjLrueuqx/E7uSm1Eq3fAMuEDRtEDI3X1W9LTkVqlZjedJ8AXdkdrInj2vamPzfGCad2ltmRDmqNjHzbAcoqKmgBnCu06B9RWA917/ytokcbsLuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0igQZPlLjKCHmKyssKG9ijPtsNwYwCf3Wre1PX9avry3UqF19HW"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421802,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuECRHUjRQmoz/npVkbxYuOImFt67sevp/+jYHqwbmNMNqLaSnCQGgxoI5MReaG1aLnxjLrueuqx/E7uSm1Eq3fAMuEDRtEDI3X1W9LTkVqlZjedJ8AXdkdrInj2vamPzfGCad2ltmRDmqNjHzbAcoqKmgBnCu06B9RWA917/ytokcbsLuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0igQZPlLjKCHmKyssKG9ijPtsNwYwCf3Wre1PX9avry3UqF19HW"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuECRHUjRQmoz/npVkbxYuOImFt67sevp/+jYHqwbmNMNqLaSnCQGgxoI5MReaG1aLnxjLrueuqx/E7uSm1Eq3fAMuEDRtEDI3X1W9LTkVqlZjedJ8AXdkdrInj2vamPzfGCad2ltmRDmqNjHzbAcoqKmgBnCu06B9RWA917/ytokcbsLuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0igQZPlLjKCHmKyssKG9ijPtsNwYwCf3Wre1PX9avry3UqF19HW"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421801,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421801,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "owner_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwCs9rhl",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_LwCs9rhl"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421800,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421800,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "owner_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwCs9rhl",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_LwCs9rhl"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 73,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 331,
      "height": 73,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53SaDunQ1V6P6fCv9/IYWDNl5nvtEPUa5ok8CQ9TdPBQn7HQpmHIk=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421799,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBW4Wnyttf/QqQdewspI8jbykCs/MA/VeqcEjXRMey2Gxd4zG13IH+unLtPFGjQnn+OnVtVyC7fMyCHx1RzKR8JuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0mg7p0NVej+nwr/fyGFgzZeZ77RD1GuaJPAkPU3TwUJ+x3KRlmW"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421799,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBW4Wnyttf/QqQdewspI8jbykCs/MA/VeqcEjXRMey2Gxd4zG13IH+unLtPFGjQnn+OnVtVyC7fMyCHx1RzKR8JuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0mg7p0NVej+nwr/fyGFgzZeZ77RD1GuaJPAkPU3TwUJ+x3KRlmW",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421798,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBW4Wnyttf/QqQdewspI8jbykCs/MA/VeqcEjXRMey2Gxd4zG13IH+unLtPFGjQnn+OnVtVyC7fMyCHx1RzKR8JuECOLRrhp5ZBmSgcLS4kR9NHY9y7bkuu83GfAZ/qMNPiCNaOBF8Hh38+mWyycIWfiJdmnEheruxvHEvY3M34pF8GuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0mg7p0NVej+nwr/fyGFgzZeZ77RD1GuaJPAkPU3TwUJ+x00uIM1"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421798,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBW4Wnyttf/QqQdewspI8jbykCs/MA/VeqcEjXRMey2Gxd4zG13IH+unLtPFGjQnn+OnVtVyC7fMyCHx1RzKR8JuECOLRrhp5ZBmSgcLS4kR9NHY9y7bkuu83GfAZ/qMNPiCNaOBF8Hh38+mWyycIWfiJdmnEheruxvHEvY3M34pF8GuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0mg7p0NVej+nwr/fyGFgzZeZ77RD1GuaJPAkPU3TwUJ+x00uIM1"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBW4Wnyttf/QqQdewspI8jbykCs/MA/VeqcEjXRMey2Gxd4zG13IH+unLtPFGjQnn+OnVtVyC7fMyCHx1RzKR8JuECOLRrhp5ZBmSgcLS4kR9NHY9y7bkuu83GfAZ/qMNPiCNaOBF8Hh38+mWyycIWfiJdmnEheruxvHEvY3M34pF8GuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0mg7p0NVej+nwr/fyGFgzZeZ77RD1GuaJPAkPU3TwUJ+x00uIM1"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 73
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": 73
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 73
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 73
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 73
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 73,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 331,
      "height": 73,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 73
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": 73
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 73
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 73
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 73
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 73,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 331,
      "height": 73,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 74,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 556,
      "height": 74,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53SqBbixEYI2azBsDTt7lPSOTYUi2V+e3NCJn2W9/d+zt0OhB5U4A=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421797,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED+czR+50mOHh/CbY8R/sQS3UeTTSFLqTNrWcvpz4+By25sGI4+AKdMxx8BI/1Db9jC+SHnZxxpgG/9aR4/90gAuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0qgW4sRGCNmswbA07e5T0jk2FItlfntzQiZ9lvf3fs7dDppxCc+"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421797,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuED+czR+50mOHh/CbY8R/sQS3UeTTSFLqTNrWcvpz4+By25sGI4+AKdMxx8BI/1Db9jC+SHnZxxpgG/9aR4/90gAuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0qgW4sRGCNmswbA07e5T0jk2FItlfntzQiZ9lvf3fs7dDppxCc+",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421796,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEB/h+ku8CI8cxc+icmQEH8BZ0+s+rAlEeTDJQLkZjFO44ufPlTEuXxogjUNegimevAZgVQeJNeTrLTJFEQjzboCuED+czR+50mOHh/CbY8R/sQS3UeTTSFLqTNrWcvpz4+By25sGI4+AKdMxx8BI/1Db9jC+SHnZxxpgG/9aR4/90gAuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0qgW4sRGCNmswbA07e5T0jk2FItlfntzQiZ9lvf3fs7dDrjMN8m"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421796,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEB/h+ku8CI8cxc+icmQEH8BZ0+s+rAlEeTDJQLkZjFO44ufPlTEuXxogjUNegimevAZgVQeJNeTrLTJFEQjzboCuED+czR+50mOHh/CbY8R/sQS3UeTTSFLqTNrWcvpz4+By25sGI4+AKdMxx8BI/1Db9jC+SHnZxxpgG/9aR4/90gAuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0qgW4sRGCNmswbA07e5T0jk2FItlfntzQiZ9lvf3fs7dDrjMN8m"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEB/h+ku8CI8cxc+icmQEH8BZ0+s+rAlEeTDJQLkZjFO44ufPlTEuXxogjUNegimevAZgVQeJNeTrLTJFEQjzboCuED+czR+50mOHh/CbY8R/sQS3UeTTSFLqTNrWcvpz4+By25sGI4+AKdMxx8BI/1Db9jC+SHnZxxpgG/9aR4/90gAuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0qgW4sRGCNmswbA07e5T0jk2FItlfntzQiZ9lvf3fs7dDrjMN8m"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 74
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": 74
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 74
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 74
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 74
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 74,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 556,
      "height": 74,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 74
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": 74
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 74
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 74
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 74
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 74,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 556,
      "height": 74,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421795,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421795,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "owner_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwCs9rhl",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_LwIVSSB3aW6fAKB89BjMgOBNHvEAzlMeLv0uW/JoSso+N7CW9pYkrtabqyVubywgSSB3aW6fAKDfa5vKbvnIUY8yeaw2mF6ECMypgIbbXeGHfVElueryTdAcfSI="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421794,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421794,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "owner_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwCs9rhl",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_LwIVSSB3aW6fAKB89BjMgOBNHvEAzlMeLv0uW/JoSso+N7CW9pYkrtabqyVubywgSSB3aW6fAKDfa5vKbvnIUY8yeaw2mF6ECMypgIbbXeGHfVElueryTdAcfSI="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 75,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 821,
      "height": 75,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53S6CmBFVrLVsN0ag6tH6txJHSjF/cbVYZ/o/iWCbKXx23xeNkujc=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421793,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEASjthK2nuEfJSUumOUbT8mWbFsyAb4LlumLrwUIbxEUxvusrY86QdI0DvFvzBYYmjN94hrLtkvGx8GN10+94QPuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0ugpgRVay1bDdGoOrR+rcSR0oxf3G1WGf6P4lgmyl8dt8XLSV14"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421793,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEASjthK2nuEfJSUumOUbT8mWbFsyAb4LlumLrwUIbxEUxvusrY86QdI0DvFvzBYYmjN94hrLtkvGx8GN10+94QPuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0ugpgRVay1bDdGoOrR+rcSR0oxf3G1WGf6P4lgmyl8dt8XLSV14",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421792,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEASjthK2nuEfJSUumOUbT8mWbFsyAb4LlumLrwUIbxEUxvusrY86QdI0DvFvzBYYmjN94hrLtkvGx8GN10+94QPuECgP0lhc8y7q8BUFP6xMjYZOOjgNL5YGSWFQiSR1pMmJYtRyk/hTup3Yg0IqsLNJzugwNJt73R+/w/YENynOVkBuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0ugpgRVay1bDdGoOrR+rcSR0oxf3G1WGf6P4lgmyl8dt8XfYbO1"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421792,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEASjthK2nuEfJSUumOUbT8mWbFsyAb4LlumLrwUIbxEUxvusrY86QdI0DvFvzBYYmjN94hrLtkvGx8GN10+94QPuECgP0lhc8y7q8BUFP6xMjYZOOjgNL5YGSWFQiSR1pMmJYtRyk/hTup3Yg0IqsLNJzugwNJt73R+/w/YENynOVkBuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0ugpgRVay1bDdGoOrR+rcSR0oxf3G1WGf6P4lgmyl8dt8XfYbO1"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEASjthK2nuEfJSUumOUbT8mWbFsyAb4LlumLrwUIbxEUxvusrY86QdI0DvFvzBYYmjN94hrLtkvGx8GN10+94QPuECgP0lhc8y7q8BUFP6xMjYZOOjgNL5YGSWFQiSR1pMmJYtRyk/hTup3Yg0IqsLNJzugwNJt73R+/w/YENynOVkBuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0ugpgRVay1bDdGoOrR+rcSR0oxf3G1WGf6P4lgmyl8dt8XfYbO1"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 75
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": 75
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 75
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 75
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 75
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 75,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 821,
      "height": 75,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 75
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": 75
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 75
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 75
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 75
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 75,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 821,
      "height": 75,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 76,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 83,
      "height": 76,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_RWJldF9hbHJlYWR5X3Rha2VuiHO7fw=="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53TKAWd3EK+cw2w46IuXcbl5F3jkbAuWCBKrIeSgoB0F+t5XLgHds=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421791,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBm0982ieWh09myGdVGVK5xBXySPS1OnhbQFEm70nUIN684pdF4fDFAA1U4VGZh9TdL7fPruZgV29RO99vNkhEDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0ygFndxCvnMNsOOiLl3G5eRd45GwLlggSqyHkoKAdBfreXfxvPa"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421791,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBm0982ieWh09myGdVGVK5xBXySPS1OnhbQFEm70nUIN684pdF4fDFAA1U4VGZh9TdL7fPruZgV29RO99vNkhEDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0ygFndxCvnMNsOOiLl3G5eRd45GwLlggSqyHkoKAdBfreXfxvPa",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421790,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEATjI4c96fMAiz8v1+tu22vQrl1hogEtRMvJfbcPSkQfZMU7e7WIPFlWKXiwVkMCDRynv3WpjJZWHbLrZ3eAQEBuEBm0982ieWh09myGdVGVK5xBXySPS1OnhbQFEm70nUIN684pdF4fDFAA1U4VGZh9TdL7fPruZgV29RO99vNkhEDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0ygFndxCvnMNsOOiLl3G5eRd45GwLlggSqyHkoKAdBfreVLkmKC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421790,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEATjI4c96fMAiz8v1+tu22vQrl1hogEtRMvJfbcPSkQfZMU7e7WIPFlWKXiwVkMCDRynv3WpjJZWHbLrZ3eAQEBuEBm0982ieWh09myGdVGVK5xBXySPS1OnhbQFEm70nUIN684pdF4fDFAA1U4VGZh9TdL7fPruZgV29RO99vNkhEDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0ygFndxCvnMNsOOiLl3G5eRd45GwLlggSqyHkoKAdBfreVLkmKC"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEATjI4c96fMAiz8v1+tu22vQrl1hogEtRMvJfbcPSkQfZMU7e7WIPFlWKXiwVkMCDRynv3WpjJZWHbLrZ3eAQEBuEBm0982ieWh09myGdVGVK5xBXySPS1OnhbQFEm70nUIN684pdF4fDFAA1U4VGZh9TdL7fPruZgV29RO99vNkhEDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0ygFndxCvnMNsOOiLl3G5eRd45GwLlggSqyHkoKAdBfreVLkmKC"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 76
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": 76
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 76
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 76
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 76
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 76,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 83,
      "height": 76,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_RWJldF9hbHJlYWR5X3Rha2VuiHO7fw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 76
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": 76
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 76
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 76
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 76
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 76,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 83,
      "height": 76,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_RWJldF9hbHJlYWR5X3Rha2VuiHO7fw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 77,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 83,
      "height": 77,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_RWJldF9hbHJlYWR5X3Rha2VuiHO7fw=="
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2D1tYCDG7iatxxKsFTt8t3PzLsKb92Pu2o7WYP58UaZPwvDz1e",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53TaBwD3ohyxBWPJP5nLo3pBDOxlVCPTbi4qS1bKVoWckPAwJx6XY=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421789,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDknkMx1PwkDh7aUK6w1vD2AE2/C9QmazoERtvFsw7lYS2oCRtG4ioUlJ6b6Im2S9dAfy0vpYxrdlV6OK+pSpkLuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud02gcA96IcsQVjyT+Zy6N6QQzsZVQj024uKktWylaFnJDwM0glRZ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421789,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDknkMx1PwkDh7aUK6w1vD2AE2/C9QmazoERtvFsw7lYS2oCRtG4ioUlJ6b6Im2S9dAfy0vpYxrdlV6OK+pSpkLuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud02gcA96IcsQVjyT+Zy6N6QQzsZVQj024uKktWylaFnJDwM0glRZ",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421788,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBFq/ST1yFBHRa0hrVmF1kyFAc/oOEvW5xQDuK3YxkFYLzEWXd/jQtugDVnH7XufuGNPRdoMq7Rny8DhePtBmgLuEDknkMx1PwkDh7aUK6w1vD2AE2/C9QmazoERtvFsw7lYS2oCRtG4ioUlJ6b6Im2S9dAfy0vpYxrdlV6OK+pSpkLuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud02gcA96IcsQVjyT+Zy6N6QQzsZVQj024uKktWylaFnJDwNcg1O9"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421788,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBFq/ST1yFBHRa0hrVmF1kyFAc/oOEvW5xQDuK3YxkFYLzEWXd/jQtugDVnH7XufuGNPRdoMq7Rny8DhePtBmgLuEDknkMx1PwkDh7aUK6w1vD2AE2/C9QmazoERtvFsw7lYS2oCRtG4ioUlJ6b6Im2S9dAfy0vpYxrdlV6OK+pSpkLuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud02gcA96IcsQVjyT+Zy6N6QQzsZVQj024uKktWylaFnJDwNcg1O9"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBFq/ST1yFBHRa0hrVmF1kyFAc/oOEvW5xQDuK3YxkFYLzEWXd/jQtugDVnH7XufuGNPRdoMq7Rny8DhePtBmgLuEDknkMx1PwkDh7aUK6w1vD2AE2/C9QmazoERtvFsw7lYS2oCRtG4ioUlJ6b6Im2S9dAfy0vpYxrdlV6OK+pSpkLuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud02gcA96IcsQVjyT+Zy6N6QQzsZVQj024uKktWylaFnJDwNcg1O9"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 77
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": 77
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 77
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 77
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 77
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 77,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 83,
      "height": 77,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_RWJldF9hbHJlYWR5X3Rha2VuiHO7fw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 77
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": 77
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 77
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 77
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 77
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 77,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 83,
      "height": 77,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_RWJldF9hbHJlYWR5X3Rha2VuiHO7fw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
        "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
        "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 78,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 263,
      "height": 78,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_SWRpZmZlcmVudCBxdWVzdGlvbpFHdWg="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
        "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
        "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
        "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
        "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53TqBbIu0CbrgYFABzMIHgkCBQPeSmuSxUDg1ksz0l1bxKTvTL3qk=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421787,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECb7Fd9R9R3ukTBlxPC5LAoAsa3SU4lTL4yTM7VGvk0QmrWO6ePuocKGYRjbiHzgMCBWFNqYviD+Sy2yXZdv6EKuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud06gWyLtAm64GBQAczCB4JAgUD3kprksVA4NZLM9JdW8Sk5BzS5c"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421787,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuECb7Fd9R9R3ukTBlxPC5LAoAsa3SU4lTL4yTM7VGvk0QmrWO6ePuocKGYRjbiHzgMCBWFNqYviD+Sy2yXZdv6EKuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud06gWyLtAm64GBQAczCB4JAgUD3kprksVA4NZLM9JdW8Sk5BzS5c",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421786,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECb7Fd9R9R3ukTBlxPC5LAoAsa3SU4lTL4yTM7VGvk0QmrWO6ePuocKGYRjbiHzgMCBWFNqYviD+Sy2yXZdv6EKuEDCn3zCsmUjG7zF4Z7Np0lfDkXpmudj9zXRj4PPL6rbc2+qQbF9XSue3rf8y2/UCHS1QnDjipN09U4UizUijC8KuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud06gWyLtAm64GBQAczCB4JAgUD3kprksVA4NZLM9JdW8Sk5AmU3o"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421786,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuECb7Fd9R9R3ukTBlxPC5LAoAsa3SU4lTL4yTM7VGvk0QmrWO6ePuocKGYRjbiHzgMCBWFNqYviD+Sy2yXZdv6EKuEDCn3zCsmUjG7zF4Z7Np0lfDkXpmudj9zXRj4PPL6rbc2+qQbF9XSue3rf8y2/UCHS1QnDjipN09U4UizUijC8KuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud06gWyLtAm64GBQAczCB4JAgUD3kprksVA4NZLM9JdW8Sk5AmU3o"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuECb7Fd9R9R3ukTBlxPC5LAoAsa3SU4lTL4yTM7VGvk0QmrWO6ePuocKGYRjbiHzgMCBWFNqYviD+Sy2yXZdv6EKuEDCn3zCsmUjG7zF4Z7Np0lfDkXpmudj9zXRj4PPL6rbc2+qQbF9XSue3rf8y2/UCHS1QnDjipN09U4UizUijC8KuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud06gWyLtAm64GBQAczCB4JAgUD3kprksVA4NZLM9JdW8Sk5AmU3o"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 78
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": 78
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 78
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 78
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 78
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 78,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 263,
      "height": 78,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_SWRpZmZlcmVudCBxdWVzdGlvbpFHdWg="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 78
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": 78
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 78
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 78
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 78
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 78,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 263,
      "height": 78,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_SWRpZmZlcmVudCBxdWVzdGlvbpFHdWg="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
        "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
        "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 79,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 263,
      "height": 79,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_SWRpZmZlcmVudCBxdWVzdGlvbpFHdWg="
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
        "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
        "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
        "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
        "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2gkccv6L2DtjK39TqJsquADniANTPqv6HHsbSsuBL3eAu5szJk",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53T6AfyPEbM/U0zeCXXVNLPbz4laNZjsE20nlyU9T7xhbrjaYVlV8=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421785,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAn8rv8Ft+LXXMmmtZuooQEl6kCS+q+dZpBL2nxD6dCaMyytrBflPor9BSLKFGazDlA6KfmZ2Ea6v+7Bbhoht0HuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0+gH8jxGzP1NM3gl11TSz28+JWjWY7BNtJ5clPU+8YW641pqwVG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421785,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAn8rv8Ft+LXXMmmtZuooQEl6kCS+q+dZpBL2nxD6dCaMyytrBflPor9BSLKFGazDlA6KfmZ2Ea6v+7Bbhoht0HuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0+gH8jxGzP1NM3gl11TSz28+JWjWY7BNtJ5clPU+8YW641pqwVG",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421784,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAIFwyMJH9h2YTSXn7KlMoOpuIHw1i4r1wi4280vnKIXVJIMd2gubRdwb+ByHSuuEaxkT2STQ3Kt5BIk3t0BSYHuEAn8rv8Ft+LXXMmmtZuooQEl6kCS+q+dZpBL2nxD6dCaMyytrBflPor9BSLKFGazDlA6KfmZ2Ea6v+7Bbhoht0HuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0+gH8jxGzP1NM3gl11TSz28+JWjWY7BNtJ5clPU+8YW643RNJt+"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421784,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEAIFwyMJH9h2YTSXn7KlMoOpuIHw1i4r1wi4280vnKIXVJIMd2gubRdwb+ByHSuuEaxkT2STQ3Kt5BIk3t0BSYHuEAn8rv8Ft+LXXMmmtZuooQEl6kCS+q+dZpBL2nxD6dCaMyytrBflPor9BSLKFGazDlA6KfmZ2Ea6v+7Bbhoht0HuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0+gH8jxGzP1NM3gl11TSz28+JWjWY7BNtJ5clPU+8YW643RNJt+"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEAIFwyMJH9h2YTSXn7KlMoOpuIHw1i4r1wi4280vnKIXVJIMd2gubRdwb+ByHSuuEaxkT2STQ3Kt5BIk3t0BSYHuEAn8rv8Ft+LXXMmmtZuooQEl6kCS+q+dZpBL2nxD6dCaMyytrBflPor9BSLKFGazDlA6KfmZ2Ea6v+7Bbhoht0HuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud0+gH8jxGzP1NM3gl11TSz28+JWjWY7BNtJ5clPU+8YW643RNJt+"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 79
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": 79
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 79
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 79
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 79
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 79,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 263,
      "height": 79,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_SWRpZmZlcmVudCBxdWVzdGlvbpFHdWg="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 79
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": 79
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 79
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 79
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 79
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 79,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 263,
      "height": 79,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_SWRpZmZlcmVudCBxdWVzdGlvbpFHdWg="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421783,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421783,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "owner_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421782,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421782,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "owner_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421781,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421781,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "balance": 69999999999969
    },
    {
      "account": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "balance": 39999999999981
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
        "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
        "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 80,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 325,
      "height": 80,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_OW5vIHdpbm5pbmcgYmV0r9Yizg=="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
        "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
        "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
        "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
        "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53UKChpMoYZi+rtUkyTMEzCj0r8xgQHmB2L/z7I0pRF5hlb8pJZVA=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421780,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDgHitkuF8RqNdloQi3BQRWz3t6tjwAXfj2HuVf0AwlboxbJhnH9j+aq/t2lJlBaiFOIOhvMu+DNQfVnviDg0YIuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1CgoaTKGGYvq7VJMkzBMwo9K/MYEB5gdi/8+yNKUReYZW8xEp7P"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421780,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDgHitkuF8RqNdloQi3BQRWz3t6tjwAXfj2HuVf0AwlboxbJhnH9j+aq/t2lJlBaiFOIOhvMu+DNQfVnviDg0YIuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1CgoaTKGGYvq7VJMkzBMwo9K/MYEB5gdi/8+yNKUReYZW8xEp7P",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421779,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECN6elyspyIBezoYowHB8cOryooX8cqFfsn0d8QQCu0HN4zZ3Msg+cqJZs8jzuQLqfTNysrzwZgK85flNhvcAACuEDgHitkuF8RqNdloQi3BQRWz3t6tjwAXfj2HuVf0AwlboxbJhnH9j+aq/t2lJlBaiFOIOhvMu+DNQfVnviDg0YIuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1CgoaTKGGYvq7VJMkzBMwo9K/MYEB5gdi/8+yNKUReYZW9q77aG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421779,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuECN6elyspyIBezoYowHB8cOryooX8cqFfsn0d8QQCu0HN4zZ3Msg+cqJZs8jzuQLqfTNysrzwZgK85flNhvcAACuEDgHitkuF8RqNdloQi3BQRWz3t6tjwAXfj2HuVf0AwlboxbJhnH9j+aq/t2lJlBaiFOIOhvMu+DNQfVnviDg0YIuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1CgoaTKGGYvq7VJMkzBMwo9K/MYEB5gdi/8+yNKUReYZW9q77aG"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuECN6elyspyIBezoYowHB8cOryooX8cqFfsn0d8QQCu0HN4zZ3Msg+cqJZs8jzuQLqfTNysrzwZgK85flNhvcAACuEDgHitkuF8RqNdloQi3BQRWz3t6tjwAXfj2HuVf0AwlboxbJhnH9j+aq/t2lJlBaiFOIOhvMu+DNQfVnviDg0YIuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1CgoaTKGGYvq7VJMkzBMwo9K/MYEB5gdi/8+yNKUReYZW9q77aG"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 80
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": 80
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 80
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 80
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 80
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 80,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 325,
      "height": 80,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_OW5vIHdpbm5pbmcgYmV0r9Yizg=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 80
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": 80
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 80
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 80
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 80
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 80,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 325,
      "height": 80,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_OW5vIHdpbm5pbmcgYmV0r9Yizg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421778,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421778,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "owner_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421777,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421777,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "owner_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421776,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421776,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "balance": 69999999999969
    },
    {
      "account": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "balance": 39999999999981
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 81,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 446,
      "height": 81,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53UaCcxEmjPvVFiZQSWaC+FpOxusrHKJ5Hr3s92ZVYEhZXb2jOPfc=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421775,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDPszXs14M04j+lKWYUO61IN+IuO19Z2//yXYSAb3V8mRud12f7zWx8igzzKFoERRXvaDS00RQVDte4veX8+2sEuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1GgnMRJoz71RYmUElmgvhaTsbrKxyieR697PdmVWBIWV2+4Cw95"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421775,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDPszXs14M04j+lKWYUO61IN+IuO19Z2//yXYSAb3V8mRud12f7zWx8igzzKFoERRXvaDS00RQVDte4veX8+2sEuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1GgnMRJoz71RYmUElmgvhaTsbrKxyieR697PdmVWBIWV2+4Cw95",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421774,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDPszXs14M04j+lKWYUO61IN+IuO19Z2//yXYSAb3V8mRud12f7zWx8igzzKFoERRXvaDS00RQVDte4veX8+2sEuED6JPFuYsyt+s2Q/cZtjT9UThlcKryJP/I591ym5WvuAHNDal74ctyZHlz8XLh/GXyAljYJoQO6/NuXVgYkXEwPuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1GgnMRJoz71RYmUElmgvhaTsbrKxyieR697PdmVWBIWV2/1A6bH"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421774,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEDPszXs14M04j+lKWYUO61IN+IuO19Z2//yXYSAb3V8mRud12f7zWx8igzzKFoERRXvaDS00RQVDte4veX8+2sEuED6JPFuYsyt+s2Q/cZtjT9UThlcKryJP/I591ym5WvuAHNDal74ctyZHlz8XLh/GXyAljYJoQO6/NuXVgYkXEwPuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1GgnMRJoz71RYmUElmgvhaTsbrKxyieR697PdmVWBIWV2/1A6bH"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEDPszXs14M04j+lKWYUO61IN+IuO19Z2//yXYSAb3V8mRud12f7zWx8igzzKFoERRXvaDS00RQVDte4veX8+2sEuED6JPFuYsyt+s2Q/cZtjT9UThlcKryJP/I591ym5WvuAHNDal74ctyZHlz8XLh/GXyAljYJoQO6/NuXVgYkXEwPuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1GgnMRJoz71RYmUElmgvhaTsbrKxyieR697PdmVWBIWV2/1A6bH"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 81
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": 81
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 81
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 81
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 81
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 81,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 446,
      "height": 81,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 81
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": 81
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 81
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 81
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 81
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 81,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 446,
      "height": 81,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421773,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421773,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "owner_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421772,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421772,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "owner_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421771,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421771,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "balance": 69999999999969
    },
    {
      "account": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "balance": 39999999999981
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421770,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421770,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "balance": 10
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
        "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
        "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 82,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 466,
      "height": 82,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
        "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
        "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
        "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
        "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_dME2o3DU9KWHVLe4jMkTtkWQSnrjNvmwTbwPBJBzAejFup95p",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53UqBVlwdcATjeggerSsf1Naq0Dr3hAlhU8phg4So+03yPKyWfxZ0=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421769,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB3E6QjY4rJi+CgIslbkHWOGC2we8EIghgzVYnDKft/qwz7tve4VIIrH/x1K7C0CYDBLGnnGBrSMCJOMyvwiHsLuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1KgVZcHXAE43oIHq0rH9TWqtA694QJYVPKYYOEqPtN8jysX9mSS"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421769,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB3E6QjY4rJi+CgIslbkHWOGC2we8EIghgzVYnDKft/qwz7tve4VIIrH/x1K7C0CYDBLGnnGBrSMCJOMyvwiHsLuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1KgVZcHXAE43oIHq0rH9TWqtA694QJYVPKYYOEqPtN8jysX9mSS",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421768,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEB3E6QjY4rJi+CgIslbkHWOGC2we8EIghgzVYnDKft/qwz7tve4VIIrH/x1K7C0CYDBLGnnGBrSMCJOMyvwiHsLuECIzkA1y2VQF5lSdTUr1d7Dn094gBaZUuyp1atRtHxszWnVRjxXbFPnHMBUAqHlL9gVskAiiHEQe5u1uyWm3EILuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1KgVZcHXAE43oIHq0rH9TWqtA694QJYVPKYYOEqPtN8jytwKM7i"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421768,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEB3E6QjY4rJi+CgIslbkHWOGC2we8EIghgzVYnDKft/qwz7tve4VIIrH/x1K7C0CYDBLGnnGBrSMCJOMyvwiHsLuECIzkA1y2VQF5lSdTUr1d7Dn094gBaZUuyp1atRtHxszWnVRjxXbFPnHMBUAqHlL9gVskAiiHEQe5u1uyWm3EILuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1KgVZcHXAE43oIHq0rH9TWqtA694QJYVPKYYOEqPtN8jytwKM7i"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEB3E6QjY4rJi+CgIslbkHWOGC2we8EIghgzVYnDKft/qwz7tve4VIIrH/x1K7C0CYDBLGnnGBrSMCJOMyvwiHsLuECIzkA1y2VQF5lSdTUr1d7Dn094gBaZUuyp1atRtHxszWnVRjxXbFPnHMBUAqHlL9gVskAiiHEQe5u1uyWm3EILuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1KgVZcHXAE43oIHq0rH9TWqtA694QJYVPKYYOEqPtN8jytwKM7i"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 82
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": 82
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 82
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 82
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 82
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 82,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 466,
      "height": 82,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 82
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
        "round": 82
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 82
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 82
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
    "round": 82
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 82,
      "contract_id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "gas_price": 1,
      "gas_used": 466,
      "height": 82,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421767,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421767,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "owner_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421766,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421766,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "owner_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421765,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421765,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "balance": 0
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421764,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421764,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_4haEgfNxEmpG8F5cXA8q4fgECEHLif6KG92Rvz3afsBGXmHVs",
      "balance": 0
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421763,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421763,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "balance": 69999999999979
    },
    {
      "account": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "balance": 39999999999981
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421762,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421762,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "balance": 69999999999979
    },
    {
      "account": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "balance": 39999999999981
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 3,
    "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
    "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
    "deposit": "1",
    "vm_version": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
        "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
        "deposit": "1",
        "vm_version": 7
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
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 3,
    "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
    "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
    "deposit": 10,
    "vm_version": "1"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
        "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
        "deposit": 10,
        "vm_version": "1"
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
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": "1",
    "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
    "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
    "deposit": 10,
    "vm_version": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": "1",
        "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
        "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
        "deposit": 10,
        "vm_version": 7
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
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 3,
    "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
    "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
    "deposit": 10,
    "vm_version": 7
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53U6CszMx53YbnBZ/zvDfCckRCd2NeAIaUL+TTUzFHaITGtFY7N4s=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
          "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "vm_version": 7
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
  "id": -576460752303421761,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB8sGy17TRTUHlujvxB1QiF01N8c3uwZLqskBo0IoVQRvgxXOcF0D2TDMFf1E/BlYFYF3IJC0ofEDF9l2ani3gHuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1OgrMzMed2G5wWf87w3wnJEQndjXgCGlC/k01MxR2iExrR7uts8"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421761,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB8sGy17TRTUHlujvxB1QiF01N8c3uwZLqskBo0IoVQRvgxXOcF0D2TDMFf1E/BlYFYF3IJC0ofEDF9l2ani3gHuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1OgrMzMed2G5wWf87w3wnJEQndjXgCGlC/k01MxR2iExrR7uts8",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
          "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "vm_version": 7
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
  "id": -576460752303421760,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEB8sGy17TRTUHlujvxB1QiF01N8c3uwZLqskBo0IoVQRvgxXOcF0D2TDMFf1E/BlYFYF3IJC0ofEDF9l2ani3gHuED2Ao8/8gR9yBUbJgK6wXmFPCg7TsDGXsXcMyvfdBeyZQz1sYCY+EwEJBnVCXSOY4PNxO6NOiUCQ3njKpxCjcAPuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1OgrMzMed2G5wWf87w3wnJEQndjXgCGlC/k01MxR2iExrRoTf5w"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421760,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEB8sGy17TRTUHlujvxB1QiF01N8c3uwZLqskBo0IoVQRvgxXOcF0D2TDMFf1E/BlYFYF3IJC0ofEDF9l2ani3gHuED2Ao8/8gR9yBUbJgK6wXmFPCg7TsDGXsXcMyvfdBeyZQz1sYCY+EwEJBnVCXSOY4PNxO6NOiUCQ3njKpxCjcAPuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1OgrMzMed2G5wWf87w3wnJEQndjXgCGlC/k01MxR2iExrRoTf5w"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEB8sGy17TRTUHlujvxB1QiF01N8c3uwZLqskBo0IoVQRvgxXOcF0D2TDMFf1E/BlYFYF3IJC0ofEDF9l2ani3gHuED2Ao8/8gR9yBUbJgK6wXmFPCg7TsDGXsXcMyvfdBeyZQz1sYCY+EwEJBnVCXSOY4PNxO6NOiUCQ3njKpxCjcAPuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1OgrMzMed2G5wWf87w3wnJEQndjXgCGlC/k01MxR2iExrRoTf5w"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421759,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421759,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "owner_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwCs9rhl",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_LwCs9rhl"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421758,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421758,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "owner_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwCs9rhl",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_LwCs9rhl"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "ABCDEFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 84,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 331,
      "height": 84,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "ABCDEFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "ABCDEFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "ABCDEFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53VKB7QM0m388fd/iYXqmDKkhSsOyzgBLlgvy982FRb6zLSC3+aIE=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421757,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA2VK27KJhg+jCZUdnCUN2TXSYnInMzQWt9+jq1NGL77Ql+Lzj2EY8MUsYPcP/TM4azgmCbiUmSFC2KnN4VETkDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1Sge0DNJt/PH3f4mF6pgypIUrDss4AS5YL8vfNhUW+sy0gMi1hR"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421757,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA2VK27KJhg+jCZUdnCUN2TXSYnInMzQWt9+jq1NGL77Ql+Lzj2EY8MUsYPcP/TM4azgmCbiUmSFC2KnN4VETkDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1Sge0DNJt/PH3f4mF6pgypIUrDss4AS5YL8vfNhUW+sy0gMi1hR",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421756,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAq8Zl3mt2AbsIus6HdU4666etFmuFYOmCTog0XIIKIWRFm9kwBRuodIe0IYqGDHC1adSV25a3BaoSZ6a4TBLwOuEA2VK27KJhg+jCZUdnCUN2TXSYnInMzQWt9+jq1NGL77Ql+Lzj2EY8MUsYPcP/TM4azgmCbiUmSFC2KnN4VETkDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1Sge0DNJt/PH3f4mF6pgypIUrDss4AS5YL8vfNhUW+sy0hd0zby"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421756,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEAq8Zl3mt2AbsIus6HdU4666etFmuFYOmCTog0XIIKIWRFm9kwBRuodIe0IYqGDHC1adSV25a3BaoSZ6a4TBLwOuEA2VK27KJhg+jCZUdnCUN2TXSYnInMzQWt9+jq1NGL77Ql+Lzj2EY8MUsYPcP/TM4azgmCbiUmSFC2KnN4VETkDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1Sge0DNJt/PH3f4mF6pgypIUrDss4AS5YL8vfNhUW+sy0hd0zby"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEAq8Zl3mt2AbsIus6HdU4666etFmuFYOmCTog0XIIKIWRFm9kwBRuodIe0IYqGDHC1adSV25a3BaoSZ6a4TBLwOuEA2VK27KJhg+jCZUdnCUN2TXSYnInMzQWt9+jq1NGL77Ql+Lzj2EY8MUsYPcP/TM4azgmCbiUmSFC2KnN4VETkDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1Sge0DNJt/PH3f4mF6pgypIUrDss4AS5YL8vfNhUW+sy0hd0zby"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 84
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": 84
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 84
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 84
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 84
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 84,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 331,
      "height": 84,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 84
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": 84
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 84
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 84
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 84
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 84,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 331,
      "height": 84,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "ABCDEFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 85,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 556,
      "height": 85,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "ABCDEFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "ABCDEFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "ABCDEFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53VaBBVY2H/YUBaf/HUJqwAoGze123kAbZ9Iu5GKBsmFN5l/8gs10=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421755,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAeuL6WWzvkyyRYXxxQJ1TA4Jc7Yno+200HXGQdpwWxdXLtXltu8mcfG7Q2du/j5A2A/VvcdXQvLRGUEQvKEbEFuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1WgQVWNh/2FAWn/x1CasAKBs3tdt5AG2fSLuRigbJhTeZe234hf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421755,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAeuL6WWzvkyyRYXxxQJ1TA4Jc7Yno+200HXGQdpwWxdXLtXltu8mcfG7Q2du/j5A2A/VvcdXQvLRGUEQvKEbEFuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1WgQVWNh/2FAWn/x1CasAKBs3tdt5AG2fSLuRigbJhTeZe234hf",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421754,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAeuL6WWzvkyyRYXxxQJ1TA4Jc7Yno+200HXGQdpwWxdXLtXltu8mcfG7Q2du/j5A2A/VvcdXQvLRGUEQvKEbEFuEChhYOKHHypbUjqEuhUUeskYX1copB/rD2Jlt0HWH8jMB+wXEFkvzKGrXRsKDknqUyHMQ0zNqdtdwiGTz+DfnUPuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1WgQVWNh/2FAWn/x1CasAKBs3tdt5AG2fSLuRigbJhTeZd/SycI"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421754,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEAeuL6WWzvkyyRYXxxQJ1TA4Jc7Yno+200HXGQdpwWxdXLtXltu8mcfG7Q2du/j5A2A/VvcdXQvLRGUEQvKEbEFuEChhYOKHHypbUjqEuhUUeskYX1copB/rD2Jlt0HWH8jMB+wXEFkvzKGrXRsKDknqUyHMQ0zNqdtdwiGTz+DfnUPuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1WgQVWNh/2FAWn/x1CasAKBs3tdt5AG2fSLuRigbJhTeZd/SycI"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEAeuL6WWzvkyyRYXxxQJ1TA4Jc7Yno+200HXGQdpwWxdXLtXltu8mcfG7Q2du/j5A2A/VvcdXQvLRGUEQvKEbEFuEChhYOKHHypbUjqEuhUUeskYX1copB/rD2Jlt0HWH8jMB+wXEFkvzKGrXRsKDknqUyHMQ0zNqdtdwiGTz+DfnUPuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1WgQVWNh/2FAWn/x1CasAKBs3tdt5AG2fSLuRigbJhTeZd/SycI"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 85
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": 85
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 85
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 85
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 85
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 85,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 556,
      "height": 85,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 85
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": 85
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 85
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 85
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 85
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 85,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 556,
      "height": 85,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421753,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421753,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "owner_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwCs9rhl",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_LwIVSSB3aW6fAKB89BjMgOBNHvEAzlMeLv0uW/JoSso+N7CW9pYkrtabqyVubywgSSB3aW6fAKDfa5vKbvnIUY8yeaw2mF6ECMypgIbbXeGHfVElueryTdAcfSI="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421752,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421752,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "owner_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwCs9rhl",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_LwIVSSB3aW6fAKB89BjMgOBNHvEAzlMeLv0uW/JoSso+N7CW9pYkrtabqyVubywgSSB3aW6fAKDfa5vKbvnIUY8yeaw2mF6ECMypgIbbXeGHfVElueryTdAcfSI="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "ABCDEFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 86,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 821,
      "height": 86,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "ABCDEFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "ABCDEFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "ABCDEFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53VqAH8xA7vfGfv4bXLi+prdMDkA4De7nmE8t3XTvBHv4s6iMvBks=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421751,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBhz31J8JJmBw0kbjhcAIO8Squ0zB231Y5aJ6AZrIxCWsC7e0x7SkuQCoR8EO9mK/yF43BWYIhcwP/CexXBVZ0GuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1agB/MQO73xn7+G1y4vqa3TA5AOA3u55hPLd107wR7+LOpuboZF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421751,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBhz31J8JJmBw0kbjhcAIO8Squ0zB231Y5aJ6AZrIxCWsC7e0x7SkuQCoR8EO9mK/yF43BWYIhcwP/CexXBVZ0GuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1agB/MQO73xn7+G1y4vqa3TA5AOA3u55hPLd107wR7+LOpuboZF",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421750,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBhz31J8JJmBw0kbjhcAIO8Squ0zB231Y5aJ6AZrIxCWsC7e0x7SkuQCoR8EO9mK/yF43BWYIhcwP/CexXBVZ0GuED97LcXzIeOB6dkyaqNdxANAQPCw4yrj2PtQ1ugRXZLaYAlnHwsWqiztXUUd6jb8zgukCcroBm7N5s6Tk3Rz7wCuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1agB/MQO73xn7+G1y4vqa3TA5AOA3u55hPLd107wR7+LOrOa+mr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421750,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBhz31J8JJmBw0kbjhcAIO8Squ0zB231Y5aJ6AZrIxCWsC7e0x7SkuQCoR8EO9mK/yF43BWYIhcwP/CexXBVZ0GuED97LcXzIeOB6dkyaqNdxANAQPCw4yrj2PtQ1ugRXZLaYAlnHwsWqiztXUUd6jb8zgukCcroBm7N5s6Tk3Rz7wCuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1agB/MQO73xn7+G1y4vqa3TA5AOA3u55hPLd107wR7+LOrOa+mr"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBhz31J8JJmBw0kbjhcAIO8Squ0zB231Y5aJ6AZrIxCWsC7e0x7SkuQCoR8EO9mK/yF43BWYIhcwP/CexXBVZ0GuED97LcXzIeOB6dkyaqNdxANAQPCw4yrj2PtQ1ugRXZLaYAlnHwsWqiztXUUd6jb8zgukCcroBm7N5s6Tk3Rz7wCuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1agB/MQO73xn7+G1y4vqa3TA5AOA3u55hPLd107wR7+LOrOa+mr"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 86
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": 86
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 86
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 86
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 86
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 86,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 821,
      "height": 86,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 86
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": 86
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 86
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 86
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 86
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 86,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 821,
      "height": 86,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "ABCDEFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 87,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 83,
      "height": 87,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_RWJldF9hbHJlYWR5X3Rha2VuiHO7fw=="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "ABCDEFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "ABCDEFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "ABCDEFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53V6Ag5U1+jFtAo0antMaUMhraBmrA7a/QCPikxYEbqCvOC15ikPg=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421749,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBGdZuzA5HzYZe4+VtdXv9ib8HwdWBADEWM503nZGZ+ukIKOXci4v+2xbrdQlrIJCl1xYACRWbfjfyuuO+ES7UOuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1egIOVNfoxbQKNGp7TGlDIa2gZqwO2v0Aj4pMWBG6grzgtV/Odo"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421749,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBGdZuzA5HzYZe4+VtdXv9ib8HwdWBADEWM503nZGZ+ukIKOXci4v+2xbrdQlrIJCl1xYACRWbfjfyuuO+ES7UOuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1egIOVNfoxbQKNGp7TGlDIa2gZqwO2v0Aj4pMWBG6grzgtV/Odo",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421748,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBGdZuzA5HzYZe4+VtdXv9ib8HwdWBADEWM503nZGZ+ukIKOXci4v+2xbrdQlrIJCl1xYACRWbfjfyuuO+ES7UOuEB0LBYBMYARIUaiVd659UkjMUbWXNu2QwhTy+wh60o3Hxp2khBCGE16YbEZZGXeJj4wU82lNDGyKs5ry8sV5/8DuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1egIOVNfoxbQKNGp7TGlDIa2gZqwO2v0Aj4pMWBG6grzgtQZRxk"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421748,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBGdZuzA5HzYZe4+VtdXv9ib8HwdWBADEWM503nZGZ+ukIKOXci4v+2xbrdQlrIJCl1xYACRWbfjfyuuO+ES7UOuEB0LBYBMYARIUaiVd659UkjMUbWXNu2QwhTy+wh60o3Hxp2khBCGE16YbEZZGXeJj4wU82lNDGyKs5ry8sV5/8DuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1egIOVNfoxbQKNGp7TGlDIa2gZqwO2v0Aj4pMWBG6grzgtQZRxk"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBGdZuzA5HzYZe4+VtdXv9ib8HwdWBADEWM503nZGZ+ukIKOXci4v+2xbrdQlrIJCl1xYACRWbfjfyuuO+ES7UOuEB0LBYBMYARIUaiVd659UkjMUbWXNu2QwhTy+wh60o3Hxp2khBCGE16YbEZZGXeJj4wU82lNDGyKs5ry8sV5/8DuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1egIOVNfoxbQKNGp7TGlDIa2gZqwO2v0Aj4pMWBG6grzgtQZRxk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 87
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": 87
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 87
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 87
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 87
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 87,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 83,
      "height": 87,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_RWJldF9hbHJlYWR5X3Rha2VuiHO7fw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 87
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": 87
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 87
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 87
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 87
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 87,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 83,
      "height": 87,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_RWJldF9hbHJlYWR5X3Rha2VuiHO7fw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "ABCDEFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 88,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 83,
      "height": 88,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_RWJldF9hbHJlYWR5X3Rha2VuiHO7fw=="
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "ABCDEFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "ABCDEFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "ABCDEFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_bvyBQ7yj3xB4rkKYmLUDxYj3p8zHo1SkeVrUgx9GP9MrFd1UG",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53WKCQR++pEV+07FD3KorVnSZP6JlqNxLElNPw+DPmDeSQLI0Acuk=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421747,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDGIm962rDHRwCjOyxHQIov32WoSsaSoJ6L/XPYzpuDCWlQq0yT+TTvKfDMmyUJ0g776jwEdb8JWAkqLTmocM4DuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1igkEfvqRFftOxQ9yqK1Z0mT+iZajcSxJTT8Pgz5g3kkCxZVMPh"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421747,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDGIm962rDHRwCjOyxHQIov32WoSsaSoJ6L/XPYzpuDCWlQq0yT+TTvKfDMmyUJ0g776jwEdb8JWAkqLTmocM4DuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1igkEfvqRFftOxQ9yqK1Z0mT+iZajcSxJTT8Pgz5g3kkCxZVMPh",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421746,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECmO5cxA1H9zXVYLj1cIxysE0Fy16IuWEU1rHP/6Dlzys526kmhKawaqAFObijg8E9Np0vHeEnTGgAMBrFAKWoBuEDGIm962rDHRwCjOyxHQIov32WoSsaSoJ6L/XPYzpuDCWlQq0yT+TTvKfDMmyUJ0g776jwEdb8JWAkqLTmocM4DuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1igkEfvqRFftOxQ9yqK1Z0mT+iZajcSxJTT8Pgz5g3kkCz3F/Uz"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421746,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuECmO5cxA1H9zXVYLj1cIxysE0Fy16IuWEU1rHP/6Dlzys526kmhKawaqAFObijg8E9Np0vHeEnTGgAMBrFAKWoBuEDGIm962rDHRwCjOyxHQIov32WoSsaSoJ6L/XPYzpuDCWlQq0yT+TTvKfDMmyUJ0g776jwEdb8JWAkqLTmocM4DuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1igkEfvqRFftOxQ9yqK1Z0mT+iZajcSxJTT8Pgz5g3kkCz3F/Uz"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuECmO5cxA1H9zXVYLj1cIxysE0Fy16IuWEU1rHP/6Dlzys526kmhKawaqAFObijg8E9Np0vHeEnTGgAMBrFAKWoBuEDGIm962rDHRwCjOyxHQIov32WoSsaSoJ6L/XPYzpuDCWlQq0yT+TTvKfDMmyUJ0g776jwEdb8JWAkqLTmocM4DuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1igkEfvqRFftOxQ9yqK1Z0mT+iZajcSxJTT8Pgz5g3kkCz3F/Uz"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 88
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": 88
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 88
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 88
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 88
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 88,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 83,
      "height": 88,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_RWJldF9hbHJlYWR5X3Rha2VuiHO7fw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 88
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": 88
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 88
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 88
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 88
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 88,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 83,
      "height": 88,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_RWJldF9hbHJlYWR5X3Rha2VuiHO7fw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
        "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
        "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
    "call_data": "ABCDEFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 89,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 263,
      "height": 89,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_SWRpZmZlcmVudCBxdWVzdGlvbpFHdWg="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
        "call_data": "ABCDEFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
        "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
        "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
        "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
    "call_data": "ABCDEFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
        "call_data": "ABCDEFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
        "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53WaDufoOz2mE5lbTV7h3MQ//f+7Znkch1oHJ5PND1RjymrAUNK0E=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421745,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAUl6t4QkHgUmCTxkrZJmgumMWC9EIx4kffVHxyKEYjNc8L8IXcGwZFIe89Q9QrtuOLqqbYbLMW7FCkMQDVzU0AuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1mg7n6Ds9phOZW01e4dzEP/3/u2Z5HIdaByeTzQ9UY8pqwIvv2F"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421745,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAUl6t4QkHgUmCTxkrZJmgumMWC9EIx4kffVHxyKEYjNc8L8IXcGwZFIe89Q9QrtuOLqqbYbLMW7FCkMQDVzU0AuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1mg7n6Ds9phOZW01e4dzEP/3/u2Z5HIdaByeTzQ9UY8pqwIvv2F",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421744,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAUl6t4QkHgUmCTxkrZJmgumMWC9EIx4kffVHxyKEYjNc8L8IXcGwZFIe89Q9QrtuOLqqbYbLMW7FCkMQDVzU0AuEDUS9o2fE+Nxrkrp0drSZhE442olrt0IiJ9sUnluG9Q1VhAWoiIvWuWXJb7+XMvLLm36towwbkIaPxfjyrF500EuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1mg7n6Ds9phOZW01e4dzEP/3/u2Z5HIdaByeTzQ9UY8pqzerLVN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421744,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEAUl6t4QkHgUmCTxkrZJmgumMWC9EIx4kffVHxyKEYjNc8L8IXcGwZFIe89Q9QrtuOLqqbYbLMW7FCkMQDVzU0AuEDUS9o2fE+Nxrkrp0drSZhE442olrt0IiJ9sUnluG9Q1VhAWoiIvWuWXJb7+XMvLLm36towwbkIaPxfjyrF500EuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1mg7n6Ds9phOZW01e4dzEP/3/u2Z5HIdaByeTzQ9UY8pqzerLVN"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEAUl6t4QkHgUmCTxkrZJmgumMWC9EIx4kffVHxyKEYjNc8L8IXcGwZFIe89Q9QrtuOLqqbYbLMW7FCkMQDVzU0AuEDUS9o2fE+Nxrkrp0drSZhE442olrt0IiJ9sUnluG9Q1VhAWoiIvWuWXJb7+XMvLLm36towwbkIaPxfjyrF500EuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1mg7n6Ds9phOZW01e4dzEP/3/u2Z5HIdaByeTzQ9UY8pqzerLVN"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 89
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": 89
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 89
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 89
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 89
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 89,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 263,
      "height": 89,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_SWRpZmZlcmVudCBxdWVzdGlvbpFHdWg="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 89
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": 89
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 89
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 89
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 89
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 89,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 263,
      "height": 89,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_SWRpZmZlcmVudCBxdWVzdGlvbpFHdWg="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
        "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
        "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
    "call_data": "ABCDEFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 90,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 263,
      "height": 90,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_SWRpZmZlcmVudCBxdWVzdGlvbpFHdWg="
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
        "call_data": "ABCDEFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
        "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
        "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
        "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
    "call_data": "ABCDEFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
        "call_data": "ABCDEFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
        "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2LwS6j9ZXRuAb9vkRB47MaXz75LfF7zRA9TkVg1uM4mQGuHfNi",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53WqAoNgmTOxErPYzDusm3csu+bHRd3IMyZBGwISvomc/cHp3Lafo=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421743,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECQRfHDPkB7JwxB0R3C9O6Pg4eD+VTAk7+F47kp1B/eU4i9EDufEnaSlFCVAPRKBN7Bk8axHNJEluUJD3NzupgDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1qgKDYJkzsRKz2Mw7rJt3LLvmx0XdyDMmQRsCEr6JnP3B7v14PT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421743,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuECQRfHDPkB7JwxB0R3C9O6Pg4eD+VTAk7+F47kp1B/eU4i9EDufEnaSlFCVAPRKBN7Bk8axHNJEluUJD3NzupgDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1qgKDYJkzsRKz2Mw7rJt3LLvmx0XdyDMmQRsCEr6JnP3B7v14PT",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421742,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBu4wZOJ74CjSQj+XPKL0mfqszOhwU2fUKdPaW4gos5pe3JUhHbeLvAPp+WP5Ojy0ET+AwJh0F6//n3vHVgFM8LuECQRfHDPkB7JwxB0R3C9O6Pg4eD+VTAk7+F47kp1B/eU4i9EDufEnaSlFCVAPRKBN7Bk8axHNJEluUJD3NzupgDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1qgKDYJkzsRKz2Mw7rJt3LLvmx0XdyDMmQRsCEr6JnP3B5AS2ON"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421742,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBu4wZOJ74CjSQj+XPKL0mfqszOhwU2fUKdPaW4gos5pe3JUhHbeLvAPp+WP5Ojy0ET+AwJh0F6//n3vHVgFM8LuECQRfHDPkB7JwxB0R3C9O6Pg4eD+VTAk7+F47kp1B/eU4i9EDufEnaSlFCVAPRKBN7Bk8axHNJEluUJD3NzupgDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1qgKDYJkzsRKz2Mw7rJt3LLvmx0XdyDMmQRsCEr6JnP3B5AS2ON"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBu4wZOJ74CjSQj+XPKL0mfqszOhwU2fUKdPaW4gos5pe3JUhHbeLvAPp+WP5Ojy0ET+AwJh0F6//n3vHVgFM8LuECQRfHDPkB7JwxB0R3C9O6Pg4eD+VTAk7+F47kp1B/eU4i9EDufEnaSlFCVAPRKBN7Bk8axHNJEluUJD3NzupgDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1qgKDYJkzsRKz2Mw7rJt3LLvmx0XdyDMmQRsCEr6JnP3B5AS2ON"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 90
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": 90
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 90
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 90
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 90
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 90,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 263,
      "height": 90,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_SWRpZmZlcmVudCBxdWVzdGlvbpFHdWg="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 90
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": 90
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 90
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 90
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 90
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 90,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 263,
      "height": 90,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_SWRpZmZlcmVudCBxdWVzdGlvbpFHdWg="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421741,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421741,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "owner_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421740,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421740,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "owner_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421739,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421739,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "balance": 39999999999971
    },
    {
      "account": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "balance": 69999999999979
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
        "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
        "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "ABCDEFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 91,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 325,
      "height": 91,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_OW5vIHdpbm5pbmcgYmV0r9Yizg=="
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
        "call_data": "ABCDEFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
        "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
        "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
        "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "ABCDEFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
        "call_data": "ABCDEFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
        "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53W6A7DvAaTqA9FY51eX2wP4gEmNwL/+qyBvsTNDFyVTosGQJQdwQ=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421738,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBwYBN4sm5KC3OWq7NbVJvuGxjnnhd+caA2f9VE23N/Scj8k3Oq+KsfGkcXvzN6TlwScgrSx93IxpNsfjrPGeUBuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1ugOw7wGk6gPRWOdXl9sD+IBJjcC//qsgb7EzQxclU6LBnvbicY"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421738,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBwYBN4sm5KC3OWq7NbVJvuGxjnnhd+caA2f9VE23N/Scj8k3Oq+KsfGkcXvzN6TlwScgrSx93IxpNsfjrPGeUBuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1ugOw7wGk6gPRWOdXl9sD+IBJjcC//qsgb7EzQxclU6LBnvbicY",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421737,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBEw5EO+KcwIshPRkF28PKExbfmpU/1DyejGayOcv8AgWpgHcmsh0PQJ3U82jpCkId0CoJZL9JwyqarYVdRjUsEuEBwYBN4sm5KC3OWq7NbVJvuGxjnnhd+caA2f9VE23N/Scj8k3Oq+KsfGkcXvzN6TlwScgrSx93IxpNsfjrPGeUBuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1ugOw7wGk6gPRWOdXl9sD+IBJjcC//qsgb7EzQxclU6LBm1ySzB"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421737,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBEw5EO+KcwIshPRkF28PKExbfmpU/1DyejGayOcv8AgWpgHcmsh0PQJ3U82jpCkId0CoJZL9JwyqarYVdRjUsEuEBwYBN4sm5KC3OWq7NbVJvuGxjnnhd+caA2f9VE23N/Scj8k3Oq+KsfGkcXvzN6TlwScgrSx93IxpNsfjrPGeUBuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1ugOw7wGk6gPRWOdXl9sD+IBJjcC//qsgb7EzQxclU6LBm1ySzB"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBEw5EO+KcwIshPRkF28PKExbfmpU/1DyejGayOcv8AgWpgHcmsh0PQJ3U82jpCkId0CoJZL9JwyqarYVdRjUsEuEBwYBN4sm5KC3OWq7NbVJvuGxjnnhd+caA2f9VE23N/Scj8k3Oq+KsfGkcXvzN6TlwScgrSx93IxpNsfjrPGeUBuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1ugOw7wGk6gPRWOdXl9sD+IBJjcC//qsgb7EzQxclU6LBm1ySzB"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 91
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": 91
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 91
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 91
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 91
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 91,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 325,
      "height": 91,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_OW5vIHdpbm5pbmcgYmV0r9Yizg=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 91
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": 91
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 91
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 91
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 91
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 91,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 325,
      "height": 91,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_OW5vIHdpbm5pbmcgYmV0r9Yizg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421736,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421736,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "owner_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421735,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421735,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "owner_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421734,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421734,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "balance": 39999999999971
    },
    {
      "account": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "balance": 69999999999979
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "ABCDEFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 92,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 446,
      "height": 92,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
        "call_data": "ABCDEFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "ABCDEFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
        "call_data": "ABCDEFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53XKDBWP3h/4XGegNtZwo4gwnSoG5tvrUi0Ubgvqh9t3eq6W9xqjs=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421733,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED6yL14BQ8bKR6zYcT4Hujg88YHrmJfrHuzn4qYnUTpnotxhd/U3nXXe2ddWAiE2D2o3c5M+9AfzJqgvppv5EsKuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1ygwVj94f+FxnoDbWcKOIMJ0qBubb61ItFG4L6ofbd3qunv9vU3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421733,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuED6yL14BQ8bKR6zYcT4Hujg88YHrmJfrHuzn4qYnUTpnotxhd/U3nXXe2ddWAiE2D2o3c5M+9AfzJqgvppv5EsKuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1ygwVj94f+FxnoDbWcKOIMJ0qBubb61ItFG4L6ofbd3qunv9vU3",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421732,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBXzzpgDJmdsLKBkFDi6zDlNtpvPG78Ic5DXNdT6Q9D+HBH03i+C/6gjLfdQq5zO9LmzgFB2M6ePFyqZn63/CEFuED6yL14BQ8bKR6zYcT4Hujg88YHrmJfrHuzn4qYnUTpnotxhd/U3nXXe2ddWAiE2D2o3c5M+9AfzJqgvppv5EsKuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1ygwVj94f+FxnoDbWcKOIMJ0qBubb61ItFG4L6ofbd3qumqDeZU"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421732,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBXzzpgDJmdsLKBkFDi6zDlNtpvPG78Ic5DXNdT6Q9D+HBH03i+C/6gjLfdQq5zO9LmzgFB2M6ePFyqZn63/CEFuED6yL14BQ8bKR6zYcT4Hujg88YHrmJfrHuzn4qYnUTpnotxhd/U3nXXe2ddWAiE2D2o3c5M+9AfzJqgvppv5EsKuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1ygwVj94f+FxnoDbWcKOIMJ0qBubb61ItFG4L6ofbd3qumqDeZU"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBXzzpgDJmdsLKBkFDi6zDlNtpvPG78Ic5DXNdT6Q9D+HBH03i+C/6gjLfdQq5zO9LmzgFB2M6ePFyqZn63/CEFuED6yL14BQ8bKR6zYcT4Hujg88YHrmJfrHuzn4qYnUTpnotxhd/U3nXXe2ddWAiE2D2o3c5M+9AfzJqgvppv5EsKuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1ygwVj94f+FxnoDbWcKOIMJ0qBubb61ItFG4L6ofbd3qumqDeZU"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 92
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": 92
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 92
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 92
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 92
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 92,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 446,
      "height": 92,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 92
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": 92
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 92
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 92
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 92
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 92,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 446,
      "height": 92,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421731,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421731,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "owner_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421730,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421730,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "owner_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421729,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421729,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "balance": 39999999999971
    },
    {
      "account": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "balance": 69999999999979
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421728,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421728,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "balance": 10
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
        "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
        "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "ABCDEFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 93,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 466,
      "height": 93,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
        "call_data": "ABCDEFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
        "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
        "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
        "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "ABCDEFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
        "call_data": "ABCDEFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
        "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2RV24NY27ovLKyoTfTQoASFfKagRhWkYx49iHR4sTsij9GBZzu",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53XaCOqHo18hSuAu+mcZV7ZCm4RnoePh/7jOyRlU9KOu0aXTcqakM=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421727,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBH+Pml2IaJg/A92RoknMdzRBB3gLApnbxgBpPM9hHc62D7WpbAX6hQkgDOnkxj7Adta+ge1FbZE8vedJxIiekBuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud12gjqh6NfIUrgLvpnGVe2QpuEZ6Hj4f+4zskZVPSjrtGl14ymIp"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421727,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBH+Pml2IaJg/A92RoknMdzRBB3gLApnbxgBpPM9hHc62D7WpbAX6hQkgDOnkxj7Adta+ge1FbZE8vedJxIiekBuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud12gjqh6NfIUrgLvpnGVe2QpuEZ6Hj4f+4zskZVPSjrtGl14ymIp",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421726,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBH+Pml2IaJg/A92RoknMdzRBB3gLApnbxgBpPM9hHc62D7WpbAX6hQkgDOnkxj7Adta+ge1FbZE8vedJxIiekBuEDWDjObkphfjyXTQwkghU0inGYqcqYbZ/2q+P0jwTEz2LvGEjV1kkEYUQ++fgUDrqGgZyi5H6KV9AQUb+Z9eTYIuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud12gjqh6NfIUrgLvpnGVe2QpuEZ6Hj4f+4zskZVPSjrtGl2mGQSf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421726,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBH+Pml2IaJg/A92RoknMdzRBB3gLApnbxgBpPM9hHc62D7WpbAX6hQkgDOnkxj7Adta+ge1FbZE8vedJxIiekBuEDWDjObkphfjyXTQwkghU0inGYqcqYbZ/2q+P0jwTEz2LvGEjV1kkEYUQ++fgUDrqGgZyi5H6KV9AQUb+Z9eTYIuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud12gjqh6NfIUrgLvpnGVe2QpuEZ6Hj4f+4zskZVPSjrtGl2mGQSf"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBH+Pml2IaJg/A92RoknMdzRBB3gLApnbxgBpPM9hHc62D7WpbAX6hQkgDOnkxj7Adta+ge1FbZE8vedJxIiekBuEDWDjObkphfjyXTQwkghU0inGYqcqYbZ/2q+P0jwTEz2LvGEjV1kkEYUQ++fgUDrqGgZyi5H6KV9AQUb+Z9eTYIuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud12gjqh6NfIUrgLvpnGVe2QpuEZ6Hj4f+4zskZVPSjrtGl2mGQSf"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 93
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": 93
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 93
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 93
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 93
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 93,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 466,
      "height": 93,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 93
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
        "round": 93
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 93
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 93
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
    "round": 93
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 93,
      "contract_id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "gas_price": 1,
      "gas_used": 466,
      "height": 93,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421725,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421725,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "owner_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421724,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421724,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "owner_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421723,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421723,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "balance": 0
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421722,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421722,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_qxx2UwGYhgT52xQUMwdfxdWSouvZUeGYKKiHbTk5Xvq7dXyNu",
      "balance": 0
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421721,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421721,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "balance": 39999999999981
    },
    {
      "account": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "balance": 69999999999979
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421720,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421720,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "balance": 39999999999981
    },
    {
      "account": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "balance": 69999999999979
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 3,
    "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
    "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
    "deposit": "1",
    "vm_version": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
        "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
        "deposit": "1",
        "vm_version": 7
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
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 3,
    "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
    "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
    "deposit": 10,
    "vm_version": "1"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
        "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
        "deposit": 10,
        "vm_version": "1"
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
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": "1",
    "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
    "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
    "deposit": 10,
    "vm_version": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": "1",
        "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
        "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
        "deposit": 10,
        "vm_version": 7
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
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 3,
    "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
    "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
    "deposit": 10,
    "vm_version": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53XqAKucKbjZNTnj/wKz0tKOIDlUBP+kRi+4/Kv4fjnG67WUS7608=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
          "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "vm_version": 7
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
  "id": -576460752303421719,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED3fBm/A02rEI1xd2aC0qpqdtGMdmeqfhJDce5LIIe5SxA11fBl/KRUh1kH4OkQIhpPbC4mjdA7+f8NkjUFlxAKuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud16gCrnCm42TU54/8Cs9LSjiA5VAT/pEYvuPyr+H45xuu1me5oBC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421719,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuED3fBm/A02rEI1xd2aC0qpqdtGMdmeqfhJDce5LIIe5SxA11fBl/KRUh1kH4OkQIhpPbC4mjdA7+f8NkjUFlxAKuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud16gCrnCm42TU54/8Cs9LSjiA5VAT/pEYvuPyr+H45xuu1me5oBC",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
          "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "vm_version": 7
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
  "id": -576460752303421718,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECezIBraIv78zpRDXMXtSvzHOU9EvGymlhLt2siwCNzD2hAPcnhEbZoCjt12gj2U2Btq8Bk1Fa0y2MbIj+6NTAHuED3fBm/A02rEI1xd2aC0qpqdtGMdmeqfhJDce5LIIe5SxA11fBl/KRUh1kH4OkQIhpPbC4mjdA7+f8NkjUFlxAKuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud16gCrnCm42TU54/8Cs9LSjiA5VAT/pEYvuPyr+H45xuu1lwGYAl"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421718,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuECezIBraIv78zpRDXMXtSvzHOU9EvGymlhLt2siwCNzD2hAPcnhEbZoCjt12gj2U2Btq8Bk1Fa0y2MbIj+6NTAHuED3fBm/A02rEI1xd2aC0qpqdtGMdmeqfhJDce5LIIe5SxA11fBl/KRUh1kH4OkQIhpPbC4mjdA7+f8NkjUFlxAKuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud16gCrnCm42TU54/8Cs9LSjiA5VAT/pEYvuPyr+H45xuu1lwGYAl"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuECezIBraIv78zpRDXMXtSvzHOU9EvGymlhLt2siwCNzD2hAPcnhEbZoCjt12gj2U2Btq8Bk1Fa0y2MbIj+6NTAHuED3fBm/A02rEI1xd2aC0qpqdtGMdmeqfhJDce5LIIe5SxA11fBl/KRUh1kH4OkQIhpPbC4mjdA7+f8NkjUFlxAKuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud16gCrnCm42TU54/8Cs9LSjiA5VAT/pEYvuPyr+H45xuu1lwGYAl"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421717,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421717,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "owner_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwCs9rhl",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_LwCs9rhl"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421716,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421716,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "owner_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwCs9rhl",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_LwCs9rhl"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "ABCDEFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 95,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 331,
      "height": 95,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "ABCDEFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "ABCDEFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "ABCDEFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53X6BMtHlbXFQEaQWTsw6WgMiyqAYekdeV3OkzEcJqlcz6lUUDjSg=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421715,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECYv0w+tpEVVs8vOiqTLGVl0Q5ILsfQ7a0deos6hzsT6mLA8sC2XVVWm4SmUsniOphYBQyWeM5seZULHvRMuwUKuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1+gTLR5W1xUBGkFk7MOloDIsqgGHpHXldzpMxHCapXM+pUGqvfm"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421715,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuECYv0w+tpEVVs8vOiqTLGVl0Q5ILsfQ7a0deos6hzsT6mLA8sC2XVVWm4SmUsniOphYBQyWeM5seZULHvRMuwUKuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1+gTLR5W1xUBGkFk7MOloDIsqgGHpHXldzpMxHCapXM+pUGqvfm",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421714,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAE4kU+9mR5CHA2ncK5MgSYS8hBHfI9JSR+zNImykBsmdhb83Rl2QMhh5aof259DCX4zIPK052fhOf2pJYDnBsNuECYv0w+tpEVVs8vOiqTLGVl0Q5ILsfQ7a0deos6hzsT6mLA8sC2XVVWm4SmUsniOphYBQyWeM5seZULHvRMuwUKuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1+gTLR5W1xUBGkFk7MOloDIsqgGHpHXldzpMxHCapXM+pUShd7n"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421714,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEAE4kU+9mR5CHA2ncK5MgSYS8hBHfI9JSR+zNImykBsmdhb83Rl2QMhh5aof259DCX4zIPK052fhOf2pJYDnBsNuECYv0w+tpEVVs8vOiqTLGVl0Q5ILsfQ7a0deos6hzsT6mLA8sC2XVVWm4SmUsniOphYBQyWeM5seZULHvRMuwUKuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1+gTLR5W1xUBGkFk7MOloDIsqgGHpHXldzpMxHCapXM+pUShd7n"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEAE4kU+9mR5CHA2ncK5MgSYS8hBHfI9JSR+zNImykBsmdhb83Rl2QMhh5aof259DCX4zIPK052fhOf2pJYDnBsNuECYv0w+tpEVVs8vOiqTLGVl0Q5ILsfQ7a0deos6hzsT6mLA8sC2XVVWm4SmUsniOphYBQyWeM5seZULHvRMuwUKuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud1+gTLR5W1xUBGkFk7MOloDIsqgGHpHXldzpMxHCapXM+pUShd7n"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 95
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": 95
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 95
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 95
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 95
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 95,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 331,
      "height": 95,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 95
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": 95
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 95
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 95
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 95
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 95,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 331,
      "height": 95,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "ABCDEFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 96,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 556,
      "height": 96,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "ABCDEFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "ABCDEFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "ABCDEFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53YKCzb6dZca6WE4qaRUqXTHfkI8r5oqR48PPhhNarqU+apYKXgik=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421713,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECbBjT/VT0OwW7MD4R5THGxgJcYx2/mrd5kehLbQxxL9CgNy438ULIDXgawKLGFy2c8MZLv+zJT4eqAVeC9wJYMuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2Cgs2+nWXGulhOKmkVKl0x35CPK+aKkePDz4YTWq6lPmqXwXDY0"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421713,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuECbBjT/VT0OwW7MD4R5THGxgJcYx2/mrd5kehLbQxxL9CgNy438ULIDXgawKLGFy2c8MZLv+zJT4eqAVeC9wJYMuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2Cgs2+nWXGulhOKmkVKl0x35CPK+aKkePDz4YTWq6lPmqXwXDY0",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421712,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBehNOnHKeEdCPPnTgzxND6KPyZYDCCakLQW4EZd9SNMi6FHtUpYgkjNtOJM3R/E48lxESvZKqOVqnt2U85MYoKuECbBjT/VT0OwW7MD4R5THGxgJcYx2/mrd5kehLbQxxL9CgNy438ULIDXgawKLGFy2c8MZLv+zJT4eqAVeC9wJYMuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2Cgs2+nWXGulhOKmkVKl0x35CPK+aKkePDz4YTWq6lPmqXnupHK"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421712,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBehNOnHKeEdCPPnTgzxND6KPyZYDCCakLQW4EZd9SNMi6FHtUpYgkjNtOJM3R/E48lxESvZKqOVqnt2U85MYoKuECbBjT/VT0OwW7MD4R5THGxgJcYx2/mrd5kehLbQxxL9CgNy438ULIDXgawKLGFy2c8MZLv+zJT4eqAVeC9wJYMuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2Cgs2+nWXGulhOKmkVKl0x35CPK+aKkePDz4YTWq6lPmqXnupHK"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBehNOnHKeEdCPPnTgzxND6KPyZYDCCakLQW4EZd9SNMi6FHtUpYgkjNtOJM3R/E48lxESvZKqOVqnt2U85MYoKuECbBjT/VT0OwW7MD4R5THGxgJcYx2/mrd5kehLbQxxL9CgNy438ULIDXgawKLGFy2c8MZLv+zJT4eqAVeC9wJYMuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2Cgs2+nWXGulhOKmkVKl0x35CPK+aKkePDz4YTWq6lPmqXnupHK"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 96
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": 96
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 96
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 96
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 96
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 96,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 556,
      "height": 96,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 96
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": 96
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 96
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 96
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 96
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 96,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 556,
      "height": 96,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421711,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421711,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "owner_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwCs9rhl",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_LwIVSSB3aW6fAKB89BjMgOBNHvEAzlMeLv0uW/JoSso+N7CW9pYkrtabqyVubywgSSB3aW6fAKDfa5vKbvnIUY8yeaw2mF6ECMypgIbbXeGHfVElueryTdAcfSI="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421710,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421710,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "owner_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwCs9rhl",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_LwIVSSB3aW6fAKB89BjMgOBNHvEAzlMeLv0uW/JoSso+N7CW9pYkrtabqyVubywgSSB3aW6fAKDfa5vKbvnIUY8yeaw2mF6ECMypgIbbXeGHfVElueryTdAcfSI="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "ABCDEFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 97,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 821,
      "height": 97,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "ABCDEFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "ABCDEFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "ABCDEFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53YaACzcNUZMjQ+yI5JHGN9xT48OxG42lxY1xl0XSVagUP8OBbb+0=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421709,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBx8hhQiZ3Fz+jSFG1kk15xH7/4qpORcrXrdu5roY9o5uyBo5wK9Vua2IFRp7NhH6++p77M1m2osvnlyLDuxasPuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2GgAs3DVGTI0PsiOSRxjfcU+PDsRuNpcWNcZdF0lWoFD/DMhzyv"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421709,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBx8hhQiZ3Fz+jSFG1kk15xH7/4qpORcrXrdu5roY9o5uyBo5wK9Vua2IFRp7NhH6++p77M1m2osvnlyLDuxasPuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2GgAs3DVGTI0PsiOSRxjfcU+PDsRuNpcWNcZdF0lWoFD/DMhzyv",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421708,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAMEL3wD4jWdwqIIO3aaw1U8csbofO2/a8r2zh9ctu88CwPFDf8iifgdu+ym6BgnUTD52zQBI+0N9KGeCQjqcwEuEBx8hhQiZ3Fz+jSFG1kk15xH7/4qpORcrXrdu5roY9o5uyBo5wK9Vua2IFRp7NhH6++p77M1m2osvnlyLDuxasPuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2GgAs3DVGTI0PsiOSRxjfcU+PDsRuNpcWNcZdF0lWoFD/AmNmR9"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421708,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEAMEL3wD4jWdwqIIO3aaw1U8csbofO2/a8r2zh9ctu88CwPFDf8iifgdu+ym6BgnUTD52zQBI+0N9KGeCQjqcwEuEBx8hhQiZ3Fz+jSFG1kk15xH7/4qpORcrXrdu5roY9o5uyBo5wK9Vua2IFRp7NhH6++p77M1m2osvnlyLDuxasPuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2GgAs3DVGTI0PsiOSRxjfcU+PDsRuNpcWNcZdF0lWoFD/AmNmR9"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEAMEL3wD4jWdwqIIO3aaw1U8csbofO2/a8r2zh9ctu88CwPFDf8iifgdu+ym6BgnUTD52zQBI+0N9KGeCQjqcwEuEBx8hhQiZ3Fz+jSFG1kk15xH7/4qpORcrXrdu5roY9o5uyBo5wK9Vua2IFRp7NhH6++p77M1m2osvnlyLDuxasPuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2GgAs3DVGTI0PsiOSRxjfcU+PDsRuNpcWNcZdF0lWoFD/AmNmR9"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 97
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": 97
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 97
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 97
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 97
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 97,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 821,
      "height": 97,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 97
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": 97
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 97
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 97
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 97
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 97,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 821,
      "height": 97,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "ABCDEFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 98,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 83,
      "height": 98,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_RWJldF9hbHJlYWR5X3Rha2VuiHO7fw=="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "ABCDEFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "ABCDEFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "ABCDEFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53YqC4MNlnwD/iRKHXDD6sad/7AuNgYrIG/GHCiUfXunVy9SoSOEc=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421707,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDDwYScgw3wypeENbtFG8R+zUq1kBCXmkSZ2ELxOSAQXfBlfyLeQ12k8fKTcY7UY9VArlFPZjdRTbVMqxoHtYEBuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2KguDDZZ8A/4kSh1ww+rGnf+wLjYGKyBvxhwolH17p1cvVeTMos"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421707,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDDwYScgw3wypeENbtFG8R+zUq1kBCXmkSZ2ELxOSAQXfBlfyLeQ12k8fKTcY7UY9VArlFPZjdRTbVMqxoHtYEBuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2KguDDZZ8A/4kSh1ww+rGnf+wLjYGKyBvxhwolH17p1cvVeTMos",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421706,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECJWPP5UOT1sGrhAqvqF2lSBZxKNRuZAeisD5MclfMqRfwYQH4QQZ4myl9g7lFlDy8JTjqTcMBpZZvkzZhMWpYBuEDDwYScgw3wypeENbtFG8R+zUq1kBCXmkSZ2ELxOSAQXfBlfyLeQ12k8fKTcY7UY9VArlFPZjdRTbVMqxoHtYEBuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2KguDDZZ8A/4kSh1ww+rGnf+wLjYGKyBvxhwolH17p1cvWFNTnM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421706,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuECJWPP5UOT1sGrhAqvqF2lSBZxKNRuZAeisD5MclfMqRfwYQH4QQZ4myl9g7lFlDy8JTjqTcMBpZZvkzZhMWpYBuEDDwYScgw3wypeENbtFG8R+zUq1kBCXmkSZ2ELxOSAQXfBlfyLeQ12k8fKTcY7UY9VArlFPZjdRTbVMqxoHtYEBuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2KguDDZZ8A/4kSh1ww+rGnf+wLjYGKyBvxhwolH17p1cvWFNTnM"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuECJWPP5UOT1sGrhAqvqF2lSBZxKNRuZAeisD5MclfMqRfwYQH4QQZ4myl9g7lFlDy8JTjqTcMBpZZvkzZhMWpYBuEDDwYScgw3wypeENbtFG8R+zUq1kBCXmkSZ2ELxOSAQXfBlfyLeQ12k8fKTcY7UY9VArlFPZjdRTbVMqxoHtYEBuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2KguDDZZ8A/4kSh1ww+rGnf+wLjYGKyBvxhwolH17p1cvWFNTnM"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 98
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": 98
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 98
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 98
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 98
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 98,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 83,
      "height": 98,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_RWJldF9hbHJlYWR5X3Rha2VuiHO7fw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 98
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": 98
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 98
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 98
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 98
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 98,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 83,
      "height": 98,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_RWJldF9hbHJlYWR5X3Rha2VuiHO7fw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "ABCDEFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 99,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 83,
      "height": 99,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_RWJldF9hbHJlYWR5X3Rha2VuiHO7fw=="
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "ABCDEFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "ABCDEFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "ABCDEFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2cpvs1iPSahSkBtU1vpp6GeWAqErFNk1KG7LY3vSFZFCgLsUms",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53Y6BodUpFyEVTc8GUKW9SmgXOkiLaYyeswUDYRujRxUIuVNw+TOE=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421705,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBCHacGdZ+QnUcoBaV+w8+Dzdpyj7OBIX9z5t2d2LukdLP0h0eHztQMt4myokwbs8Lt1NZwOiuu8DVl5HkxqfgOuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2OgaHVKRchFU3PBlClvUpoFzpIi2mMnrMFA2Ebo0cVCLlQ483K/"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421705,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBCHacGdZ+QnUcoBaV+w8+Dzdpyj7OBIX9z5t2d2LukdLP0h0eHztQMt4myokwbs8Lt1NZwOiuu8DVl5HkxqfgOuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2OgaHVKRchFU3PBlClvUpoFzpIi2mMnrMFA2Ebo0cVCLlQ483K/",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421704,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBCHacGdZ+QnUcoBaV+w8+Dzdpyj7OBIX9z5t2d2LukdLP0h0eHztQMt4myokwbs8Lt1NZwOiuu8DVl5HkxqfgOuEDmt3oF1lIqiRGuERVNTCXIK62XkZghczriOAPYKFNz1cqFXfQ6mq6qM4hussfdNzJkkygz+6NDfKDA7yE3DJ4HuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2OgaHVKRchFU3PBlClvUpoFzpIi2mMnrMFA2Ebo0cVCLlS74Vtg"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421704,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBCHacGdZ+QnUcoBaV+w8+Dzdpyj7OBIX9z5t2d2LukdLP0h0eHztQMt4myokwbs8Lt1NZwOiuu8DVl5HkxqfgOuEDmt3oF1lIqiRGuERVNTCXIK62XkZghczriOAPYKFNz1cqFXfQ6mq6qM4hussfdNzJkkygz+6NDfKDA7yE3DJ4HuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2OgaHVKRchFU3PBlClvUpoFzpIi2mMnrMFA2Ebo0cVCLlS74Vtg"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBCHacGdZ+QnUcoBaV+w8+Dzdpyj7OBIX9z5t2d2LukdLP0h0eHztQMt4myokwbs8Lt1NZwOiuu8DVl5HkxqfgOuEDmt3oF1lIqiRGuERVNTCXIK62XkZghczriOAPYKFNz1cqFXfQ6mq6qM4hussfdNzJkkygz+6NDfKDA7yE3DJ4HuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2OgaHVKRchFU3PBlClvUpoFzpIi2mMnrMFA2Ebo0cVCLlS74Vtg"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 99
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": 99
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 99
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 99
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 99
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 99,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 83,
      "height": 99,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_RWJldF9hbHJlYWR5X3Rha2VuiHO7fw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 99
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": 99
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 99
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 99
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 99
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 99,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 83,
      "height": 99,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_RWJldF9hbHJlYWR5X3Rha2VuiHO7fw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
        "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
        "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
    "call_data": "ABCDEFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 100,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 263,
      "height": 100,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_SWRpZmZlcmVudCBxdWVzdGlvbpFHdWg="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
        "call_data": "ABCDEFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
        "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
        "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
        "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
    "call_data": "ABCDEFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
        "call_data": "ABCDEFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
        "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ZKDoGjsbvk0mPjCclBIxUQkpB/qX1WJneC1ByoCr1EQnmy2nejM=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421703,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECUYHFeDRltC89hw7BEhSmpr9P/X7RPJr3j3ID7wO8z1GOk33ETO+Rl6RMGxojuHsl5cALVYUvBbdDQQA/kfTQLuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2Sg6Bo7G75NJj4wnJQSMVEJKQf6l9ViZ3gtQcqAq9REJ5vFExXl"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421703,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuECUYHFeDRltC89hw7BEhSmpr9P/X7RPJr3j3ID7wO8z1GOk33ETO+Rl6RMGxojuHsl5cALVYUvBbdDQQA/kfTQLuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2Sg6Bo7G75NJj4wnJQSMVEJKQf6l9ViZ3gtQcqAq9REJ5vFExXl",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421702,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECUYHFeDRltC89hw7BEhSmpr9P/X7RPJr3j3ID7wO8z1GOk33ETO+Rl6RMGxojuHsl5cALVYUvBbdDQQA/kfTQLuED3dd23ejBh3qCVW8miOcAF3/PJ/pdJSX8FvmTjdKXZvtPtM2dXEZ8qEETX86etjDYVQ2G18e3s8SKUPl0GcZgDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2Sg6Bo7G75NJj4wnJQSMVEJKQf6l9ViZ3gtQcqAq9REJ5tqXrJz"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421702,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuECUYHFeDRltC89hw7BEhSmpr9P/X7RPJr3j3ID7wO8z1GOk33ETO+Rl6RMGxojuHsl5cALVYUvBbdDQQA/kfTQLuED3dd23ejBh3qCVW8miOcAF3/PJ/pdJSX8FvmTjdKXZvtPtM2dXEZ8qEETX86etjDYVQ2G18e3s8SKUPl0GcZgDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2Sg6Bo7G75NJj4wnJQSMVEJKQf6l9ViZ3gtQcqAq9REJ5tqXrJz"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuECUYHFeDRltC89hw7BEhSmpr9P/X7RPJr3j3ID7wO8z1GOk33ETO+Rl6RMGxojuHsl5cALVYUvBbdDQQA/kfTQLuED3dd23ejBh3qCVW8miOcAF3/PJ/pdJSX8FvmTjdKXZvtPtM2dXEZ8qEETX86etjDYVQ2G18e3s8SKUPl0GcZgDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2Sg6Bo7G75NJj4wnJQSMVEJKQf6l9ViZ3gtQcqAq9REJ5tqXrJz"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 100
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": 100
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 100
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 100
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 100
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 100,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 263,
      "height": 100,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_SWRpZmZlcmVudCBxdWVzdGlvbpFHdWg="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 100
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": 100
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 100
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 100
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 100
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 100,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 263,
      "height": 100,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_SWRpZmZlcmVudCBxdWVzdGlvbpFHdWg="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
        "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
        "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
    "call_data": "ABCDEFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 101,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 263,
      "height": 101,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_SWRpZmZlcmVudCBxdWVzdGlvbpFHdWg="
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
        "call_data": "ABCDEFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
        "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
        "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
        "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
    "call_data": "ABCDEFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
        "call_data": "ABCDEFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
        "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2DrVHjP5WznzyyGUHDQWYjeDSq4bZWKKJEpVbMpFjyy4X6JB9e",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ZaAJV4tiFjz65efzlWoBseiXgIyYKCR5GThNy36ZgKQqCS2vEts=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421701,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEApVew1K8dT0stFAo4GuIDsG6FDhyd+jeQlR2Mrzd2kfvu1hFGzXKalkeLROdAGrRGA+H+nkC0mtMNMaiTRRmYNuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2WgCVeLYhY8+uXn85VqAbHol4CMmCgkeRk4Tct+mYCkKgm5C+0Z"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421701,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEApVew1K8dT0stFAo4GuIDsG6FDhyd+jeQlR2Mrzd2kfvu1hFGzXKalkeLROdAGrRGA+H+nkC0mtMNMaiTRRmYNuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2WgCVeLYhY8+uXn85VqAbHol4CMmCgkeRk4Tct+mYCkKgm5C+0Z",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421700,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEApVew1K8dT0stFAo4GuIDsG6FDhyd+jeQlR2Mrzd2kfvu1hFGzXKalkeLROdAGrRGA+H+nkC0mtMNMaiTRRmYNuEC6kkc6rZj7dLua5vrlK3IjAbsIDJesy1JAEOp5wh0u9Vucu2Sj9fuguuGBm28my7AoPbwGK+v12JZOFxjAewIFuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2WgCVeLYhY8+uXn85VqAbHol4CMmCgkeRk4Tct+mYCkKgkt9M1R"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421700,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEApVew1K8dT0stFAo4GuIDsG6FDhyd+jeQlR2Mrzd2kfvu1hFGzXKalkeLROdAGrRGA+H+nkC0mtMNMaiTRRmYNuEC6kkc6rZj7dLua5vrlK3IjAbsIDJesy1JAEOp5wh0u9Vucu2Sj9fuguuGBm28my7AoPbwGK+v12JZOFxjAewIFuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2WgCVeLYhY8+uXn85VqAbHol4CMmCgkeRk4Tct+mYCkKgkt9M1R"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEApVew1K8dT0stFAo4GuIDsG6FDhyd+jeQlR2Mrzd2kfvu1hFGzXKalkeLROdAGrRGA+H+nkC0mtMNMaiTRRmYNuEC6kkc6rZj7dLua5vrlK3IjAbsIDJesy1JAEOp5wh0u9Vucu2Sj9fuguuGBm28my7AoPbwGK+v12JZOFxjAewIFuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2WgCVeLYhY8+uXn85VqAbHol4CMmCgkeRk4Tct+mYCkKgkt9M1R"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 101
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": 101
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 101
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 101
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 101
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 101,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 263,
      "height": 101,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_SWRpZmZlcmVudCBxdWVzdGlvbpFHdWg="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 101
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": 101
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 101
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 101
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 101
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 101,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 263,
      "height": 101,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_SWRpZmZlcmVudCBxdWVzdGlvbpFHdWg="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421699,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421699,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "owner_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421698,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421698,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "owner_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421697,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421697,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "balance": 69999999999969
    },
    {
      "account": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "balance": 39999999999981
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
        "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
        "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "ABCDEFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 102,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 325,
      "height": 102,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_OW5vIHdpbm5pbmcgYmV0r9Yizg=="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
        "call_data": "ABCDEFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
        "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
        "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
        "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "ABCDEFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
        "call_data": "ABCDEFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
        "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ZqDeOy1ZPDYYAWxBVyw7AABp0ucMyMT2fg0MuJaWZsodoEAVtOs=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421696,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECEdeH48Lz9O+iYcotx4DY2yChIwMTcSglPwVUxLd+EfB3fugttJPwta+fBnbGHtfz7pubHShYJKDAG55kAKSIFuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2ag3jstWTw2GAFsQVcsOwAAadLnDMjE9n4NDLiWlmbKHaB/FdUM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuECEdeH48Lz9O+iYcotx4DY2yChIwMTcSglPwVUxLd+EfB3fugttJPwta+fBnbGHtfz7pubHShYJKDAG55kAKSIFuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2ag3jstWTw2GAFsQVcsOwAAadLnDMjE9n4NDLiWlmbKHaB/FdUM",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421695,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBJCkeypfl6YKcYBIsgJIRuNX0rH2j1wZgKeOKyaZiWi4sv/231Lpw9SNkucjl4NKCqEbLczQG5TMSEp5iggWUDuECEdeH48Lz9O+iYcotx4DY2yChIwMTcSglPwVUxLd+EfB3fugttJPwta+fBnbGHtfz7pubHShYJKDAG55kAKSIFuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2ag3jstWTw2GAFsQVcsOwAAadLnDMjE9n4NDLiWlmbKHaBpgVxI"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBJCkeypfl6YKcYBIsgJIRuNX0rH2j1wZgKeOKyaZiWi4sv/231Lpw9SNkucjl4NKCqEbLczQG5TMSEp5iggWUDuECEdeH48Lz9O+iYcotx4DY2yChIwMTcSglPwVUxLd+EfB3fugttJPwta+fBnbGHtfz7pubHShYJKDAG55kAKSIFuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2ag3jstWTw2GAFsQVcsOwAAadLnDMjE9n4NDLiWlmbKHaBpgVxI"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBJCkeypfl6YKcYBIsgJIRuNX0rH2j1wZgKeOKyaZiWi4sv/231Lpw9SNkucjl4NKCqEbLczQG5TMSEp5iggWUDuECEdeH48Lz9O+iYcotx4DY2yChIwMTcSglPwVUxLd+EfB3fugttJPwta+fBnbGHtfz7pubHShYJKDAG55kAKSIFuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2ag3jstWTw2GAFsQVcsOwAAadLnDMjE9n4NDLiWlmbKHaBpgVxI"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 102
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": 102
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 102
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 102
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 102
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 102,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 325,
      "height": 102,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_OW5vIHdpbm5pbmcgYmV0r9Yizg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 102
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": 102
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 102
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 102
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 102
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 102,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 325,
      "height": 102,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_OW5vIHdpbm5pbmcgYmV0r9Yizg=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421694,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421694,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "owner_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421693,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421693,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "owner_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421692,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421692,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "balance": 69999999999969
    },
    {
      "account": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "balance": 39999999999981
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "ABCDEFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 103,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 446,
      "height": 103,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
        "call_data": "ABCDEFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "ABCDEFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
        "call_data": "ABCDEFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53Z6CYYd9cUuLxD64ZiULceRJ08t2N5o706WGKbWys27Tsr47ofhI=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421691,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAAMV8ntd0gzk5pevb/wyJqGZE1i2pPyHAq081z9R5vsd0MFKoQGgHqAN+OUuuiFQ0LMYMz1jk1ovAKFclhIrgFuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2egmGHfXFLi8Q+uGYlC3HkSdPLdjeaO9Olhim1srNu07K962lJA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421691,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAAMV8ntd0gzk5pevb/wyJqGZE1i2pPyHAq081z9R5vsd0MFKoQGgHqAN+OUuuiFQ0LMYMz1jk1ovAKFclhIrgFuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2egmGHfXFLi8Q+uGYlC3HkSdPLdjeaO9Olhim1srNu07K962lJA",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421690,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAAMV8ntd0gzk5pevb/wyJqGZE1i2pPyHAq081z9R5vsd0MFKoQGgHqAN+OUuuiFQ0LMYMz1jk1ovAKFclhIrgFuED/hbWvDrIsFNkpEgcAC3dIDL/TNwEmkYVF88WRoVhlNv/0oktQSmKIDRk3lmcmtxac56unoN0goXaaWpAHcY8OuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2egmGHfXFLi8Q+uGYlC3HkSdPLdjeaO9Olhim1srNu07K9DGH/1"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEAAMV8ntd0gzk5pevb/wyJqGZE1i2pPyHAq081z9R5vsd0MFKoQGgHqAN+OUuuiFQ0LMYMz1jk1ovAKFclhIrgFuED/hbWvDrIsFNkpEgcAC3dIDL/TNwEmkYVF88WRoVhlNv/0oktQSmKIDRk3lmcmtxac56unoN0goXaaWpAHcY8OuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2egmGHfXFLi8Q+uGYlC3HkSdPLdjeaO9Olhim1srNu07K9DGH/1"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEAAMV8ntd0gzk5pevb/wyJqGZE1i2pPyHAq081z9R5vsd0MFKoQGgHqAN+OUuuiFQ0LMYMz1jk1ovAKFclhIrgFuED/hbWvDrIsFNkpEgcAC3dIDL/TNwEmkYVF88WRoVhlNv/0oktQSmKIDRk3lmcmtxac56unoN0goXaaWpAHcY8OuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2egmGHfXFLi8Q+uGYlC3HkSdPLdjeaO9Olhim1srNu07K9DGH/1"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 103
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": 103
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 103
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 103
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 103
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 103,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 446,
      "height": 103,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 103
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": 103
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 103
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 103
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 103
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 103,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 446,
      "height": 103,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
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
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421689,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "owner_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu"
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
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421688,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "owner_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421687,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421687,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "balance": 69999999999969
    },
    {
      "account": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "balance": 39999999999981
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421686,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421686,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "balance": 10
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
        "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
        "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "ABCDEFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 104,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 466,
      "height": 104,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
        "call_data": "ABCDEFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
        "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
        "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
        "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "ABCDEFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
        "call_data": "ABCDEFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
        "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_88L3wHiZgyQuC1auh42GU8cPeW7Z5h4o4Au1CpDmrtq8dS1BG",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53aKA6sNzjxiY6T+PlEbWyP1+Fss4FhW61+P6fq9EVGeiPibdzTsE=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421685,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDELi7IE3dfRm5e3lmfwoEBksY4kMbya0d6zQhXE3cqQIHXQWIZnYWbZK1DQ6k4WDHx+GaCD/qmHy9PaBO4YhIPuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2igOrDc48YmOk/j5RG1sj9fhbLOBYVutfj+n6vRFRnoj4m/Tgay"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421685,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDELi7IE3dfRm5e3lmfwoEBksY4kMbya0d6zQhXE3cqQIHXQWIZnYWbZK1DQ6k4WDHx+GaCD/qmHy9PaBO4YhIPuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2igOrDc48YmOk/j5RG1sj9fhbLOBYVutfj+n6vRFRnoj4m/Tgay",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421684,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECfXJz+i6HWF6jKAnlHa6lwFm0xz+711Z13PR8ZVMntoe35VQSS1HqcEWheWEbzcrfBOTTY7i671xrtCdsG49gCuEDELi7IE3dfRm5e3lmfwoEBksY4kMbya0d6zQhXE3cqQIHXQWIZnYWbZK1DQ6k4WDHx+GaCD/qmHy9PaBO4YhIPuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2igOrDc48YmOk/j5RG1sj9fhbLOBYVutfj+n6vRFRnoj4kx1j88"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421684,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuECfXJz+i6HWF6jKAnlHa6lwFm0xz+711Z13PR8ZVMntoe35VQSS1HqcEWheWEbzcrfBOTTY7i671xrtCdsG49gCuEDELi7IE3dfRm5e3lmfwoEBksY4kMbya0d6zQhXE3cqQIHXQWIZnYWbZK1DQ6k4WDHx+GaCD/qmHy9PaBO4YhIPuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2igOrDc48YmOk/j5RG1sj9fhbLOBYVutfj+n6vRFRnoj4kx1j88"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuECfXJz+i6HWF6jKAnlHa6lwFm0xz+711Z13PR8ZVMntoe35VQSS1HqcEWheWEbzcrfBOTTY7i671xrtCdsG49gCuEDELi7IE3dfRm5e3lmfwoEBksY4kMbya0d6zQhXE3cqQIHXQWIZnYWbZK1DQ6k4WDHx+GaCD/qmHy9PaBO4YhIPuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2igOrDc48YmOk/j5RG1sj9fhbLOBYVutfj+n6vRFRnoj4kx1j88"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 104
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": 104
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 104
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 104
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 104
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 104,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 466,
      "height": 104,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 104
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
        "round": 104
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 104
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 104
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
    "round": 104
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 104,
      "contract_id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "gas_price": 1,
      "gas_used": 466,
      "height": 104,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421683,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421683,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "owner_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421682,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421682,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "owner_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421681,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421681,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "balance": 0
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421680,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421680,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_HBJwpRyMidyGEaW1ZNUohCYx2fFMRzgyMW3WNzMxzu9fjZGvF",
      "balance": 0
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421679,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421679,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "balance": 69999999999979
    },
    {
      "account": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "balance": 39999999999981
    }
  ],
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
      "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421678,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "balance": 69999999999979
    },
    {
      "account": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "balance": 39999999999981
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 3,
    "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
    "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
    "deposit": "1",
    "vm_version": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
        "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
        "deposit": "1",
        "vm_version": 7
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
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 3,
    "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
    "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
    "deposit": 10,
    "vm_version": "1"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
        "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
        "deposit": 10,
        "vm_version": "1"
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
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": "1",
    "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
    "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
    "deposit": 10,
    "vm_version": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": "1",
        "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
        "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
        "deposit": 10,
        "vm_version": 7
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
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 3,
    "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
    "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
    "deposit": 10,
    "vm_version": 7
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53aaBaxZGkLjioXWzBKiS0qAhc8DPrjBB+yBKa1sKOeE6rLb2IZeM=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
          "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "vm_version": 7
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
  "id": -576460752303421677,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECHBzw3jjyvdywstk6U6KCVWyrIijoNI/ajyPBR2R/pYTxidUA2nrEuwCQlopltfgLFdc7XVgz+AIghSsyNubEOuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2mgWsWRpC44qF1swSoktKgIXPAz64wQfsgSmtbCjnhOqy0+nEf2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421677,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuECHBzw3jjyvdywstk6U6KCVWyrIijoNI/ajyPBR2R/pYTxidUA2nrEuwCQlopltfgLFdc7XVgz+AIghSsyNubEOuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2mgWsWRpC44qF1swSoktKgIXPAz64wQfsgSmtbCjnhOqy0+nEf2",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
          "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "vm_version": 7
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
  "id": -576460752303421676,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAjBhDWh4vrdY7x3ISYQ0bIyUbsr7oBswUa5tAeu9LirA1LaMJ856mnSQQ9eRdtUm09KrosVgHZVyxGlHF2y9UKuECHBzw3jjyvdywstk6U6KCVWyrIijoNI/ajyPBR2R/pYTxidUA2nrEuwCQlopltfgLFdc7XVgz+AIghSsyNubEOuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2mgWsWRpC44qF1swSoktKgIXPAz64wQfsgSmtbCjnhOqy3Qmk4F"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421676,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEAjBhDWh4vrdY7x3ISYQ0bIyUbsr7oBswUa5tAeu9LirA1LaMJ856mnSQQ9eRdtUm09KrosVgHZVyxGlHF2y9UKuECHBzw3jjyvdywstk6U6KCVWyrIijoNI/ajyPBR2R/pYTxidUA2nrEuwCQlopltfgLFdc7XVgz+AIghSsyNubEOuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2mgWsWRpC44qF1swSoktKgIXPAz64wQfsgSmtbCjnhOqy3Qmk4F"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEAjBhDWh4vrdY7x3ISYQ0bIyUbsr7oBswUa5tAeu9LirA1LaMJ856mnSQQ9eRdtUm09KrosVgHZVyxGlHF2y9UKuECHBzw3jjyvdywstk6U6KCVWyrIijoNI/ajyPBR2R/pYTxidUA2nrEuwCQlopltfgLFdc7XVgz+AIghSsyNubEOuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2mgWsWRpC44qF1swSoktKgIXPAz64wQfsgSmtbCjnhOqy3Qmk4F"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421675,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421675,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "owner_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwCs9rhl",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_LwCs9rhl"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421674,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421674,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "owner_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwCs9rhl",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_LwCs9rhl"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 106,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 331,
      "height": 106,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53aqAE3svHYKp0s1B3JHxDSrML6PFQqjRea9DAaH91N+fQXYQ7sxc=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421673,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAPLeoCOdMApEpIUBWvaHsBGTUynzZZ1yzRXrSSmF12kVrHwSe56ojcXtcdIRmYZCnb84ZGB5knvAh/MUOiARkDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2qgBN7Lx2CqdLNQdyR8Q0qzC+jxUKo0XmvQwGh/dTfn0F3kASo9"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421673,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAPLeoCOdMApEpIUBWvaHsBGTUynzZZ1yzRXrSSmF12kVrHwSe56ojcXtcdIRmYZCnb84ZGB5knvAh/MUOiARkDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2qgBN7Lx2CqdLNQdyR8Q0qzC+jxUKo0XmvQwGh/dTfn0F3kASo9",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421672,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAPLeoCOdMApEpIUBWvaHsBGTUynzZZ1yzRXrSSmF12kVrHwSe56ojcXtcdIRmYZCnb84ZGB5knvAh/MUOiARkDuEDO/ROw1hksBTLGjhw6BWpt0SxNdNtAEQxkj27PfPMtDXudjqscLHIrfirR1r2Ja8YT4Ao6ohndwrBkt6C60bEHuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2qgBN7Lx2CqdLNQdyR8Q0qzC+jxUKo0XmvQwGh/dTfn0F3oYRCC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421672,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEAPLeoCOdMApEpIUBWvaHsBGTUynzZZ1yzRXrSSmF12kVrHwSe56ojcXtcdIRmYZCnb84ZGB5knvAh/MUOiARkDuEDO/ROw1hksBTLGjhw6BWpt0SxNdNtAEQxkj27PfPMtDXudjqscLHIrfirR1r2Ja8YT4Ao6ohndwrBkt6C60bEHuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2qgBN7Lx2CqdLNQdyR8Q0qzC+jxUKo0XmvQwGh/dTfn0F3oYRCC"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEAPLeoCOdMApEpIUBWvaHsBGTUynzZZ1yzRXrSSmF12kVrHwSe56ojcXtcdIRmYZCnb84ZGB5knvAh/MUOiARkDuEDO/ROw1hksBTLGjhw6BWpt0SxNdNtAEQxkj27PfPMtDXudjqscLHIrfirR1r2Ja8YT4Ao6ohndwrBkt6C60bEHuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2qgBN7Lx2CqdLNQdyR8Q0qzC+jxUKo0XmvQwGh/dTfn0F3oYRCC"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 106
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": 106
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 106
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 106
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 106
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 106,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 331,
      "height": 106,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 106
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": 106
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 106
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 106
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 106
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 106,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 331,
      "height": 106,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 107,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 556,
      "height": 107,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53a6AqJ2Gz7iuDRxcIlfLV4+V0xl8tPrvF2DAlL/PbXEB6/U8Zv8g=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421671,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBJoXVp0lf7Ym4RUCmIcOgTuRahUyZTPZ6hgNW8HVxw+6A1UvlsW2YN1n7reqH0uNbUGNB+HeLjVQWZxPN6ExYKuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2ugKidhs+4rg0cXCJXy1ePldMZfLT67xdgwJS/z21xAev3PeQul"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421671,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBJoXVp0lf7Ym4RUCmIcOgTuRahUyZTPZ6hgNW8HVxw+6A1UvlsW2YN1n7reqH0uNbUGNB+HeLjVQWZxPN6ExYKuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2ugKidhs+4rg0cXCJXy1ePldMZfLT67xdgwJS/z21xAev3PeQul",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421670,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBJoXVp0lf7Ym4RUCmIcOgTuRahUyZTPZ6hgNW8HVxw+6A1UvlsW2YN1n7reqH0uNbUGNB+HeLjVQWZxPN6ExYKuEBaG6IWW7aV8VL9zbV6yteAZmEg9l3JMFG9X4EqVjKxQLL7d5kR2DqlHT6gXIYNRglrTnY8xol6JZAg98iWBjQJuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2ugKidhs+4rg0cXCJXy1ePldMZfLT67xdgwJS/z21xAev3eoCur"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBJoXVp0lf7Ym4RUCmIcOgTuRahUyZTPZ6hgNW8HVxw+6A1UvlsW2YN1n7reqH0uNbUGNB+HeLjVQWZxPN6ExYKuEBaG6IWW7aV8VL9zbV6yteAZmEg9l3JMFG9X4EqVjKxQLL7d5kR2DqlHT6gXIYNRglrTnY8xol6JZAg98iWBjQJuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2ugKidhs+4rg0cXCJXy1ePldMZfLT67xdgwJS/z21xAev3eoCur"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBJoXVp0lf7Ym4RUCmIcOgTuRahUyZTPZ6hgNW8HVxw+6A1UvlsW2YN1n7reqH0uNbUGNB+HeLjVQWZxPN6ExYKuEBaG6IWW7aV8VL9zbV6yteAZmEg9l3JMFG9X4EqVjKxQLL7d5kR2DqlHT6gXIYNRglrTnY8xol6JZAg98iWBjQJuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2ugKidhs+4rg0cXCJXy1ePldMZfLT67xdgwJS/z21xAev3eoCur"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 107
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": 107
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 107
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 107
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 107
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 107,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 556,
      "height": 107,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 107
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": 107
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 107
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 107
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 107
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 107,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 556,
      "height": 107,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421669,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421669,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "owner_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwCs9rhl",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_LwIVSSB3aW6fAKB89BjMgOBNHvEAzlMeLv0uW/JoSso+N7CW9pYkrtabqyVubywgSSB3aW6fAKDfa5vKbvnIUY8yeaw2mF6ECMypgIbbXeGHfVElueryTdAcfSI="
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
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421668,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "owner_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwCs9rhl",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_LwIVSSB3aW6fAKB89BjMgOBNHvEAzlMeLv0uW/JoSso+N7CW9pYkrtabqyVubywgSSB3aW6fAKDfa5vKbvnIUY8yeaw2mF6ECMypgIbbXeGHfVElueryTdAcfSI="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 108,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 821,
      "height": 108,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53bKBueS39iJzLHu11NLLFb2O1uAo9il6SP8lqhXhMF/XUHLKfA3U=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421667,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDZ36sUkuF+XWwC65DyGHCQWJxhyZCCxl25wbPw1OghgiSLz180V+2ib6Wp0s0bu77dk4NY8OXBV9hT1POvaQYEuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2ygbnkt/Yicyx7tdTSyxW9jtbgKPYpekj/JaoV4TBf11Bxlxfp/"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421667,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDZ36sUkuF+XWwC65DyGHCQWJxhyZCCxl25wbPw1OghgiSLz180V+2ib6Wp0s0bu77dk4NY8OXBV9hT1POvaQYEuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2ygbnkt/Yicyx7tdTSyxW9jtbgKPYpekj/JaoV4TBf11Bxlxfp/",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421666,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA4NMAzALhMDVAh2IY/BzDSWE0lbJgtNp+viXgjuSjotZQlkiFp/gd70V/mHO4hQJs7nmgaIewz2nr7Le1MKg0OuEDZ36sUkuF+XWwC65DyGHCQWJxhyZCCxl25wbPw1OghgiSLz180V+2ib6Wp0s0bu77dk4NY8OXBV9hT1POvaQYEuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2ygbnkt/Yicyx7tdTSyxW9jtbgKPYpekj/JaoV4TBf11ByDe4Bl"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEA4NMAzALhMDVAh2IY/BzDSWE0lbJgtNp+viXgjuSjotZQlkiFp/gd70V/mHO4hQJs7nmgaIewz2nr7Le1MKg0OuEDZ36sUkuF+XWwC65DyGHCQWJxhyZCCxl25wbPw1OghgiSLz180V+2ib6Wp0s0bu77dk4NY8OXBV9hT1POvaQYEuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2ygbnkt/Yicyx7tdTSyxW9jtbgKPYpekj/JaoV4TBf11ByDe4Bl"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEA4NMAzALhMDVAh2IY/BzDSWE0lbJgtNp+viXgjuSjotZQlkiFp/gd70V/mHO4hQJs7nmgaIewz2nr7Le1MKg0OuEDZ36sUkuF+XWwC65DyGHCQWJxhyZCCxl25wbPw1OghgiSLz180V+2ib6Wp0s0bu77dk4NY8OXBV9hT1POvaQYEuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2ygbnkt/Yicyx7tdTSyxW9jtbgKPYpekj/JaoV4TBf11ByDe4Bl"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 108
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": 108
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 108
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 108
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 108
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 108,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 821,
      "height": 108,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 108
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": 108
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 108
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 108
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 108
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 108,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 821,
      "height": 108,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 109,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 83,
      "height": 109,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_RWJldF9hbHJlYWR5X3Rha2VuiHO7fw=="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53baDIsVydVmlDWfY2VEXnFyu5KvztqKIZ4RF+wAABVCPhshS1b3s=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421665,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA4h8mvBTZKSMNR32NkFj17Y07c+DgJZIzX5kOrthGjTR7fpA8ca5Sp3FfhOVjkeIyg8U1a2bV7osKsw7PeJRkEuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud22gyLFcnVZpQ1n2NlRF5xcruSr87aiiGeERfsAAAVQj4bLJfPAD"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421665,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA4h8mvBTZKSMNR32NkFj17Y07c+DgJZIzX5kOrthGjTR7fpA8ca5Sp3FfhOVjkeIyg8U1a2bV7osKsw7PeJRkEuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud22gyLFcnVZpQ1n2NlRF5xcruSr87aiiGeERfsAAAVQj4bLJfPAD",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421664,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA4h8mvBTZKSMNR32NkFj17Y07c+DgJZIzX5kOrthGjTR7fpA8ca5Sp3FfhOVjkeIyg8U1a2bV7osKsw7PeJRkEuECtRVNGMWNKZ0TabMwo4Z5I8R/wnD12faRpSydG5RzJdkKB3Jwnu9PVDK9yu8o47wJQ3xpoaybApviTnw0ddjcGuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud22gyLFcnVZpQ1n2NlRF5xcruSr87aiiGeERfsAAAVQj4bIydMe1"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421664,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEA4h8mvBTZKSMNR32NkFj17Y07c+DgJZIzX5kOrthGjTR7fpA8ca5Sp3FfhOVjkeIyg8U1a2bV7osKsw7PeJRkEuECtRVNGMWNKZ0TabMwo4Z5I8R/wnD12faRpSydG5RzJdkKB3Jwnu9PVDK9yu8o47wJQ3xpoaybApviTnw0ddjcGuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud22gyLFcnVZpQ1n2NlRF5xcruSr87aiiGeERfsAAAVQj4bIydMe1"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEA4h8mvBTZKSMNR32NkFj17Y07c+DgJZIzX5kOrthGjTR7fpA8ca5Sp3FfhOVjkeIyg8U1a2bV7osKsw7PeJRkEuECtRVNGMWNKZ0TabMwo4Z5I8R/wnD12faRpSydG5RzJdkKB3Jwnu9PVDK9yu8o47wJQ3xpoaybApviTnw0ddjcGuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud22gyLFcnVZpQ1n2NlRF5xcruSr87aiiGeERfsAAAVQj4bIydMe1"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 109
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": 109
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 109
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 109
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 109
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 109,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 83,
      "height": 109,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_RWJldF9hbHJlYWR5X3Rha2VuiHO7fw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 109
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": 109
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 109
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 109
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 109
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 109,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 83,
      "height": 109,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_RWJldF9hbHJlYWR5X3Rha2VuiHO7fw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 110,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 83,
      "height": 110,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_RWJldF9hbHJlYWR5X3Rha2VuiHO7fw=="
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_2JhYpMuj1vwHS9pqVFNfjqzoA1CwDFnLqFXqD1GiGgvR8H63ow",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53bqDwEWaLfI0L/G9wwWnKmQRkik73PPwgnWyZiQIfP4M7kW9GjwQ=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421663,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDkZmth+YPO1JBI/6wf+xEdy2wR2meewdhCNWJ6jy5T45yOUN59yWdHzAlwrYHOi4iPo0a2qXTlDhTB55d+4G4HuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud26g8BFmi3yNC/xvcMFpypkEZIpO9zz8IJ1smYkCHz+DO5GGkjru"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421663,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDkZmth+YPO1JBI/6wf+xEdy2wR2meewdhCNWJ6jy5T45yOUN59yWdHzAlwrYHOi4iPo0a2qXTlDhTB55d+4G4HuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud26g8BFmi3yNC/xvcMFpypkEZIpO9zz8IJ1smYkCHz+DO5GGkjru",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421662,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAUnOWEYrA3K/NnzkvcLKzetxIfWemDSE3V8cyWF8yNhzHPTvdL+1TIFG+H81ttLe4cl0ldODx/3TGzybs6TqMHuEDkZmth+YPO1JBI/6wf+xEdy2wR2meewdhCNWJ6jy5T45yOUN59yWdHzAlwrYHOi4iPo0a2qXTlDhTB55d+4G4HuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud26g8BFmi3yNC/xvcMFpypkEZIpO9zz8IJ1smYkCHz+DO5FWNVMx"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421662,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEAUnOWEYrA3K/NnzkvcLKzetxIfWemDSE3V8cyWF8yNhzHPTvdL+1TIFG+H81ttLe4cl0ldODx/3TGzybs6TqMHuEDkZmth+YPO1JBI/6wf+xEdy2wR2meewdhCNWJ6jy5T45yOUN59yWdHzAlwrYHOi4iPo0a2qXTlDhTB55d+4G4HuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud26g8BFmi3yNC/xvcMFpypkEZIpO9zz8IJ1smYkCHz+DO5FWNVMx"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEAUnOWEYrA3K/NnzkvcLKzetxIfWemDSE3V8cyWF8yNhzHPTvdL+1TIFG+H81ttLe4cl0ldODx/3TGzybs6TqMHuEDkZmth+YPO1JBI/6wf+xEdy2wR2meewdhCNWJ6jy5T45yOUN59yWdHzAlwrYHOi4iPo0a2qXTlDhTB55d+4G4HuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud26g8BFmi3yNC/xvcMFpypkEZIpO9zz8IJ1smYkCHz+DO5FWNVMx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 110
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": 110
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 110
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 110
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 110
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 110,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 83,
      "height": 110,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_RWJldF9hbHJlYWR5X3Rha2VuiHO7fw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 110
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": 110
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 110
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 110
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 110
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 110,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 83,
      "height": 110,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_RWJldF9hbHJlYWR5X3Rha2VuiHO7fw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
        "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
        "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 111,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 263,
      "height": 111,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_SWRpZmZlcmVudCBxdWVzdGlvbpFHdWg="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
        "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
        "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
        "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
        "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53b6Dl5f2XHPtBD67bA0r20/DqmF+DkggTqXgGI2Q//LUtlI6A5Q8=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421661,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBpIflfyUFHF5exVcJUnb/mKuHLyY7wqyUI5nCPXBwPMGqdH6mqgm2dwPLHpQ84Ccx2KwzWO29H+sTCUT5UfpUDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2+g5eX9lxz7QQ+u2wNK9tPw6phfg5IIE6l4BiNkP/y1LZQuwPkU"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421661,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBpIflfyUFHF5exVcJUnb/mKuHLyY7wqyUI5nCPXBwPMGqdH6mqgm2dwPLHpQ84Ccx2KwzWO29H+sTCUT5UfpUDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2+g5eX9lxz7QQ+u2wNK9tPw6phfg5IIE6l4BiNkP/y1LZQuwPkU",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421660,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBc45pX9UUpdKTVys1SOi1IP+B4iKmHwmeTwqU/2qnCmq/dProP2RgmLhMky5Qw1t8XEXD2VJRZ3OD2xb7VbGMOuEBpIflfyUFHF5exVcJUnb/mKuHLyY7wqyUI5nCPXBwPMGqdH6mqgm2dwPLHpQ84Ccx2KwzWO29H+sTCUT5UfpUDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2+g5eX9lxz7QQ+u2wNK9tPw6phfg5IIE6l4BiNkP/y1LZQODyrg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421660,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBc45pX9UUpdKTVys1SOi1IP+B4iKmHwmeTwqU/2qnCmq/dProP2RgmLhMky5Qw1t8XEXD2VJRZ3OD2xb7VbGMOuEBpIflfyUFHF5exVcJUnb/mKuHLyY7wqyUI5nCPXBwPMGqdH6mqgm2dwPLHpQ84Ccx2KwzWO29H+sTCUT5UfpUDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2+g5eX9lxz7QQ+u2wNK9tPw6phfg5IIE6l4BiNkP/y1LZQODyrg"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBc45pX9UUpdKTVys1SOi1IP+B4iKmHwmeTwqU/2qnCmq/dProP2RgmLhMky5Qw1t8XEXD2VJRZ3OD2xb7VbGMOuEBpIflfyUFHF5exVcJUnb/mKuHLyY7wqyUI5nCPXBwPMGqdH6mqgm2dwPLHpQ84Ccx2KwzWO29H+sTCUT5UfpUDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud2+g5eX9lxz7QQ+u2wNK9tPw6phfg5IIE6l4BiNkP/y1LZQODyrg"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 111
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": 111
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 111
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 111
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 111
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 111,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 263,
      "height": 111,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_SWRpZmZlcmVudCBxdWVzdGlvbpFHdWg="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 111
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": 111
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 111
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ABCDEFG",
        "round": 111
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 111
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 111,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 263,
      "height": 111,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_SWRpZmZlcmVudCBxdWVzdGlvbpFHdWg="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
        "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
        "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 112,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 263,
      "height": 112,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_SWRpZmZlcmVudCBxdWVzdGlvbpFHdWg="
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
        "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
        "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
        "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
        "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_G77aBP7tiqmaCGMDeLqFEE5N9K4yskdrP2HZahdQGvk2RgfBv",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53cKAStFeNI9Pt2ge9n91TgBfeiK1tshke0O3FfekooEfuP5CNhco=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421659,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA6Ur9gmpIP3OxnBAClbkPTeTf8Ov3ELrA+URrVWbZRPQd2bY2Y2WXwA6UbO16bzauV/dMNuEMBe4XB/G1+HqIEuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3CgErRXjSPT7doHvZ/dU4AX3oitbbIZHtDtxX3pKKBH7j/VLWRD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421659,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA6Ur9gmpIP3OxnBAClbkPTeTf8Ov3ELrA+URrVWbZRPQd2bY2Y2WXwA6UbO16bzauV/dMNuEMBe4XB/G1+HqIEuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3CgErRXjSPT7doHvZ/dU4AX3oitbbIZHtDtxX3pKKBH7j/VLWRD",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421658,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA6Ur9gmpIP3OxnBAClbkPTeTf8Ov3ELrA+URrVWbZRPQd2bY2Y2WXwA6UbO16bzauV/dMNuEMBe4XB/G1+HqIEuEC0oRM/sRcFF5AOtvvwcu98x0mKuWSPHOMD+JNpbnSh7+A27/infz3CBgYPiFKdKuqsOP4z96lb1RUft5G8fLMDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3CgErRXjSPT7doHvZ/dU4AX3oitbbIZHtDtxX3pKKBH7j/dlQrF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421658,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEA6Ur9gmpIP3OxnBAClbkPTeTf8Ov3ELrA+URrVWbZRPQd2bY2Y2WXwA6UbO16bzauV/dMNuEMBe4XB/G1+HqIEuEC0oRM/sRcFF5AOtvvwcu98x0mKuWSPHOMD+JNpbnSh7+A27/infz3CBgYPiFKdKuqsOP4z96lb1RUft5G8fLMDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3CgErRXjSPT7doHvZ/dU4AX3oitbbIZHtDtxX3pKKBH7j/dlQrF"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEA6Ur9gmpIP3OxnBAClbkPTeTf8Ov3ELrA+URrVWbZRPQd2bY2Y2WXwA6UbO16bzauV/dMNuEMBe4XB/G1+HqIEuEC0oRM/sRcFF5AOtvvwcu98x0mKuWSPHOMD+JNpbnSh7+A27/infz3CBgYPiFKdKuqsOP4z96lb1RUft5G8fLMDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3CgErRXjSPT7doHvZ/dU4AX3oitbbIZHtDtxX3pKKBH7j/dlQrF"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 112
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": 112
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 112
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 112
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 112
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 112,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 263,
      "height": 112,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_SWRpZmZlcmVudCBxdWVzdGlvbpFHdWg="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 112
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": 112
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 112
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 112
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 112
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 112,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 263,
      "height": 112,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_SWRpZmZlcmVudCBxdWVzdGlvbpFHdWg="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421657,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421657,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "owner_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421656,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421656,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "owner_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421655,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421655,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "balance": 39999999999971
    },
    {
      "account": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "balance": 69999999999979
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
        "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
        "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 113,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 325,
      "height": 113,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_OW5vIHdpbm5pbmcgYmV0r9Yizg=="
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
        "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
        "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
        "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
        "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53caCc2TqFc2ARKAMaUaRCF1AdUA2lM/QIGHWzo207BPx0F84Hw5E=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421654,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAmTbPYBCBuCRgs+7fOfY/OJWPA3P9SXRR8K17peSibySheDAzUeSw9gtpWIqadU46vKu4x7vXQIvQJazvUhIoDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3GgnNk6hXNgESgDGlGkQhdQHVANpTP0CBh1s6NtOwT8dBe6AokY"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421654,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAmTbPYBCBuCRgs+7fOfY/OJWPA3P9SXRR8K17peSibySheDAzUeSw9gtpWIqadU46vKu4x7vXQIvQJazvUhIoDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3GgnNk6hXNgESgDGlGkQhdQHVANpTP0CBh1s6NtOwT8dBe6AokY",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421653,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAmTbPYBCBuCRgs+7fOfY/OJWPA3P9SXRR8K17peSibySheDAzUeSw9gtpWIqadU46vKu4x7vXQIvQJazvUhIoDuEBDODT7uZbR5wq09mFvfa4wy/mbGLyp6e4I1HW/vrCYtT70/O2tI6nNA/83epF3j3L2km3dJZ11aQPn/2HRchgAuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3GgnNk6hXNgESgDGlGkQhdQHVANpTP0CBh1s6NtOwT8dBe7Q6wA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421653,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEAmTbPYBCBuCRgs+7fOfY/OJWPA3P9SXRR8K17peSibySheDAzUeSw9gtpWIqadU46vKu4x7vXQIvQJazvUhIoDuEBDODT7uZbR5wq09mFvfa4wy/mbGLyp6e4I1HW/vrCYtT70/O2tI6nNA/83epF3j3L2km3dJZ11aQPn/2HRchgAuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3GgnNk6hXNgESgDGlGkQhdQHVANpTP0CBh1s6NtOwT8dBe7Q6wA"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEAmTbPYBCBuCRgs+7fOfY/OJWPA3P9SXRR8K17peSibySheDAzUeSw9gtpWIqadU46vKu4x7vXQIvQJazvUhIoDuEBDODT7uZbR5wq09mFvfa4wy/mbGLyp6e4I1HW/vrCYtT70/O2tI6nNA/83epF3j3L2km3dJZ11aQPn/2HRchgAuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3GgnNk6hXNgESgDGlGkQhdQHVANpTP0CBh1s6NtOwT8dBe7Q6wA"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 113
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": 113
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 113
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 113
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 113
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 113,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 325,
      "height": 113,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_OW5vIHdpbm5pbmcgYmV0r9Yizg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 113
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": 113
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 113
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 113
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 113
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 113,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 325,
      "height": 113,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_OW5vIHdpbm5pbmcgYmV0r9Yizg=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421652,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421652,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "owner_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421651,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421651,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "owner_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421650,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421650,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "balance": 39999999999971
    },
    {
      "account": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "balance": 69999999999979
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 114,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 446,
      "height": 114,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53cqDULIvz1DZU3Zx1QVig4OndzJYuf5ERv9oLsM9JhjU4/VPDo1Y=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421649,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBthfkXxMspQhdRqyqt7zygIaQA+J0C5IdLZUHP7PmJ/FRkMjlR/TxIHnkF6HRpVzrS/TtUR9dC4nJ8W6CbMUIBuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3Kg1CyL89Q2VN2cdUFYoODp3cyWLn+REb/aC7DPSYY1OP025+LS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421649,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBthfkXxMspQhdRqyqt7zygIaQA+J0C5IdLZUHP7PmJ/FRkMjlR/TxIHnkF6HRpVzrS/TtUR9dC4nJ8W6CbMUIBuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3Kg1CyL89Q2VN2cdUFYoODp3cyWLn+REb/aC7DPSYY1OP025+LS",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421648,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBthfkXxMspQhdRqyqt7zygIaQA+J0C5IdLZUHP7PmJ/FRkMjlR/TxIHnkF6HRpVzrS/TtUR9dC4nJ8W6CbMUIBuEDW8dRUPlaM60HAFpkHi0kzHbUKixqc1Lrf2oHB3AWNxtkT7npW757UwoJsfBvIbd74dINP5wJ/VesQDc9pzYkBuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3Kg1CyL89Q2VN2cdUFYoODp3cyWLn+REb/aC7DPSYY1OP0JiZ/w"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421648,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBthfkXxMspQhdRqyqt7zygIaQA+J0C5IdLZUHP7PmJ/FRkMjlR/TxIHnkF6HRpVzrS/TtUR9dC4nJ8W6CbMUIBuEDW8dRUPlaM60HAFpkHi0kzHbUKixqc1Lrf2oHB3AWNxtkT7npW757UwoJsfBvIbd74dINP5wJ/VesQDc9pzYkBuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3Kg1CyL89Q2VN2cdUFYoODp3cyWLn+REb/aC7DPSYY1OP0JiZ/w"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBthfkXxMspQhdRqyqt7zygIaQA+J0C5IdLZUHP7PmJ/FRkMjlR/TxIHnkF6HRpVzrS/TtUR9dC4nJ8W6CbMUIBuEDW8dRUPlaM60HAFpkHi0kzHbUKixqc1Lrf2oHB3AWNxtkT7npW757UwoJsfBvIbd74dINP5wJ/VesQDc9pzYkBuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3Kg1CyL89Q2VN2cdUFYoODp3cyWLn+REb/aC7DPSYY1OP0JiZ/w"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 114
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": 114
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 114
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 114
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 114
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 114,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 446,
      "height": 114,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 114
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": 114
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 114
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 114
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 114
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 114,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 446,
      "height": 114,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421647,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421647,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "owner_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421646,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421646,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "owner_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421645,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421645,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "balance": 39999999999971
    },
    {
      "account": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "balance": 69999999999979
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421644,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421644,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "balance": 10
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
        "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
        "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 115,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 466,
      "height": 115,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
        "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
        "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
        "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
        "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "block_hash": "kh_21aEwZpdGUmhm3Kd3pBLQ6EDeqsCWZYvnaHDrPU8DsU9hCz7pM",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53c6BrBfiBLnCoTciysyBiKPKFE7hpir2Z50z6aW/vtoltUllZXI8=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421643,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBo+IbqhbA+AVHNdm7XiICqE9Mw0YmfQLPjcD0fL5/XjHsEJrV0LQKshfVXdvdpe2wx90OFGBrNMP/4B0omVh0KuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3OgawX4gS5wqE3IsrMgYijyhRO4aYq9medM+mlv77aJbVLF0kIc"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421643,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBo+IbqhbA+AVHNdm7XiICqE9Mw0YmfQLPjcD0fL5/XjHsEJrV0LQKshfVXdvdpe2wx90OFGBrNMP/4B0omVh0KuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3OgawX4gS5wqE3IsrMgYijyhRO4aYq9medM+mlv77aJbVLF0kIc",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421642,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBo+IbqhbA+AVHNdm7XiICqE9Mw0YmfQLPjcD0fL5/XjHsEJrV0LQKshfVXdvdpe2wx90OFGBrNMP/4B0omVh0KuECwesXGHODNxA6xaSjuRSvTnowfVNI/Cnvf7F7Rq9Os9IRlENUi92hNwek+ENBi5FQHQ2D+2T/a5bvyn5Pk1IQEuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3OgawX4gS5wqE3IsrMgYijyhRO4aYq9medM+mlv77aJbVKwKjEr"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421642,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBo+IbqhbA+AVHNdm7XiICqE9Mw0YmfQLPjcD0fL5/XjHsEJrV0LQKshfVXdvdpe2wx90OFGBrNMP/4B0omVh0KuECwesXGHODNxA6xaSjuRSvTnowfVNI/Cnvf7F7Rq9Os9IRlENUi92hNwek+ENBi5FQHQ2D+2T/a5bvyn5Pk1IQEuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3OgawX4gS5wqE3IsrMgYijyhRO4aYq9medM+mlv77aJbVKwKjEr"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NILAfiEuEBo+IbqhbA+AVHNdm7XiICqE9Mw0YmfQLPjcD0fL5/XjHsEJrV0LQKshfVXdvdpe2wx90OFGBrNMP/4B0omVh0KuECwesXGHODNxA6xaSjuRSvTnowfVNI/Cnvf7F7Rq9Os9IRlENUi92hNwek+ENBi5FQHQ2D+2T/a5bvyn5Pk1IQEuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3OgawX4gS5wqE3IsrMgYijyhRO4aYq9medM+mlv77aJbVKwKjEr"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 115
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": 115
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 115
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 115
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 115
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 115,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 466,
      "height": 115,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 115
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
        "round": 115
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 115
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ABCDEFG",
        "round": 115
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
    "round": 115
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 115,
      "contract_id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "gas_price": 1,
      "gas_used": 466,
      "height": 115,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_CW9rych0Bw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421641,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421641,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "owner_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421640,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421640,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "owner_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6tpUONu",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCg32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2TAUwD"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421639,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421639,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "balance": 0
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421638,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421638,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2WMH4wxJV58rhtZRtyZtuMDz3HiTCqYPJCo1CsdcZemwQrZrWA",
      "balance": 0
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421637,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421637,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "balance": 39999999999981
    },
    {
      "account": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "balance": 69999999999979
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421636,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421636,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "balance": 39999999999981
    },
    {
      "account": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "balance": 69999999999979
    }
  ],
  "version": 1
}
```
