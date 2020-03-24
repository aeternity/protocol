
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RSKCaEi1k3zsOujh8Po/eo1EjEU8liiEx/XmL88bqZLKgCQR1rJk=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
          "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "signed_tx": "tx_+JALAfhCuEAGVFF5vB6koqLWo7HMolZmgzJ21H/XScyUvuEU+W3HHZtKRTKRVIrXT4FHP4EBbeYxhXDBoyqAh3KXQDRK9+gBuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUigmhItZN87Dro4fD6P3qNRIxFPJYohMf15i/PG6mSyoAnrXKsL"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAGVFF5vB6koqLWo7HMolZmgzJ21H/XScyUvuEU+W3HHZtKRTKRVIrXT4FHP4EBbeYxhXDBoyqAh3KXQDRK9+gBuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUigmhItZN87Dro4fD6P3qNRIxFPJYohMf15i/PG6mSyoAnrXKsL",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
          "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "signed_tx": "tx_+NILAfiEuEAGVFF5vB6koqLWo7HMolZmgzJ21H/XScyUvuEU+W3HHZtKRTKRVIrXT4FHP4EBbeYxhXDBoyqAh3KXQDRK9+gBuECCHJv1DC2HqKzOolYmRDKCDSHrMOvXNgpF2rCmmN8t0P9/1TiTGB1UDFpPK4RPuQKqBDNwSZ02sT5y2IW84p4FuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUigmhItZN87Dro4fD6P3qNRIxFPJYohMf15i/PG6mSyoAkf6woU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAGVFF5vB6koqLWo7HMolZmgzJ21H/XScyUvuEU+W3HHZtKRTKRVIrXT4FHP4EBbeYxhXDBoyqAh3KXQDRK9+gBuECCHJv1DC2HqKzOolYmRDKCDSHrMOvXNgpF2rCmmN8t0P9/1TiTGB1UDFpPK4RPuQKqBDNwSZ02sT5y2IW84p4FuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUigmhItZN87Dro4fD6P3qNRIxFPJYohMf15i/PG6mSyoAkf6woU"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAGVFF5vB6koqLWo7HMolZmgzJ21H/XScyUvuEU+W3HHZtKRTKRVIrXT4FHP4EBbeYxhXDBoyqAh3KXQDRK9+gBuECCHJv1DC2HqKzOolYmRDKCDSHrMOvXNgpF2rCmmN8t0P9/1TiTGB1UDFpPK4RPuQKqBDNwSZ02sT5y2IW84p4FuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUigmhItZN87Dro4fD6P3qNRIxFPJYohMf15i/PG6mSyoAkf6woU"
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
    "pubkey": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421801,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
      "owner_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "pubkey": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421800,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
      "owner_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 73,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RSaDNlKvLA2Qi6AqdVmhgYkkjU+QleSeNCr2E7ceGQJcJ/8PHc9M=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "signed_tx": "tx_+JALAfhCuEAhq4n6Wd6Ky3qDdYnw2AJoZ448YVPnIC2n54nWcBPP4Cb5UlZ2FLpvQrWqBgzSNjm9vIEzIA7wbM8skW3bg9YNuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUmgzZSrywNkIugKnVZoYGJJI1PkJXknjQq9hO3HhkCXCf8PYNYp"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAhq4n6Wd6Ky3qDdYnw2AJoZ448YVPnIC2n54nWcBPP4Cb5UlZ2FLpvQrWqBgzSNjm9vIEzIA7wbM8skW3bg9YNuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUmgzZSrywNkIugKnVZoYGJJI1PkJXknjQq9hO3HhkCXCf8PYNYp",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "signed_tx": "tx_+NILAfiEuEAhq4n6Wd6Ky3qDdYnw2AJoZ448YVPnIC2n54nWcBPP4Cb5UlZ2FLpvQrWqBgzSNjm9vIEzIA7wbM8skW3bg9YNuEBeMPA+RBeF8bupSsEIAdtEhY2X9M+a9safGdM4ChNd/3ZCzpPg5vvzjsCwoM/8r7g8ZRwnf4oQmgUKdW+Kl1IKuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUmgzZSrywNkIugKnVZoYGJJI1PkJXknjQq9hO3HhkCXCf8ybQdj"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAhq4n6Wd6Ky3qDdYnw2AJoZ448YVPnIC2n54nWcBPP4Cb5UlZ2FLpvQrWqBgzSNjm9vIEzIA7wbM8skW3bg9YNuEBeMPA+RBeF8bupSsEIAdtEhY2X9M+a9safGdM4ChNd/3ZCzpPg5vvzjsCwoM/8r7g8ZRwnf4oQmgUKdW+Kl1IKuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUmgzZSrywNkIugKnVZoYGJJI1PkJXknjQq9hO3HhkCXCf8ybQdj"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAhq4n6Wd6Ky3qDdYnw2AJoZ448YVPnIC2n54nWcBPP4Cb5UlZ2FLpvQrWqBgzSNjm9vIEzIA7wbM8skW3bg9YNuEBeMPA+RBeF8bupSsEIAdtEhY2X9M+a9safGdM4ChNd/3ZCzpPg5vvzjsCwoM/8r7g8ZRwnf4oQmgUKdW+Kl1IKuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUmgzZSrywNkIugKnVZoYGJJI1PkJXknjQq9hO3HhkCXCf8ybQdj"
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": 73
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 73
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 73,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": 73
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 73
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 73,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 74,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RSqDpsacltI9klMjn9fvot2mjiPcyTw4KM/uj08Wv9c7n3pXgFko=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "signed_tx": "tx_+JALAfhCuEA+BRQefJt6W6ha3HjAiuQ9sVJzQ4PDijnKbfizcjKQY47qufkQhx9CkWPEBIKeVzrmlrQFYPGzRXAelJBKLNQPuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUqg6bGnJbSPZJTI5/X76Ldpo4j3Mk8OCjP7o9PFr/XO597pE6Va"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA+BRQefJt6W6ha3HjAiuQ9sVJzQ4PDijnKbfizcjKQY47qufkQhx9CkWPEBIKeVzrmlrQFYPGzRXAelJBKLNQPuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUqg6bGnJbSPZJTI5/X76Ldpo4j3Mk8OCjP7o9PFr/XO597pE6Va",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "signed_tx": "tx_+NILAfiEuEA+BRQefJt6W6ha3HjAiuQ9sVJzQ4PDijnKbfizcjKQY47qufkQhx9CkWPEBIKeVzrmlrQFYPGzRXAelJBKLNQPuED1ovRyymoMKbDlVkNoi6StA29NkzwM3PFAoXCI7V0ibetqxtkClL/x9t393q4dunrheNLvQKExCQT24Lp4AZIIuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUqg6bGnJbSPZJTI5/X76Ldpo4j3Mk8OCjP7o9PFr/XO5950PFk4"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEA+BRQefJt6W6ha3HjAiuQ9sVJzQ4PDijnKbfizcjKQY47qufkQhx9CkWPEBIKeVzrmlrQFYPGzRXAelJBKLNQPuED1ovRyymoMKbDlVkNoi6StA29NkzwM3PFAoXCI7V0ibetqxtkClL/x9t393q4dunrheNLvQKExCQT24Lp4AZIIuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUqg6bGnJbSPZJTI5/X76Ldpo4j3Mk8OCjP7o9PFr/XO5950PFk4"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEA+BRQefJt6W6ha3HjAiuQ9sVJzQ4PDijnKbfizcjKQY47qufkQhx9CkWPEBIKeVzrmlrQFYPGzRXAelJBKLNQPuED1ovRyymoMKbDlVkNoi6StA29NkzwM3PFAoXCI7V0ibetqxtkClL/x9t393q4dunrheNLvQKExCQT24Lp4AZIIuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUqg6bGnJbSPZJTI5/X76Ldpo4j3Mk8OCjP7o9PFr/XO5950PFk4"
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": 74
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 74
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 74,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": 74
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 74
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 74,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "pubkey": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421795,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
      "owner_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwCs9rhl",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_LwIVSSB3aW6fAKC6C+jkzCIrZVHx82dNrpa0VJC54p2RyDZaBpOD0l3QPiVubywgSSB3aW6fAKAdrAHbSRoMcmZKacfrbfOnJ4yXXSZw0k/Z0DDOe8gh8NUyu2M="
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
    "pubkey": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421794,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
      "owner_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwCs9rhl",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_LwIVSSB3aW6fAKC6C+jkzCIrZVHx82dNrpa0VJC54p2RyDZaBpOD0l3QPiVubywgSSB3aW6fAKAdrAHbSRoMcmZKacfrbfOnJ4yXXSZw0k/Z0DDOe8gh8NUyu2M="
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 75,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RS6BP2/zQivqzg7HyD2pSnxhSL6fITUmgFb8R/2U8E8KJHcfnr50=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "signed_tx": "tx_+JALAfhCuEAV17jtKJ4bmD5+OdGUjdiCcNNJzIcnOw9KKBXaT2+enw/Hxvq46FvxRKHnpxJt0dLoJOcfSErK58rvaTp0XXsOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUugT9v80Ir6s4Ox8g9qUp8YUi+nyE1JoBW/Ef9lPBPCiR1KLcS0"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAV17jtKJ4bmD5+OdGUjdiCcNNJzIcnOw9KKBXaT2+enw/Hxvq46FvxRKHnpxJt0dLoJOcfSErK58rvaTp0XXsOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUugT9v80Ir6s4Ox8g9qUp8YUi+nyE1JoBW/Ef9lPBPCiR1KLcS0",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "signed_tx": "tx_+NILAfiEuEAV17jtKJ4bmD5+OdGUjdiCcNNJzIcnOw9KKBXaT2+enw/Hxvq46FvxRKHnpxJt0dLoJOcfSErK58rvaTp0XXsOuECLIfCm2spelwoeK5YD/A3JHEsRly01EnNC6pqx5MUh6Yjb4RBNJGk+pUR8R2AfWx8xcqaZJwb6dRfaZkyUs+QGuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUugT9v80Ir6s4Ox8g9qUp8YUi+nyE1JoBW/Ef9lPBPCiR1Q7L5H"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAV17jtKJ4bmD5+OdGUjdiCcNNJzIcnOw9KKBXaT2+enw/Hxvq46FvxRKHnpxJt0dLoJOcfSErK58rvaTp0XXsOuECLIfCm2spelwoeK5YD/A3JHEsRly01EnNC6pqx5MUh6Yjb4RBNJGk+pUR8R2AfWx8xcqaZJwb6dRfaZkyUs+QGuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUugT9v80Ir6s4Ox8g9qUp8YUi+nyE1JoBW/Ef9lPBPCiR1Q7L5H"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAV17jtKJ4bmD5+OdGUjdiCcNNJzIcnOw9KKBXaT2+enw/Hxvq46FvxRKHnpxJt0dLoJOcfSErK58rvaTp0XXsOuECLIfCm2spelwoeK5YD/A3JHEsRly01EnNC6pqx5MUh6Yjb4RBNJGk+pUR8R2AfWx8xcqaZJwb6dRfaZkyUs+QGuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUugT9v80Ir6s4Ox8g9qUp8YUi+nyE1JoBW/Ef9lPBPCiR1Q7L5H"
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": 75
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 75
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 75,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": 75
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 75
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 75,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 76,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RTKARQeL2LEfGyxvfCErAG66szNuGaSSQfXbVZLtrKM/y4EBF3rM=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "signed_tx": "tx_+JALAfhCuEB+TQf8nFJDb1tEB9/kVqMkSL92y8mDRouqQZc/ldQ2HQhAdZcP7/6Md8OUNXLxBwMmufhxpF9oky4sMjt2yLgOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUygEUHi9ixHxssb3whKwBuurMzbhmkkkH121WS7ayjP8uCGs9+B"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB+TQf8nFJDb1tEB9/kVqMkSL92y8mDRouqQZc/ldQ2HQhAdZcP7/6Md8OUNXLxBwMmufhxpF9oky4sMjt2yLgOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUygEUHi9ixHxssb3whKwBuurMzbhmkkkH121WS7ayjP8uCGs9+B",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "signed_tx": "tx_+NILAfiEuEBn9eKqWIi5iA6pOjKYExVjH5aiDs2LenGxA7o4eBiNRr+nKGo55ZFdCsWInyjpPYMkgNHwEplPUL89mRELHLUKuEB+TQf8nFJDb1tEB9/kVqMkSL92y8mDRouqQZc/ldQ2HQhAdZcP7/6Md8OUNXLxBwMmufhxpF9oky4sMjt2yLgOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUygEUHi9ixHxssb3whKwBuurMzbhmkkkH121WS7ayjP8uB6P1IO"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBn9eKqWIi5iA6pOjKYExVjH5aiDs2LenGxA7o4eBiNRr+nKGo55ZFdCsWInyjpPYMkgNHwEplPUL89mRELHLUKuEB+TQf8nFJDb1tEB9/kVqMkSL92y8mDRouqQZc/ldQ2HQhAdZcP7/6Md8OUNXLxBwMmufhxpF9oky4sMjt2yLgOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUygEUHi9ixHxssb3whKwBuurMzbhmkkkH121WS7ayjP8uB6P1IO"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBn9eKqWIi5iA6pOjKYExVjH5aiDs2LenGxA7o4eBiNRr+nKGo55ZFdCsWInyjpPYMkgNHwEplPUL89mRELHLUKuEB+TQf8nFJDb1tEB9/kVqMkSL92y8mDRouqQZc/ldQ2HQhAdZcP7/6Md8OUNXLxBwMmufhxpF9oky4sMjt2yLgOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEUygEUHi9ixHxssb3whKwBuurMzbhmkkkH121WS7ayjP8uB6P1IO"
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": 76
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 76
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 76,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": 76
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 76
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 76,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 77,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
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
    "block_hash": "kh_2Xi669oTYkYrc9GWoUrDCnNbaMAihDB5CTCrw95hx1ANur2Sjs",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RTaBIOZ0zgV+zlp5pDm/CP6UuAyXCskRfMMgej+Z772nf8m/Z5jg=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "signed_tx": "tx_+JALAfhCuEAnOkcuPYx7IdkuQcdvQDLI5x0TrarHdg6dtDYltKxUnENSQEKh1DYkagx5BI9BhrR8OVQ5gLg3HuPE4vEf6ooHuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEU2gSDmdM4Ffs5aeaQ5vwj+lLgMlwrJEXzDIHo/me+9p3/Jep7tp"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAnOkcuPYx7IdkuQcdvQDLI5x0TrarHdg6dtDYltKxUnENSQEKh1DYkagx5BI9BhrR8OVQ5gLg3HuPE4vEf6ooHuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEU2gSDmdM4Ffs5aeaQ5vwj+lLgMlwrJEXzDIHo/me+9p3/Jep7tp",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "signed_tx": "tx_+NILAfiEuEAP1NOlQlHfcfDdGsAuxIJ863UW79zlaaR1IDRYOEKy5lnC6g2fEu4xYJidibelBpweWiaSEIvOXfcXVZ059ikBuEAnOkcuPYx7IdkuQcdvQDLI5x0TrarHdg6dtDYltKxUnENSQEKh1DYkagx5BI9BhrR8OVQ5gLg3HuPE4vEf6ooHuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEU2gSDmdM4Ffs5aeaQ5vwj+lLgMlwrJEXzDIHo/me+9p3/ICHsYM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAP1NOlQlHfcfDdGsAuxIJ863UW79zlaaR1IDRYOEKy5lnC6g2fEu4xYJidibelBpweWiaSEIvOXfcXVZ059ikBuEAnOkcuPYx7IdkuQcdvQDLI5x0TrarHdg6dtDYltKxUnENSQEKh1DYkagx5BI9BhrR8OVQ5gLg3HuPE4vEf6ooHuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEU2gSDmdM4Ffs5aeaQ5vwj+lLgMlwrJEXzDIHo/me+9p3/ICHsYM"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAP1NOlQlHfcfDdGsAuxIJ863UW79zlaaR1IDRYOEKy5lnC6g2fEu4xYJidibelBpweWiaSEIvOXfcXVZ059ikBuEAnOkcuPYx7IdkuQcdvQDLI5x0TrarHdg6dtDYltKxUnENSQEKh1DYkagx5BI9BhrR8OVQ5gLg3HuPE4vEf6ooHuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEU2gSDmdM4Ffs5aeaQ5vwj+lLgMlwrJEXzDIHo/me+9p3/ICHsYM"
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": 77
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 77
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 77,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": 77
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 77
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 77,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
        "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
        "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
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
    "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 78,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
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
    "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
        "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
        "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
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
    "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RTqD1yCbNR54YoKYL0C78rre1hWsN9q244uoqiKasMuY1qvhVPgM=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "signed_tx": "tx_+JALAfhCuEAE54+cqrWqrlmA2e/VrH95OxB18Gb0M/hWOPQRlILwFWxu5/iaA1Bkn6NWlo/XFTppCvIN3u3tfJT1+LG0ajgAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEU6g9cgmzUeeGKCmC9Au/K63tYVrDfatuOLqKoimrDLmNarqpNve"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAE54+cqrWqrlmA2e/VrH95OxB18Gb0M/hWOPQRlILwFWxu5/iaA1Bkn6NWlo/XFTppCvIN3u3tfJT1+LG0ajgAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEU6g9cgmzUeeGKCmC9Au/K63tYVrDfatuOLqKoimrDLmNarqpNve",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "signed_tx": "tx_+NILAfiEuEAE54+cqrWqrlmA2e/VrH95OxB18Gb0M/hWOPQRlILwFWxu5/iaA1Bkn6NWlo/XFTppCvIN3u3tfJT1+LG0ajgAuECl9DTK2ulaG5z+NeO9j5frHPxPS95ine6ga1SBGVNf6q/8R94p4XGIm7AozXZB73L1UjHP7TINfObmVwwXlSoNuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEU6g9cgmzUeeGKCmC9Au/K63tYVrDfatuOLqKoimrDLmNart9rJW"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAE54+cqrWqrlmA2e/VrH95OxB18Gb0M/hWOPQRlILwFWxu5/iaA1Bkn6NWlo/XFTppCvIN3u3tfJT1+LG0ajgAuECl9DTK2ulaG5z+NeO9j5frHPxPS95ine6ga1SBGVNf6q/8R94p4XGIm7AozXZB73L1UjHP7TINfObmVwwXlSoNuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEU6g9cgmzUeeGKCmC9Au/K63tYVrDfatuOLqKoimrDLmNart9rJW"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAE54+cqrWqrlmA2e/VrH95OxB18Gb0M/hWOPQRlILwFWxu5/iaA1Bkn6NWlo/XFTppCvIN3u3tfJT1+LG0ajgAuECl9DTK2ulaG5z+NeO9j5frHPxPS95ine6ga1SBGVNf6q/8R94p4XGIm7AozXZB73L1UjHP7TINfObmVwwXlSoNuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEU6g9cgmzUeeGKCmC9Au/K63tYVrDfatuOLqKoimrDLmNart9rJW"
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": 78
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 78
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 78,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": 78
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 78
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 78,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
        "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
        "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
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
    "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 79,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
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
    "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
        "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
        "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
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
    "block_hash": "kh_SB8dMLePtC3sAP7yenpc858cRcNLMYcwXdP1z7VMerjz6LkFj",
    "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RT6Dy4NCB55G6MGEhM6MtauN5ddsZ2D+kUX0HQCJD2b8jexb8sGI=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "signed_tx": "tx_+JALAfhCuEBztms1KPeLaO6l4TEFmla1QEbIKW1xTG5LGuEYCYCWBtOaipAfCrBwvMtHJ5HQbdXUrwWzw+twlMlCtDIT77YGuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEU+g8uDQgeeRujBhITOjLWrjeXXbGdg/pFF9B0AiQ9m/I3sW9g1j"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBztms1KPeLaO6l4TEFmla1QEbIKW1xTG5LGuEYCYCWBtOaipAfCrBwvMtHJ5HQbdXUrwWzw+twlMlCtDIT77YGuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEU+g8uDQgeeRujBhITOjLWrjeXXbGdg/pFF9B0AiQ9m/I3sW9g1j",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoDUTI019w06rmuJxE2beFyo1GFkbOUOP2f6cUY57j2Kv5LkdTw==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "signed_tx": "tx_+NILAfiEuEBNulm2Ggzd76ANariDDzApMjDBUSe/DG700qwTpVWjdZdIIFmsx0N7PxpOv/Ioc2Mwq0y++ew4J0gJZlWZnSgCuEBztms1KPeLaO6l4TEFmla1QEbIKW1xTG5LGuEYCYCWBtOaipAfCrBwvMtHJ5HQbdXUrwWzw+twlMlCtDIT77YGuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEU+g8uDQgeeRujBhITOjLWrjeXXbGdg/pFF9B0AiQ9m/I3sK5SSb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBNulm2Ggzd76ANariDDzApMjDBUSe/DG700qwTpVWjdZdIIFmsx0N7PxpOv/Ioc2Mwq0y++ew4J0gJZlWZnSgCuEBztms1KPeLaO6l4TEFmla1QEbIKW1xTG5LGuEYCYCWBtOaipAfCrBwvMtHJ5HQbdXUrwWzw+twlMlCtDIT77YGuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEU+g8uDQgeeRujBhITOjLWrjeXXbGdg/pFF9B0AiQ9m/I3sK5SSb"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBNulm2Ggzd76ANariDDzApMjDBUSe/DG700qwTpVWjdZdIIFmsx0N7PxpOv/Ioc2Mwq0y++ew4J0gJZlWZnSgCuEBztms1KPeLaO6l4TEFmla1QEbIKW1xTG5LGuEYCYCWBtOaipAfCrBwvMtHJ5HQbdXUrwWzw+twlMlCtDIT77YGuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEU+g8uDQgeeRujBhITOjLWrjeXXbGdg/pFF9B0AiQ9m/I3sK5SSb"
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": 79
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 79
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 79,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": 79
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 79
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 79,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "pubkey": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421783,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
      "owner_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg"
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
    "pubkey": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421782,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
      "owner_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg"
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
      "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421781,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "balance": 69999999999969
    },
    {
      "account": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
        "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
        "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 80,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
        "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
        "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RUKAEICp6LlrdW7+uaK7BjCkw53CBHomIDlIjbHusG54kITDgFoM=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "signed_tx": "tx_+JALAfhCuEDYdbrOD4C48TpIZe/l01VWmbzbJzaJy5fpvMBIWbOOH3iAzRLRiHkw/LiID+UjD4RwZJKQ1lXBrKMnaXzT1XMHuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVCgBCAqei5a3Vu/rmiuwYwpMOdwgR6JiA5SI2x7rBueJCH2IG42"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDYdbrOD4C48TpIZe/l01VWmbzbJzaJy5fpvMBIWbOOH3iAzRLRiHkw/LiID+UjD4RwZJKQ1lXBrKMnaXzT1XMHuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVCgBCAqei5a3Vu/rmiuwYwpMOdwgR6JiA5SI2x7rBueJCH2IG42",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "signed_tx": "tx_+NILAfiEuEAav5FxP3hmOjzIHKpa+C/amJ0QrtDObSm2DDG+vjTBmy2fODuSdCrucGA428cSU//nXyw86QGhZRTc9dJA9+ALuEDYdbrOD4C48TpIZe/l01VWmbzbJzaJy5fpvMBIWbOOH3iAzRLRiHkw/LiID+UjD4RwZJKQ1lXBrKMnaXzT1XMHuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVCgBCAqei5a3Vu/rmiuwYwpMOdwgR6JiA5SI2x7rBueJCGwSjDD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAav5FxP3hmOjzIHKpa+C/amJ0QrtDObSm2DDG+vjTBmy2fODuSdCrucGA428cSU//nXyw86QGhZRTc9dJA9+ALuEDYdbrOD4C48TpIZe/l01VWmbzbJzaJy5fpvMBIWbOOH3iAzRLRiHkw/LiID+UjD4RwZJKQ1lXBrKMnaXzT1XMHuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVCgBCAqei5a3Vu/rmiuwYwpMOdwgR6JiA5SI2x7rBueJCGwSjDD"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAav5FxP3hmOjzIHKpa+C/amJ0QrtDObSm2DDG+vjTBmy2fODuSdCrucGA428cSU//nXyw86QGhZRTc9dJA9+ALuEDYdbrOD4C48TpIZe/l01VWmbzbJzaJy5fpvMBIWbOOH3iAzRLRiHkw/LiID+UjD4RwZJKQ1lXBrKMnaXzT1XMHuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVCgBCAqei5a3Vu/rmiuwYwpMOdwgR6JiA5SI2x7rBueJCGwSjDD"
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": 80
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 80
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 80,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": 80
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 80
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 80,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "pubkey": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421778,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
      "owner_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg"
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
    "pubkey": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421777,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
      "owner_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg"
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
      "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421776,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "balance": 69999999999969
    },
    {
      "account": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 81,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RUaDSHvRZB2EP/lFy9utljALY8l3CBAaVIqAJIb896WVY7fdHq2k=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "signed_tx": "tx_+JALAfhCuEDENdMoxhXSuZG6NNeE7bozUCPlmbo+7CpXqEuftn6HCo+7BfudJWbRL3IyoIsRTgsRz0QRjI1umNtUvZpQijMLuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVGg0h70WQdhD/5RcvbrZYwC2PJdwgQGlSKgCSG/PellWO31ysVN"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDENdMoxhXSuZG6NNeE7bozUCPlmbo+7CpXqEuftn6HCo+7BfudJWbRL3IyoIsRTgsRz0QRjI1umNtUvZpQijMLuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVGg0h70WQdhD/5RcvbrZYwC2PJdwgQGlSKgCSG/PellWO31ysVN",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "signed_tx": "tx_+NILAfiEuEDENdMoxhXSuZG6NNeE7bozUCPlmbo+7CpXqEuftn6HCo+7BfudJWbRL3IyoIsRTgsRz0QRjI1umNtUvZpQijMLuED8qWBNjOB9mbT47qXusr7E5H+VJPc8KsIAUMqPOy4MK/Y4tNEi0ToL4wC0Q94H0ylcs45dmeAhxGsf0KKI0lUMuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVGg0h70WQdhD/5RcvbrZYwC2PJdwgQGlSKgCSG/PellWO1moFZ1"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEDENdMoxhXSuZG6NNeE7bozUCPlmbo+7CpXqEuftn6HCo+7BfudJWbRL3IyoIsRTgsRz0QRjI1umNtUvZpQijMLuED8qWBNjOB9mbT47qXusr7E5H+VJPc8KsIAUMqPOy4MK/Y4tNEi0ToL4wC0Q94H0ylcs45dmeAhxGsf0KKI0lUMuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVGg0h70WQdhD/5RcvbrZYwC2PJdwgQGlSKgCSG/PellWO1moFZ1"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEDENdMoxhXSuZG6NNeE7bozUCPlmbo+7CpXqEuftn6HCo+7BfudJWbRL3IyoIsRTgsRz0QRjI1umNtUvZpQijMLuED8qWBNjOB9mbT47qXusr7E5H+VJPc8KsIAUMqPOy4MK/Y4tNEi0ToL4wC0Q94H0ylcs45dmeAhxGsf0KKI0lUMuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVGg0h70WQdhD/5RcvbrZYwC2PJdwgQGlSKgCSG/PellWO1moFZ1"
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": 81
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 81
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 81,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": 81
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 81
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 81,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "pubkey": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421773,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
      "owner_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg"
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
    "pubkey": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421772,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
      "owner_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg"
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
      "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421771,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "balance": 69999999999969
    },
    {
      "account": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
      "ak_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421770,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
        "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
        "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 82,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
        "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
        "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
      }
    }
  },
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
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
    "block_hash": "kh_A1AsgQ2io8RraGaL9A5bLkUAX6bGjdkqyhxQa1YkWaP2cZFYv",
    "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RUqC7kXprWW3UMzt2gKWctBqJBJFLlkd94C7xrIMGSJcHSNvHJxs=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "signed_tx": "tx_+JALAfhCuECBNgpEB57YjmwQJnIvpx0j97k8oH4kJVa2XNkEU4U+y1ShNJjZFiMLqkc7rkka8gDl+SaZ5zmbupnTYiHIwDoLuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVKgu5F6a1lt1DM7doClnLQaiQSRS5ZHfeAu8ayDBkiXB0iPxu/E"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuECBNgpEB57YjmwQJnIvpx0j97k8oH4kJVa2XNkEU4U+y1ShNJjZFiMLqkc7rkka8gDl+SaZ5zmbupnTYiHIwDoLuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVKgu5F6a1lt1DM7doClnLQaiQSRS5ZHfeAu8ayDBkiXB0iPxu/E",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoAiGaVYh4wZh+LT5/kUWyTJWhKQzqjn8AQBJcxsv1h+49Qsisg==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "signed_tx": "tx_+NILAfiEuEBjXsNETkxDmBnxn5csU4c9XqFhibpWEWt1Rw8GLBriGNi21bVRxIY+NMh9QRP8sOk/4SANYhvAAAEnegueId0JuECBNgpEB57YjmwQJnIvpx0j97k8oH4kJVa2XNkEU4U+y1ShNJjZFiMLqkc7rkka8gDl+SaZ5zmbupnTYiHIwDoLuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVKgu5F6a1lt1DM7doClnLQaiQSRS5ZHfeAu8ayDBkiXB0gCShPy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBjXsNETkxDmBnxn5csU4c9XqFhibpWEWt1Rw8GLBriGNi21bVRxIY+NMh9QRP8sOk/4SANYhvAAAEnegueId0JuECBNgpEB57YjmwQJnIvpx0j97k8oH4kJVa2XNkEU4U+y1ShNJjZFiMLqkc7rkka8gDl+SaZ5zmbupnTYiHIwDoLuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVKgu5F6a1lt1DM7doClnLQaiQSRS5ZHfeAu8ayDBkiXB0gCShPy"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBjXsNETkxDmBnxn5csU4c9XqFhibpWEWt1Rw8GLBriGNi21bVRxIY+NMh9QRP8sOk/4SANYhvAAAEnegueId0JuECBNgpEB57YjmwQJnIvpx0j97k8oH4kJVa2XNkEU4U+y1ShNJjZFiMLqkc7rkka8gDl+SaZ5zmbupnTYiHIwDoLuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVKgu5F6a1lt1DM7doClnLQaiQSRS5ZHfeAu8ayDBkiXB0gCShPy"
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": 82
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 82
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 82,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
    "round": 82
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 82
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 82,
      "contract_id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
    "pubkey": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421767,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
      "owner_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg"
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
    "pubkey": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421766,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
      "owner_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg"
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
      "ak_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421765,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
      "ak_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421764,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2fXYtJecE72PbiWmWFRk7D78y9uVAogzKYavx53BXFUXKbTXxV",
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
      "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421763,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "balance": 69999999999979
    },
    {
      "account": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
      "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421762,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "balance": 69999999999979
    },
    {
      "account": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RU6AdUDo1JdmxDX8bhN0Cqt1Bx8C7dhPAZL6+R3C/Afn2mTi0znw=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
          "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "signed_tx": "tx_+JALAfhCuEAK3QqOJJ1Z+8jSAFstpxLTRBkHKQ4HR/ggFJO8LV9loHt75Agb4XRn3u6CSSt5lb5Jx9Nc+3qLYNXgg8MbLjsKuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVOgHVA6NSXZsQ1/G4TdAqrdQcfAu3YTwGS+vkdwvwH59pmc53/b"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAK3QqOJJ1Z+8jSAFstpxLTRBkHKQ4HR/ggFJO8LV9loHt75Agb4XRn3u6CSSt5lb5Jx9Nc+3qLYNXgg8MbLjsKuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVOgHVA6NSXZsQ1/G4TdAqrdQcfAu3YTwGS+vkdwvwH59pmc53/b",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
          "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "signed_tx": "tx_+NILAfiEuEAK3QqOJJ1Z+8jSAFstpxLTRBkHKQ4HR/ggFJO8LV9loHt75Agb4XRn3u6CSSt5lb5Jx9Nc+3qLYNXgg8MbLjsKuECdeWplQO29uNY0PLtydmu+gp2CahtLStZdRLloXvsuDx3dlXCn/ffCVg+LzIgWpYPR8MPshy/qFG8+8IcZ81UDuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVOgHVA6NSXZsQ1/G4TdAqrdQcfAu3YTwGS+vkdwvwH59pmMqjmd"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAK3QqOJJ1Z+8jSAFstpxLTRBkHKQ4HR/ggFJO8LV9loHt75Agb4XRn3u6CSSt5lb5Jx9Nc+3qLYNXgg8MbLjsKuECdeWplQO29uNY0PLtydmu+gp2CahtLStZdRLloXvsuDx3dlXCn/ffCVg+LzIgWpYPR8MPshy/qFG8+8IcZ81UDuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVOgHVA6NSXZsQ1/G4TdAqrdQcfAu3YTwGS+vkdwvwH59pmMqjmd"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAK3QqOJJ1Z+8jSAFstpxLTRBkHKQ4HR/ggFJO8LV9loHt75Agb4XRn3u6CSSt5lb5Jx9Nc+3qLYNXgg8MbLjsKuECdeWplQO29uNY0PLtydmu+gp2CahtLStZdRLloXvsuDx3dlXCn/ffCVg+LzIgWpYPR8MPshy/qFG8+8IcZ81UDuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVOgHVA6NSXZsQ1/G4TdAqrdQcfAu3YTwGS+vkdwvwH59pmMqjmd"
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
    "pubkey": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421759,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
      "owner_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "pubkey": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421758,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
      "owner_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "ABCDEFG",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 84,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "ABCDEFG",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "ABCDEFG",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "ABCDEFG",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RVKBKFm+GTNPh74MsUovttA/6nst0uMjt54GHKrrNapP0Qq2Ek3k=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "signed_tx": "tx_+JALAfhCuED9YStuYwc8Cq9vhH8G48ObLU+Ql+5TwV3h2kvg4WS2p/SMy4hOGWgqiPa1XFVbi+nB2bUjk9+ygCs68AO8iO8DuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVSgShZvhkzT4e+DLFKL7bQP+p7LdLjI7eeBhyq6zWqT9EKFRaGP"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuED9YStuYwc8Cq9vhH8G48ObLU+Ql+5TwV3h2kvg4WS2p/SMy4hOGWgqiPa1XFVbi+nB2bUjk9+ygCs68AO8iO8DuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVSgShZvhkzT4e+DLFKL7bQP+p7LdLjI7eeBhyq6zWqT9EKFRaGP",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "signed_tx": "tx_+NILAfiEuED6Tg1TfIFKH52XrpVFvaosrI87g5v/Uvpp22OBhPK6Yq5tbOqrWRbJFXCkd5L9OPjYz78TLCdlIT5OMtVInD0HuED9YStuYwc8Cq9vhH8G48ObLU+Ql+5TwV3h2kvg4WS2p/SMy4hOGWgqiPa1XFVbi+nB2bUjk9+ygCs68AO8iO8DuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVSgShZvhkzT4e+DLFKL7bQP+p7LdLjI7eeBhyq6zWqT9EK7NVPK"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuED6Tg1TfIFKH52XrpVFvaosrI87g5v/Uvpp22OBhPK6Yq5tbOqrWRbJFXCkd5L9OPjYz78TLCdlIT5OMtVInD0HuED9YStuYwc8Cq9vhH8G48ObLU+Ql+5TwV3h2kvg4WS2p/SMy4hOGWgqiPa1XFVbi+nB2bUjk9+ygCs68AO8iO8DuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVSgShZvhkzT4e+DLFKL7bQP+p7LdLjI7eeBhyq6zWqT9EK7NVPK"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuED6Tg1TfIFKH52XrpVFvaosrI87g5v/Uvpp22OBhPK6Yq5tbOqrWRbJFXCkd5L9OPjYz78TLCdlIT5OMtVInD0HuED9YStuYwc8Cq9vhH8G48ObLU+Ql+5TwV3h2kvg4WS2p/SMy4hOGWgqiPa1XFVbi+nB2bUjk9+ygCs68AO8iO8DuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVSgShZvhkzT4e+DLFKL7bQP+p7LdLjI7eeBhyq6zWqT9EK7NVPK"
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": 84
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 84
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 84,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": 84
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 84
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 84,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "ABCDEFG",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 85,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "ABCDEFG",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "ABCDEFG",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "ABCDEFG",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RVaBBUDecoPR9tVb27gFIBz99D7hsOfsbRtzelRFTxbrO1FtKPos=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "signed_tx": "tx_+JALAfhCuEBZg4YCxCWPoO5uvIIkqz1teAo8lh3Rih+lkZN8604f9eWEbECRpArUB3ySuSpU6WAeBzy81oBPeDkWzVYO8GgPuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVWgQVA3nKD0fbVW9u4BSAc/fQ+4bDn7G0bc3pURU8W6ztRG/s+M"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBZg4YCxCWPoO5uvIIkqz1teAo8lh3Rih+lkZN8604f9eWEbECRpArUB3ySuSpU6WAeBzy81oBPeDkWzVYO8GgPuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVWgQVA3nKD0fbVW9u4BSAc/fQ+4bDn7G0bc3pURU8W6ztRG/s+M",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "signed_tx": "tx_+NILAfiEuEBOlPzL+jd1pSjUbscju0Bd6l1MyakDlSF90pt0gYk+L4sR9CLl6cPulRR9KSGoE23omBZpQm5Oei58cki+HtkGuEBZg4YCxCWPoO5uvIIkqz1teAo8lh3Rih+lkZN8604f9eWEbECRpArUB3ySuSpU6WAeBzy81oBPeDkWzVYO8GgPuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVWgQVA3nKD0fbVW9u4BSAc/fQ+4bDn7G0bc3pURU8W6ztRUlxJC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBOlPzL+jd1pSjUbscju0Bd6l1MyakDlSF90pt0gYk+L4sR9CLl6cPulRR9KSGoE23omBZpQm5Oei58cki+HtkGuEBZg4YCxCWPoO5uvIIkqz1teAo8lh3Rih+lkZN8604f9eWEbECRpArUB3ySuSpU6WAeBzy81oBPeDkWzVYO8GgPuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVWgQVA3nKD0fbVW9u4BSAc/fQ+4bDn7G0bc3pURU8W6ztRUlxJC"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBOlPzL+jd1pSjUbscju0Bd6l1MyakDlSF90pt0gYk+L4sR9CLl6cPulRR9KSGoE23omBZpQm5Oei58cki+HtkGuEBZg4YCxCWPoO5uvIIkqz1teAo8lh3Rih+lkZN8604f9eWEbECRpArUB3ySuSpU6WAeBzy81oBPeDkWzVYO8GgPuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVWgQVA3nKD0fbVW9u4BSAc/fQ+4bDn7G0bc3pURU8W6ztRUlxJC"
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": 85
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 85
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 85,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": 85
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 85
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 85,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "pubkey": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421753,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
      "owner_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwCs9rhl",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_LwIVSSB3aW6fAKC6C+jkzCIrZVHx82dNrpa0VJC54p2RyDZaBpOD0l3QPiVubywgSSB3aW6fAKAdrAHbSRoMcmZKacfrbfOnJ4yXXSZw0k/Z0DDOe8gh8NUyu2M="
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
    "pubkey": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421752,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
      "owner_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwCs9rhl",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_LwIVSSB3aW6fAKC6C+jkzCIrZVHx82dNrpa0VJC54p2RyDZaBpOD0l3QPiVubywgSSB3aW6fAKAdrAHbSRoMcmZKacfrbfOnJ4yXXSZw0k/Z0DDOe8gh8NUyu2M="
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "ABCDEFG",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 86,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "ABCDEFG",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "ABCDEFG",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "ABCDEFG",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RVqCm1Grr5P0H5VvPUo4XzjS3DE6g4I8sD5fngcAoTTYu/F8pAig=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "signed_tx": "tx_+JALAfhCuECpbTz2tCNSnoU7Q81l4ZRmWMCKWIBSdaNyvrK6X1ySeXdfLL1a7FqSTd44KgRA2IsHV3XhL48iir2KoLSbLG0EuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVagptRq6+T9B+Vbz1KOF840twxOoOCPLA+X54HAKE02LvxxeTsk"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuECpbTz2tCNSnoU7Q81l4ZRmWMCKWIBSdaNyvrK6X1ySeXdfLL1a7FqSTd44KgRA2IsHV3XhL48iir2KoLSbLG0EuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVagptRq6+T9B+Vbz1KOF840twxOoOCPLA+X54HAKE02LvxxeTsk",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "signed_tx": "tx_+NILAfiEuEBXw2IQjCnpFC/rJWsHhvljst5qZ4STtTcjVlBNF6qDrZ1vzBOdhCi4bpTaMmcsAckNAyu3OZCtaE1qNIVqeTULuECpbTz2tCNSnoU7Q81l4ZRmWMCKWIBSdaNyvrK6X1ySeXdfLL1a7FqSTd44KgRA2IsHV3XhL48iir2KoLSbLG0EuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVagptRq6+T9B+Vbz1KOF840twxOoOCPLA+X54HAKE02LvxrZLD9"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBXw2IQjCnpFC/rJWsHhvljst5qZ4STtTcjVlBNF6qDrZ1vzBOdhCi4bpTaMmcsAckNAyu3OZCtaE1qNIVqeTULuECpbTz2tCNSnoU7Q81l4ZRmWMCKWIBSdaNyvrK6X1ySeXdfLL1a7FqSTd44KgRA2IsHV3XhL48iir2KoLSbLG0EuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVagptRq6+T9B+Vbz1KOF840twxOoOCPLA+X54HAKE02LvxrZLD9"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBXw2IQjCnpFC/rJWsHhvljst5qZ4STtTcjVlBNF6qDrZ1vzBOdhCi4bpTaMmcsAckNAyu3OZCtaE1qNIVqeTULuECpbTz2tCNSnoU7Q81l4ZRmWMCKWIBSdaNyvrK6X1ySeXdfLL1a7FqSTd44KgRA2IsHV3XhL48iir2KoLSbLG0EuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVagptRq6+T9B+Vbz1KOF840twxOoOCPLA+X54HAKE02LvxrZLD9"
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": 86
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 86
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 86,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": 86
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 86
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 86,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "ABCDEFG",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 87,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "ABCDEFG",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "ABCDEFG",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "ABCDEFG",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RV6AIO7fyNS55OVGjEjP9GZRxYBumrlGuqGUAGL+LaSQzuuYa61E=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "signed_tx": "tx_+JALAfhCuECKFMSVIoJTU3EInBXVe0Qg1nkSt4NkjymJoFluImnpuuvbFvfyMafxfhXTMQZNxGgIe6/HY8M2MjlQE3upinAOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVegCDu38jUueTlRoxIz/RmUcWAbpq5RrqhlABi/i2kkM7o/c76W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuECKFMSVIoJTU3EInBXVe0Qg1nkSt4NkjymJoFluImnpuuvbFvfyMafxfhXTMQZNxGgIe6/HY8M2MjlQE3upinAOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVegCDu38jUueTlRoxIz/RmUcWAbpq5RrqhlABi/i2kkM7o/c76W",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "signed_tx": "tx_+NILAfiEuEARaaPxXdWfNtwMXiLzbh0T6SxHg4vK6LWc1UTcTkC1N14Gfhe6uomWZLrzfo5iGS9qAKqcy22zePLaHrgcZiwHuECKFMSVIoJTU3EInBXVe0Qg1nkSt4NkjymJoFluImnpuuvbFvfyMafxfhXTMQZNxGgIe6/HY8M2MjlQE3upinAOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVegCDu38jUueTlRoxIz/RmUcWAbpq5RrqhlABi/i2kkM7r2d/td"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEARaaPxXdWfNtwMXiLzbh0T6SxHg4vK6LWc1UTcTkC1N14Gfhe6uomWZLrzfo5iGS9qAKqcy22zePLaHrgcZiwHuECKFMSVIoJTU3EInBXVe0Qg1nkSt4NkjymJoFluImnpuuvbFvfyMafxfhXTMQZNxGgIe6/HY8M2MjlQE3upinAOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVegCDu38jUueTlRoxIz/RmUcWAbpq5RrqhlABi/i2kkM7r2d/td"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEARaaPxXdWfNtwMXiLzbh0T6SxHg4vK6LWc1UTcTkC1N14Gfhe6uomWZLrzfo5iGS9qAKqcy22zePLaHrgcZiwHuECKFMSVIoJTU3EInBXVe0Qg1nkSt4NkjymJoFluImnpuuvbFvfyMafxfhXTMQZNxGgIe6/HY8M2MjlQE3upinAOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVegCDu38jUueTlRoxIz/RmUcWAbpq5RrqhlABi/i2kkM7r2d/td"
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": 87
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 87
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 87,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": 87
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 87
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 87,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "ABCDEFG",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 88,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "ABCDEFG",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "ABCDEFG",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
        "call_data": "ABCDEFG",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
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
    "block_hash": "kh_tzaZc4HPXnoQojpHp1JvJhV1KqqDzAy4NarBq5F5sN3YEZPi",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RWKCi+SMJGEb05phX9XKWw9aPOfpWkoH2KKEXcjXoPQQF2wtfFl4=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "signed_tx": "tx_+JALAfhCuEApK1/x+bdHRzNkamSOaLiIvx4bthsjVI20aO7ldpw3Ma+lxoAiyBdmjTH1lCFSZnHvObwuRxKz6owu9spfavAAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVigovkjCRhG9OaYV/VylsPWjzn6VpKB9iihF3I16D0EBdvGAiOG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEApK1/x+bdHRzNkamSOaLiIvx4bthsjVI20aO7ldpw3Ma+lxoAiyBdmjTH1lCFSZnHvObwuRxKz6owu9spfavAAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVigovkjCRhG9OaYV/VylsPWjzn6VpKB9iihF3I16D0EBdvGAiOG",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "signed_tx": "tx_+NILAfiEuEApK1/x+bdHRzNkamSOaLiIvx4bthsjVI20aO7ldpw3Ma+lxoAiyBdmjTH1lCFSZnHvObwuRxKz6owu9spfavAAuEBQwmM0ND9TG6owBfIdloXNCncQ5aHVmpJVM+qF/20WuWFJXN54IXx5nj3WUeONc6xAX+tPoJuQlv52g78h6XIKuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVigovkjCRhG9OaYV/VylsPWjzn6VpKB9iihF3I16D0EBdsMkmDi"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEApK1/x+bdHRzNkamSOaLiIvx4bthsjVI20aO7ldpw3Ma+lxoAiyBdmjTH1lCFSZnHvObwuRxKz6owu9spfavAAuEBQwmM0ND9TG6owBfIdloXNCncQ5aHVmpJVM+qF/20WuWFJXN54IXx5nj3WUeONc6xAX+tPoJuQlv52g78h6XIKuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVigovkjCRhG9OaYV/VylsPWjzn6VpKB9iihF3I16D0EBdsMkmDi"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEApK1/x+bdHRzNkamSOaLiIvx4bthsjVI20aO7ldpw3Ma+lxoAiyBdmjTH1lCFSZnHvObwuRxKz6owu9spfavAAuEBQwmM0ND9TG6owBfIdloXNCncQ5aHVmpJVM+qF/20WuWFJXN54IXx5nj3WUeONc6xAX+tPoJuQlv52g78h6XIKuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVigovkjCRhG9OaYV/VylsPWjzn6VpKB9iihF3I16D0EBdsMkmDi"
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": 88
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 88
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 88,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": 88
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 88
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 88,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
        "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
        "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
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
    "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
    "call_data": "ABCDEFG",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 89,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
        "call_data": "ABCDEFG",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
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
    "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
        "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
        "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
    "call_data": "ABCDEFG",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
        "call_data": "ABCDEFG",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
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
    "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RWaAPz9raLBJL2eg/zyl3gldUtxjD3nmfW/5YadnQG1KnmetJT+s=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "signed_tx": "tx_+JALAfhCuECpAWgEeIDg/kNLDdVX96qA8g+Al2r+W6AfcMEc62wu0U8vcnyzfW4xPgctpS5R9KcccJLnGEyZ/eL0YINo5vkPuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVmgD8/a2iwSS9noP88pd4JXVLcYw955n1v+WGnZ0BtSp5kpto6d"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuECpAWgEeIDg/kNLDdVX96qA8g+Al2r+W6AfcMEc62wu0U8vcnyzfW4xPgctpS5R9KcccJLnGEyZ/eL0YINo5vkPuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVmgD8/a2iwSS9noP88pd4JXVLcYw955n1v+WGnZ0BtSp5kpto6d",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "signed_tx": "tx_+NILAfiEuEBJI7OUlQ2q2Is0y3ghny7G1ScLrqFPLvrRc1GJnJ9ri7Esnw/XYyFX5UKG7+6PSiPmOfUxSBvE3wfRs12Q16YKuECpAWgEeIDg/kNLDdVX96qA8g+Al2r+W6AfcMEc62wu0U8vcnyzfW4xPgctpS5R9KcccJLnGEyZ/eL0YINo5vkPuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVmgD8/a2iwSS9noP88pd4JXVLcYw955n1v+WGnZ0BtSp5k6daky"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBJI7OUlQ2q2Is0y3ghny7G1ScLrqFPLvrRc1GJnJ9ri7Esnw/XYyFX5UKG7+6PSiPmOfUxSBvE3wfRs12Q16YKuECpAWgEeIDg/kNLDdVX96qA8g+Al2r+W6AfcMEc62wu0U8vcnyzfW4xPgctpS5R9KcccJLnGEyZ/eL0YINo5vkPuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVmgD8/a2iwSS9noP88pd4JXVLcYw955n1v+WGnZ0BtSp5k6daky"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBJI7OUlQ2q2Is0y3ghny7G1ScLrqFPLvrRc1GJnJ9ri7Esnw/XYyFX5UKG7+6PSiPmOfUxSBvE3wfRs12Q16YKuECpAWgEeIDg/kNLDdVX96qA8g+Al2r+W6AfcMEc62wu0U8vcnyzfW4xPgctpS5R9KcccJLnGEyZ/eL0YINo5vkPuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVmgD8/a2iwSS9noP88pd4JXVLcYw955n1v+WGnZ0BtSp5k6daky"
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": 89
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 89
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 89,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": 89
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 89
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 89,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
        "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
        "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
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
    "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
    "call_data": "ABCDEFG",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 90,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
        "call_data": "ABCDEFG",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
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
    "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
        "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
        "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
    "call_data": "ABCDEFG",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
        "call_data": "ABCDEFG",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
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
    "block_hash": "kh_2Yw1qjfhcqT8EjyP6Ln2zCdZa4hatW4GrxF5yvNEyr1TciKK9n",
    "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RWqDELCo0tMr31fqRLbzaySSwa1v9zIeosHHYQCDoJyinUpmSBR4=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "signed_tx": "tx_+JALAfhCuEDWF4czD259wReoyfPYBCuvCRpJnldE+1rCmhrIlMhRpzrbJfc17aCRJScf8MDL6dfzLNPSLzJ4MzReAWFr2qUFuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVqgxCwqNLTK99X6kS282skksGtb/cyHqLBx2EAg6Ccop1IiMYv3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDWF4czD259wReoyfPYBCuvCRpJnldE+1rCmhrIlMhRpzrbJfc17aCRJScf8MDL6dfzLNPSLzJ4MzReAWFr2qUFuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVqgxCwqNLTK99X6kS282skksGtb/cyHqLBx2EAg6Ccop1IiMYv3",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoKy78PqBXWOiNCAIZ7UC1B94b/K0+OHEgjYycrm6KJzAX9QWrw==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "signed_tx": "tx_+NILAfiEuEBmMQ3S4UBESIcsKow9kH2YWxpLReH6+79waAhtzZiYLjyGe5fB7RUXloMrYSurTEWAT3qIT9fgBCrH1y0VhZYKuEDWF4czD259wReoyfPYBCuvCRpJnldE+1rCmhrIlMhRpzrbJfc17aCRJScf8MDL6dfzLNPSLzJ4MzReAWFr2qUFuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVqgxCwqNLTK99X6kS282skksGtb/cyHqLBx2EAg6Ccop1ImmDB+"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBmMQ3S4UBESIcsKow9kH2YWxpLReH6+79waAhtzZiYLjyGe5fB7RUXloMrYSurTEWAT3qIT9fgBCrH1y0VhZYKuEDWF4czD259wReoyfPYBCuvCRpJnldE+1rCmhrIlMhRpzrbJfc17aCRJScf8MDL6dfzLNPSLzJ4MzReAWFr2qUFuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVqgxCwqNLTK99X6kS282skksGtb/cyHqLBx2EAg6Ccop1ImmDB+"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBmMQ3S4UBESIcsKow9kH2YWxpLReH6+79waAhtzZiYLjyGe5fB7RUXloMrYSurTEWAT3qIT9fgBCrH1y0VhZYKuEDWF4czD259wReoyfPYBCuvCRpJnldE+1rCmhrIlMhRpzrbJfc17aCRJScf8MDL6dfzLNPSLzJ4MzReAWFr2qUFuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVqgxCwqNLTK99X6kS282skksGtb/cyHqLBx2EAg6Ccop1ImmDB+"
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": 90
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 90
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 90,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": 90
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 90
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 90,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "pubkey": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421741,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
      "owner_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg"
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
    "pubkey": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421740,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
      "owner_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg"
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
      "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421739,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "balance": 39999999999971
    },
    {
      "account": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
        "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
        "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "ABCDEFG",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 91,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
        "call_data": "ABCDEFG",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
        "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
        "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "ABCDEFG",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
        "call_data": "ABCDEFG",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RW6A6VGMV0UeJZhA+sUZvVcuuWoukktvaPuXWsTQkF3jgWJZ6zhg=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "signed_tx": "tx_+JALAfhCuEAJTEmxKxQ+cvDpURaq/Ry+x7kLUMyuXgh5fi2HhrRxX/zmwwKqwKcmllcOR+RFnuNKv8ZnjEdnOMO53PRJsv4AuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVugOlRjFdFHiWYQPrFGb1XLrlqLpJLb2j7l1rE0JBd44FiXFOMu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAJTEmxKxQ+cvDpURaq/Ry+x7kLUMyuXgh5fi2HhrRxX/zmwwKqwKcmllcOR+RFnuNKv8ZnjEdnOMO53PRJsv4AuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVugOlRjFdFHiWYQPrFGb1XLrlqLpJLb2j7l1rE0JBd44FiXFOMu",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "signed_tx": "tx_+NILAfiEuEAJTEmxKxQ+cvDpURaq/Ry+x7kLUMyuXgh5fi2HhrRxX/zmwwKqwKcmllcOR+RFnuNKv8ZnjEdnOMO53PRJsv4AuECz/7ZDLz+38a+HJse+tcjtPoCxujJhMFQekRhT4neiBzfIFfq5Gukz/FP7M08UBhbra3mbJXUc+ehw4D9V3GAHuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVugOlRjFdFHiWYQPrFGb1XLrlqLpJLb2j7l1rE0JBd44FgzHZyb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAJTEmxKxQ+cvDpURaq/Ry+x7kLUMyuXgh5fi2HhrRxX/zmwwKqwKcmllcOR+RFnuNKv8ZnjEdnOMO53PRJsv4AuECz/7ZDLz+38a+HJse+tcjtPoCxujJhMFQekRhT4neiBzfIFfq5Gukz/FP7M08UBhbra3mbJXUc+ehw4D9V3GAHuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVugOlRjFdFHiWYQPrFGb1XLrlqLpJLb2j7l1rE0JBd44FgzHZyb"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAJTEmxKxQ+cvDpURaq/Ry+x7kLUMyuXgh5fi2HhrRxX/zmwwKqwKcmllcOR+RFnuNKv8ZnjEdnOMO53PRJsv4AuECz/7ZDLz+38a+HJse+tcjtPoCxujJhMFQekRhT4neiBzfIFfq5Gukz/FP7M08UBhbra3mbJXUc+ehw4D9V3GAHuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVugOlRjFdFHiWYQPrFGb1XLrlqLpJLb2j7l1rE0JBd44FgzHZyb"
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": 91
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 91
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 91,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": 91
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 91
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 91,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "pubkey": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421736,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
      "owner_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg"
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
    "pubkey": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421735,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
      "owner_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg"
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
      "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421734,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "balance": 39999999999971
    },
    {
      "account": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "ABCDEFG",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 92,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
        "call_data": "ABCDEFG",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "ABCDEFG",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
        "call_data": "ABCDEFG",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RXKBuEyEv1rsGAsGCJFIBsoQYLop0yeB/rD+44CbigaEZ15KKRqQ=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "signed_tx": "tx_+JALAfhCuEAI52Yg4IKh6PWq7A4ypEkcguCzzZyI1cNyv6WtoVgWNkI12WGGd6pXqQsNMjkTcclFb048s7YIr/4GRW2q3yYDuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVygbhMhL9a7BgLBgiRSAbKEGC6KdMngf6w/uOAm4oGhGdfKjRCF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAI52Yg4IKh6PWq7A4ypEkcguCzzZyI1cNyv6WtoVgWNkI12WGGd6pXqQsNMjkTcclFb048s7YIr/4GRW2q3yYDuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVygbhMhL9a7BgLBgiRSAbKEGC6KdMngf6w/uOAm4oGhGdfKjRCF",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "signed_tx": "tx_+NILAfiEuEAI52Yg4IKh6PWq7A4ypEkcguCzzZyI1cNyv6WtoVgWNkI12WGGd6pXqQsNMjkTcclFb048s7YIr/4GRW2q3yYDuEDO1Vg0G52VGuxL66PNw1d2RJKFGmDT0UZLlGd1lqZ1BLFSwYZArcLL++qCClkKW4wQEudNCrl8kYVn/59YRIgAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVygbhMhL9a7BgLBgiRSAbKEGC6KdMngf6w/uOAm4oGhGdfIUlLK"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAI52Yg4IKh6PWq7A4ypEkcguCzzZyI1cNyv6WtoVgWNkI12WGGd6pXqQsNMjkTcclFb048s7YIr/4GRW2q3yYDuEDO1Vg0G52VGuxL66PNw1d2RJKFGmDT0UZLlGd1lqZ1BLFSwYZArcLL++qCClkKW4wQEudNCrl8kYVn/59YRIgAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVygbhMhL9a7BgLBgiRSAbKEGC6KdMngf6w/uOAm4oGhGdfIUlLK"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAI52Yg4IKh6PWq7A4ypEkcguCzzZyI1cNyv6WtoVgWNkI12WGGd6pXqQsNMjkTcclFb048s7YIr/4GRW2q3yYDuEDO1Vg0G52VGuxL66PNw1d2RJKFGmDT0UZLlGd1lqZ1BLFSwYZArcLL++qCClkKW4wQEudNCrl8kYVn/59YRIgAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEVygbhMhL9a7BgLBgiRSAbKEGC6KdMngf6w/uOAm4oGhGdfIUlLK"
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": 92
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 92
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 92,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": 92
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 92
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 92,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "pubkey": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421731,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
      "owner_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG"
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
    "pubkey": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421730,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
      "owner_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG"
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
      "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421729,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "balance": 39999999999971
    },
    {
      "account": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
      "ak_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421728,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
        "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
        "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "ABCDEFG",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 93,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
        "call_data": "ABCDEFG",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
        "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
        "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "ABCDEFG",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
        "call_data": "ABCDEFG",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
      }
    }
  },
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
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
    "block_hash": "kh_BmHgQSHxqcsJv28ouRKiHt2ENdRiEMQpG4o274qvtKSsEfVjE",
    "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RXaCaehPI24Z2FqdCRj8cKUDtsLLeyo2Rs1nleGxELXUFeC+UJSM=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "signed_tx": "tx_+JALAfhCuEAchI0f6F9sfZY6JbIVrV23j35jZhqakxR9rXCQFHa0g0B4AXgYdrEPVVAyW1ao+qRn06DhKuRz0KNK6+vHkAoPuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEV2gmnoTyNuGdhanQkY/HClA7bCy3sqNkbNZ5XhsRC11BXhd/eMN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAchI0f6F9sfZY6JbIVrV23j35jZhqakxR9rXCQFHa0g0B4AXgYdrEPVVAyW1ao+qRn06DhKuRz0KNK6+vHkAoPuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEV2gmnoTyNuGdhanQkY/HClA7bCy3sqNkbNZ5XhsRC11BXhd/eMN",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoMt5zrTP/uFj7HQMhC/VlSn2m1UW46SU00ztri8srekrXX8j5A==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "signed_tx": "tx_+NILAfiEuEAchI0f6F9sfZY6JbIVrV23j35jZhqakxR9rXCQFHa0g0B4AXgYdrEPVVAyW1ao+qRn06DhKuRz0KNK6+vHkAoPuEBE/9YFs4QIPQCVddoOtZnfe4e517bUOd2py6cL338u8Qptj8PpRbNujd7G/m477BvW0JhuwFeV0eFkgoiu9ZgCuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEV2gmnoTyNuGdhanQkY/HClA7bCy3sqNkbNZ5XhsRC11BXiwtjQ8"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAchI0f6F9sfZY6JbIVrV23j35jZhqakxR9rXCQFHa0g0B4AXgYdrEPVVAyW1ao+qRn06DhKuRz0KNK6+vHkAoPuEBE/9YFs4QIPQCVddoOtZnfe4e517bUOd2py6cL338u8Qptj8PpRbNujd7G/m477BvW0JhuwFeV0eFkgoiu9ZgCuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEV2gmnoTyNuGdhanQkY/HClA7bCy3sqNkbNZ5XhsRC11BXiwtjQ8"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAchI0f6F9sfZY6JbIVrV23j35jZhqakxR9rXCQFHa0g0B4AXgYdrEPVVAyW1ao+qRn06DhKuRz0KNK6+vHkAoPuEBE/9YFs4QIPQCVddoOtZnfe4e517bUOd2py6cL338u8Qptj8PpRbNujd7G/m477BvW0JhuwFeV0eFkgoiu9ZgCuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEV2gmnoTyNuGdhanQkY/HClA7bCy3sqNkbNZ5XhsRC11BXiwtjQ8"
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": 93
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 93
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 93,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
    "round": 93
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 93
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 93,
      "contract_id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
    "pubkey": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421725,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
      "owner_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG"
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
    "pubkey": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421724,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
      "owner_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG"
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
      "ak_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421723,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
      "ak_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421722,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_vbVDSPQo6pvofewKEVaDxkbD9973UjXa88h4yB38mZ76zjbSy",
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
      "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421721,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "balance": 39999999999981
    },
    {
      "account": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
      "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421720,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "balance": 39999999999981
    },
    {
      "account": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RXqAQK1t32akVn+wPVVJc7EVp5xPQpZ3ZC/z2CB+cw1GJV0CEDEo=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
          "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "signed_tx": "tx_+JALAfhCuED/zBskzD2VJnbz2XWJ50iA5ghQUXLJ/OH34LJflWAtMKFJdk4PDkCAjKG7PrDSXaBYIvZm4jVDCSY2i0W7CoEMuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEV6gECtbd9mpFZ/sD1VSXOxFaecT0KWd2Qv89ggfnMNRiVd1n/gb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuED/zBskzD2VJnbz2XWJ50iA5ghQUXLJ/OH34LJflWAtMKFJdk4PDkCAjKG7PrDSXaBYIvZm4jVDCSY2i0W7CoEMuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEV6gECtbd9mpFZ/sD1VSXOxFaecT0KWd2Qv89ggfnMNRiVd1n/gb",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
          "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "signed_tx": "tx_+NILAfiEuED4q9sm77r1SOgKSOrL9VWW59NsHPzh75yaTWyD+V8+7L5nCdaCF6sRnchjYvA0Q80vMUhVh3+MeZDQ/MwHvlgKuED/zBskzD2VJnbz2XWJ50iA5ghQUXLJ/OH34LJflWAtMKFJdk4PDkCAjKG7PrDSXaBYIvZm4jVDCSY2i0W7CoEMuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEV6gECtbd9mpFZ/sD1VSXOxFaecT0KWd2Qv89ggfnMNRiVf/xRh3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuED4q9sm77r1SOgKSOrL9VWW59NsHPzh75yaTWyD+V8+7L5nCdaCF6sRnchjYvA0Q80vMUhVh3+MeZDQ/MwHvlgKuED/zBskzD2VJnbz2XWJ50iA5ghQUXLJ/OH34LJflWAtMKFJdk4PDkCAjKG7PrDSXaBYIvZm4jVDCSY2i0W7CoEMuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEV6gECtbd9mpFZ/sD1VSXOxFaecT0KWd2Qv89ggfnMNRiVf/xRh3"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuED4q9sm77r1SOgKSOrL9VWW59NsHPzh75yaTWyD+V8+7L5nCdaCF6sRnchjYvA0Q80vMUhVh3+MeZDQ/MwHvlgKuED/zBskzD2VJnbz2XWJ50iA5ghQUXLJ/OH34LJflWAtMKFJdk4PDkCAjKG7PrDSXaBYIvZm4jVDCSY2i0W7CoEMuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEV6gECtbd9mpFZ/sD1VSXOxFaecT0KWd2Qv89ggfnMNRiVf/xRh3"
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
    "pubkey": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421717,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
      "owner_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "pubkey": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421716,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
      "owner_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 95,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RX6CMgqJd8nRapqUUbUw9v6wtj6hgLbCY77CjZ+5ZSZuulLi8qtA=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "signed_tx": "tx_+JALAfhCuEB3LOUltrXQBaj3z/UxUHTgo/zZVsb80UugztPsKqR9A4XpmDJvdevc/cbyvCr+Z21xRwNqK0cFssGo6UWC/JwPuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEV+gjIKiXfJ0WqalFG1MPb+sLY+oYC2wmO+wo2fuWUmbrpS+8Xtl"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB3LOUltrXQBaj3z/UxUHTgo/zZVsb80UugztPsKqR9A4XpmDJvdevc/cbyvCr+Z21xRwNqK0cFssGo6UWC/JwPuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEV+gjIKiXfJ0WqalFG1MPb+sLY+oYC2wmO+wo2fuWUmbrpS+8Xtl",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "signed_tx": "tx_+NILAfiEuEB3LOUltrXQBaj3z/UxUHTgo/zZVsb80UugztPsKqR9A4XpmDJvdevc/cbyvCr+Z21xRwNqK0cFssGo6UWC/JwPuEDFxKTY2jnhZLnYUm3Jo93RMgFVOYlkxH2FJfhg92zN7sQHoaGBj5rfh4GvNxnVS+hg9hIO7lxOOdt3JgsLNskNuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEV+gjIKiXfJ0WqalFG1MPb+sLY+oYC2wmO+wo2fuWUmbrpRPqFeu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEB3LOUltrXQBaj3z/UxUHTgo/zZVsb80UugztPsKqR9A4XpmDJvdevc/cbyvCr+Z21xRwNqK0cFssGo6UWC/JwPuEDFxKTY2jnhZLnYUm3Jo93RMgFVOYlkxH2FJfhg92zN7sQHoaGBj5rfh4GvNxnVS+hg9hIO7lxOOdt3JgsLNskNuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEV+gjIKiXfJ0WqalFG1MPb+sLY+oYC2wmO+wo2fuWUmbrpRPqFeu"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEB3LOUltrXQBaj3z/UxUHTgo/zZVsb80UugztPsKqR9A4XpmDJvdevc/cbyvCr+Z21xRwNqK0cFssGo6UWC/JwPuEDFxKTY2jnhZLnYUm3Jo93RMgFVOYlkxH2FJfhg92zN7sQHoaGBj5rfh4GvNxnVS+hg9hIO7lxOOdt3JgsLNskNuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEV+gjIKiXfJ0WqalFG1MPb+sLY+oYC2wmO+wo2fuWUmbrpRPqFeu"
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": 95
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 95
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 95,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": 95
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 95
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 95,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 96,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RYKAjpDoIf1xt6DzHHuwolkEakFSolyZXrsJG6sOj8xVjWdadELs=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "signed_tx": "tx_+JALAfhCuEBobP7rn5QzIZDURMXPBlxgWCxW4UI8cP8YRir5adOWAdeIVH7J3X+jOznPeO/mI6Dj0wkHwHfk9f0g3ruteI8PuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWCgI6Q6CH9cbeg8xx7sKJZBGpBUqJcmV67CRurDo/MVY1nVwJoh"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBobP7rn5QzIZDURMXPBlxgWCxW4UI8cP8YRir5adOWAdeIVH7J3X+jOznPeO/mI6Dj0wkHwHfk9f0g3ruteI8PuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWCgI6Q6CH9cbeg8xx7sKJZBGpBUqJcmV67CRurDo/MVY1nVwJoh",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "signed_tx": "tx_+NILAfiEuEBobP7rn5QzIZDURMXPBlxgWCxW4UI8cP8YRir5adOWAdeIVH7J3X+jOznPeO/mI6Dj0wkHwHfk9f0g3ruteI8PuECug/88FuAkOwJMYI2otm9VQDs4yNtkTww98nmOEoiYN2RiwXA9qK2WAFebH/n+5OBe4bs9t15Wn7zX2q7wN2sKuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWCgI6Q6CH9cbeg8xx7sKJZBGpBUqJcmV67CRurDo/MVY1nWrc8b"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBobP7rn5QzIZDURMXPBlxgWCxW4UI8cP8YRir5adOWAdeIVH7J3X+jOznPeO/mI6Dj0wkHwHfk9f0g3ruteI8PuECug/88FuAkOwJMYI2otm9VQDs4yNtkTww98nmOEoiYN2RiwXA9qK2WAFebH/n+5OBe4bs9t15Wn7zX2q7wN2sKuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWCgI6Q6CH9cbeg8xx7sKJZBGpBUqJcmV67CRurDo/MVY1nWrc8b"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBobP7rn5QzIZDURMXPBlxgWCxW4UI8cP8YRir5adOWAdeIVH7J3X+jOznPeO/mI6Dj0wkHwHfk9f0g3ruteI8PuECug/88FuAkOwJMYI2otm9VQDs4yNtkTww98nmOEoiYN2RiwXA9qK2WAFebH/n+5OBe4bs9t15Wn7zX2q7wN2sKuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWCgI6Q6CH9cbeg8xx7sKJZBGpBUqJcmV67CRurDo/MVY1nWrc8b"
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": 96
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 96
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 96,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": 96
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 96
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 96,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "pubkey": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421711,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
      "owner_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwCs9rhl",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_LwIVSSB3aW6fAKC6C+jkzCIrZVHx82dNrpa0VJC54p2RyDZaBpOD0l3QPiVubywgSSB3aW6fAKAdrAHbSRoMcmZKacfrbfOnJ4yXXSZw0k/Z0DDOe8gh8NUyu2M="
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
    "pubkey": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421710,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
      "owner_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwCs9rhl",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_LwIVSSB3aW6fAKC6C+jkzCIrZVHx82dNrpa0VJC54p2RyDZaBpOD0l3QPiVubywgSSB3aW6fAKAdrAHbSRoMcmZKacfrbfOnJ4yXXSZw0k/Z0DDOe8gh8NUyu2M="
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 97,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RYaDKjBGmkbBWLoW3Brc7CSb5/MXhOI9cAuw1v5+q4urVtQS/QSE=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "signed_tx": "tx_+JALAfhCuECpD3rjx7tPWZj6vUy5P2tfYV4Whyb/8B8XuQ6p6bzwDZEhgp6Fr8z0v80/V1zHRw/5ILlWknBzNjIdv+dHVCUEuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWGgyowRppGwVi6Ftwa3Owkm+fzF4TiPXALsNb+fquLq1bUye6Xm"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuECpD3rjx7tPWZj6vUy5P2tfYV4Whyb/8B8XuQ6p6bzwDZEhgp6Fr8z0v80/V1zHRw/5ILlWknBzNjIdv+dHVCUEuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWGgyowRppGwVi6Ftwa3Owkm+fzF4TiPXALsNb+fquLq1bUye6Xm",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "signed_tx": "tx_+NILAfiEuEBsX0UUD9Xl011MvHNp6Hm6aGdLlWQnY+CMa/PgTI5FHWAr/REjeDR/2KoYxd+ZH0y8qk1OdPizkExfkq1wOp8CuECpD3rjx7tPWZj6vUy5P2tfYV4Whyb/8B8XuQ6p6bzwDZEhgp6Fr8z0v80/V1zHRw/5ILlWknBzNjIdv+dHVCUEuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWGgyowRppGwVi6Ftwa3Owkm+fzF4TiPXALsNb+fquLq1bWgQjkU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBsX0UUD9Xl011MvHNp6Hm6aGdLlWQnY+CMa/PgTI5FHWAr/REjeDR/2KoYxd+ZH0y8qk1OdPizkExfkq1wOp8CuECpD3rjx7tPWZj6vUy5P2tfYV4Whyb/8B8XuQ6p6bzwDZEhgp6Fr8z0v80/V1zHRw/5ILlWknBzNjIdv+dHVCUEuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWGgyowRppGwVi6Ftwa3Owkm+fzF4TiPXALsNb+fquLq1bWgQjkU"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBsX0UUD9Xl011MvHNp6Hm6aGdLlWQnY+CMa/PgTI5FHWAr/REjeDR/2KoYxd+ZH0y8qk1OdPizkExfkq1wOp8CuECpD3rjx7tPWZj6vUy5P2tfYV4Whyb/8B8XuQ6p6bzwDZEhgp6Fr8z0v80/V1zHRw/5ILlWknBzNjIdv+dHVCUEuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWGgyowRppGwVi6Ftwa3Owkm+fzF4TiPXALsNb+fquLq1bWgQjkU"
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": 97
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 97
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 97,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": 97
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 97
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 97,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 98,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RYqBZRe3migV7U3ovP/jbmi6Vi5EQvq/bmVvdUudPMvsfbgKWlWg=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "signed_tx": "tx_+JALAfhCuEBaXDnvhuzimWEEhODJh5R2VIAvggOR/YNPr4Ra1UZh4it6o/9M6pSy6Pii6vs/RjFrssYczMhdxs8AWA2J88kAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWKgWUXt5ooFe1N6Lz/425oulYuREL6v25lb3VLnTzL7H24L4Srn"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBaXDnvhuzimWEEhODJh5R2VIAvggOR/YNPr4Ra1UZh4it6o/9M6pSy6Pii6vs/RjFrssYczMhdxs8AWA2J88kAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWKgWUXt5ooFe1N6Lz/425oulYuREL6v25lb3VLnTzL7H24L4Srn",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "signed_tx": "tx_+NILAfiEuEBaXDnvhuzimWEEhODJh5R2VIAvggOR/YNPr4Ra1UZh4it6o/9M6pSy6Pii6vs/RjFrssYczMhdxs8AWA2J88kAuEDs+aQiflkdscbl7VRCGXdmfh72hD5mQn7O5W+ZBiH1Xe4e12GjwTtcy/RP6HdUydcEjzueqyGoaQozl9FP684IuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWKgWUXt5ooFe1N6Lz/425oulYuREL6v25lb3VLnTzL7H26gavFR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBaXDnvhuzimWEEhODJh5R2VIAvggOR/YNPr4Ra1UZh4it6o/9M6pSy6Pii6vs/RjFrssYczMhdxs8AWA2J88kAuEDs+aQiflkdscbl7VRCGXdmfh72hD5mQn7O5W+ZBiH1Xe4e12GjwTtcy/RP6HdUydcEjzueqyGoaQozl9FP684IuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWKgWUXt5ooFe1N6Lz/425oulYuREL6v25lb3VLnTzL7H26gavFR"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBaXDnvhuzimWEEhODJh5R2VIAvggOR/YNPr4Ra1UZh4it6o/9M6pSy6Pii6vs/RjFrssYczMhdxs8AWA2J88kAuEDs+aQiflkdscbl7VRCGXdmfh72hD5mQn7O5W+ZBiH1Xe4e12GjwTtcy/RP6HdUydcEjzueqyGoaQozl9FP684IuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWKgWUXt5ooFe1N6Lz/425oulYuREL6v25lb3VLnTzL7H26gavFR"
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": 98
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 98
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 98,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": 98
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 98
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 98,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 99,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
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
    "block_hash": "kh_3D8VnKgCDtvDLgZRN5J59o5UXTcmDfxt2Tp66DEGuGZe7YVeP",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RY6D4xaP+ju5pAbR6Nyofc4jkUALYc/WxMigWs5kIH+1tmX1rA6I=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "signed_tx": "tx_+JALAfhCuEBxllkCQ9cZd2gUzuUe3uQ1AywAO+/q827oNwn2Zy7ND/1qaY9yY+tbgdNI26ACJCp8XpefKfc0ErfRG7/gabUBuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWOg+MWj/o7uaQG0ejcqH3OI5FAC2HP1sTIoFrOZCB/tbZl6d5JU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBxllkCQ9cZd2gUzuUe3uQ1AywAO+/q827oNwn2Zy7ND/1qaY9yY+tbgdNI26ACJCp8XpefKfc0ErfRG7/gabUBuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWOg+MWj/o7uaQG0ejcqH3OI5FAC2HP1sTIoFrOZCB/tbZl6d5JU",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "signed_tx": "tx_+NILAfiEuEBTxXvDhdO5ZQsH3to9IvtEdhoRdEa0K3Zkty7DctbLY5YeutnX+s0FsWoCvdhj2CQmRs2vq5eowlzMiYjh5BMIuEBxllkCQ9cZd2gUzuUe3uQ1AywAO+/q827oNwn2Zy7ND/1qaY9yY+tbgdNI26ACJCp8XpefKfc0ErfRG7/gabUBuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWOg+MWj/o7uaQG0ejcqH3OI5FAC2HP1sTIoFrOZCB/tbZk2i8b/"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBTxXvDhdO5ZQsH3to9IvtEdhoRdEa0K3Zkty7DctbLY5YeutnX+s0FsWoCvdhj2CQmRs2vq5eowlzMiYjh5BMIuEBxllkCQ9cZd2gUzuUe3uQ1AywAO+/q827oNwn2Zy7ND/1qaY9yY+tbgdNI26ACJCp8XpefKfc0ErfRG7/gabUBuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWOg+MWj/o7uaQG0ejcqH3OI5FAC2HP1sTIoFrOZCB/tbZk2i8b/"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBTxXvDhdO5ZQsH3to9IvtEdhoRdEa0K3Zkty7DctbLY5YeutnX+s0FsWoCvdhj2CQmRs2vq5eowlzMiYjh5BMIuEBxllkCQ9cZd2gUzuUe3uQ1AywAO+/q827oNwn2Zy7ND/1qaY9yY+tbgdNI26ACJCp8XpefKfc0ErfRG7/gabUBuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWOg+MWj/o7uaQG0ejcqH3OI5FAC2HP1sTIoFrOZCB/tbZk2i8b/"
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": 99
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 99
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 99,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": 99
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 99
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 99,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
        "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
        "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
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
    "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 100,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
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
    "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
        "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
        "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
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
    "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RZKDUqNfiXKc3m2lveNlE7DfWBrKt4fyM1ID2Z82QzPQQw4yoLLs=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "signed_tx": "tx_+JALAfhCuED9TnVuNIHCll8j6aLJonBqYrr8KoOF2368mzbRNv5BB44iBfF8uTo7qvooFNpVqjVN54UP3GDPnWa/DOMV4ycOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWSg1KjX4lynN5tpb3jZROw31gayreH8jNSA9mfNkMz0EMPh7IAe"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuED9TnVuNIHCll8j6aLJonBqYrr8KoOF2368mzbRNv5BB44iBfF8uTo7qvooFNpVqjVN54UP3GDPnWa/DOMV4ycOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWSg1KjX4lynN5tpb3jZROw31gayreH8jNSA9mfNkMz0EMPh7IAe",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "signed_tx": "tx_+NILAfiEuEDBF+HPLAh1hLr7sNQzJK81dEbZV6hsK8k1jYGejSf9q76wGCdZsb3txw9cQKDTKMLtlDzluFk+rI4oyQogvMkPuED9TnVuNIHCll8j6aLJonBqYrr8KoOF2368mzbRNv5BB44iBfF8uTo7qvooFNpVqjVN54UP3GDPnWa/DOMV4ycOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWSg1KjX4lynN5tpb3jZROw31gayreH8jNSA9mfNkMz0EMMq+M3E"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEDBF+HPLAh1hLr7sNQzJK81dEbZV6hsK8k1jYGejSf9q76wGCdZsb3txw9cQKDTKMLtlDzluFk+rI4oyQogvMkPuED9TnVuNIHCll8j6aLJonBqYrr8KoOF2368mzbRNv5BB44iBfF8uTo7qvooFNpVqjVN54UP3GDPnWa/DOMV4ycOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWSg1KjX4lynN5tpb3jZROw31gayreH8jNSA9mfNkMz0EMMq+M3E"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEDBF+HPLAh1hLr7sNQzJK81dEbZV6hsK8k1jYGejSf9q76wGCdZsb3txw9cQKDTKMLtlDzluFk+rI4oyQogvMkPuED9TnVuNIHCll8j6aLJonBqYrr8KoOF2368mzbRNv5BB44iBfF8uTo7qvooFNpVqjVN54UP3GDPnWa/DOMV4ycOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWSg1KjX4lynN5tpb3jZROw31gayreH8jNSA9mfNkMz0EMMq+M3E"
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": 100
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 100
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 100,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": 100
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 100
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 100,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
        "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
        "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
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
    "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 101,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
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
    "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
        "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
        "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
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
    "block_hash": "kh_NSoGzNzUus86jcycP73YoEvM6dz5GQadb3cBc2oMWaedY5y6k",
    "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RZaCQYfjh/SL1At5rK780fwZx77OGEnFS0D9v7pyCtJMx49XIrhg=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "signed_tx": "tx_+JALAfhCuEAfymPci32B7WJdpVCFbm5xQ5m9Vs8Zmz/9NjENvsx3lBcj4xLvTufhpGG/qsMP8sFVpCRQ1v4Ao9W3fYfMcbkMuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWWgkGH44f0i9QLeayu/NH8Gce+zhhJxUtA/b+6cgrSTMeOOY/Kr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAfymPci32B7WJdpVCFbm5xQ5m9Vs8Zmz/9NjENvsx3lBcj4xLvTufhpGG/qsMP8sFVpCRQ1v4Ao9W3fYfMcbkMuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWWgkGH44f0i9QLeayu/NH8Gce+zhhJxUtA/b+6cgrSTMeOOY/Kr",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoNK7Qn1Yff/Fia/qRQbFCm/8lyG69CZt5gxRTB9gUuruKhByEA==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "signed_tx": "tx_+NILAfiEuEAfymPci32B7WJdpVCFbm5xQ5m9Vs8Zmz/9NjENvsx3lBcj4xLvTufhpGG/qsMP8sFVpCRQ1v4Ao9W3fYfMcbkMuEB9Gv3fw95rC3qTtvtaLjiLQ6L9gL/9h/8QlqMRAmhsAjNhgIFyQ8Rdom5JGfx+sYoxlyITuZu6q+u4AQhS3VgCuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWWgkGH44f0i9QLeayu/NH8Gce+zhhJxUtA/b+6cgrSTMeOqfDla"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAfymPci32B7WJdpVCFbm5xQ5m9Vs8Zmz/9NjENvsx3lBcj4xLvTufhpGG/qsMP8sFVpCRQ1v4Ao9W3fYfMcbkMuEB9Gv3fw95rC3qTtvtaLjiLQ6L9gL/9h/8QlqMRAmhsAjNhgIFyQ8Rdom5JGfx+sYoxlyITuZu6q+u4AQhS3VgCuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWWgkGH44f0i9QLeayu/NH8Gce+zhhJxUtA/b+6cgrSTMeOqfDla"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAfymPci32B7WJdpVCFbm5xQ5m9Vs8Zmz/9NjENvsx3lBcj4xLvTufhpGG/qsMP8sFVpCRQ1v4Ao9W3fYfMcbkMuEB9Gv3fw95rC3qTtvtaLjiLQ6L9gL/9h/8QlqMRAmhsAjNhgIFyQ8Rdom5JGfx+sYoxlyITuZu6q+u4AQhS3VgCuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWWgkGH44f0i9QLeayu/NH8Gce+zhhJxUtA/b+6cgrSTMeOqfDla"
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": 101
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 101
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 101,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": 101
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 101
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 101,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "pubkey": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421699,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
      "owner_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg"
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
    "pubkey": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421698,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
      "owner_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg"
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
      "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421697,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "balance": 69999999999969
    },
    {
      "account": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
        "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
        "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 102,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
        "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
        "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RZqAwfShJ7b6RAfJS6C0nydpImHVbYch+EnToj/b17xmJ+gLd1B8=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "signed_tx": "tx_+JALAfhCuEDY6ZiYMP/a5kjFyYho2V3BaDUvG1AQJiXETiyiXSZ3cKgTgRLzsg2nIsfYAOmMFTbwEfQcQsMryW9vB7eetMoCuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWagMH0oSe2+kQHyUugtJ8naSJh1W2HIfhJ06I/29e8ZifoItMgW"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDY6ZiYMP/a5kjFyYho2V3BaDUvG1AQJiXETiyiXSZ3cKgTgRLzsg2nIsfYAOmMFTbwEfQcQsMryW9vB7eetMoCuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWagMH0oSe2+kQHyUugtJ8naSJh1W2HIfhJ06I/29e8ZifoItMgW",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "signed_tx": "tx_+NILAfiEuEAti8DMREN8cDSf+R66ThodPGYD2A6ppN7fHKDbqg8x7owthu3oUcqsNramW0Z6mLn2Z0N7A7tyhUvJ3SIxvuQHuEDY6ZiYMP/a5kjFyYho2V3BaDUvG1AQJiXETiyiXSZ3cKgTgRLzsg2nIsfYAOmMFTbwEfQcQsMryW9vB7eetMoCuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWagMH0oSe2+kQHyUugtJ8naSJh1W2HIfhJ06I/29e8ZifpgUrYX"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAti8DMREN8cDSf+R66ThodPGYD2A6ppN7fHKDbqg8x7owthu3oUcqsNramW0Z6mLn2Z0N7A7tyhUvJ3SIxvuQHuEDY6ZiYMP/a5kjFyYho2V3BaDUvG1AQJiXETiyiXSZ3cKgTgRLzsg2nIsfYAOmMFTbwEfQcQsMryW9vB7eetMoCuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWagMH0oSe2+kQHyUugtJ8naSJh1W2HIfhJ06I/29e8ZifpgUrYX"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAti8DMREN8cDSf+R66ThodPGYD2A6ppN7fHKDbqg8x7owthu3oUcqsNramW0Z6mLn2Z0N7A7tyhUvJ3SIxvuQHuEDY6ZiYMP/a5kjFyYho2V3BaDUvG1AQJiXETiyiXSZ3cKgTgRLzsg2nIsfYAOmMFTbwEfQcQsMryW9vB7eetMoCuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWagMH0oSe2+kQHyUugtJ8naSJh1W2HIfhJ06I/29e8ZifpgUrYX"
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": 102
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 102
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 102,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": 102
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 102
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 102,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "pubkey": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421694,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
      "owner_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg"
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
    "pubkey": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421693,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
      "owner_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg"
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
      "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421692,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "balance": 69999999999969
    },
    {
      "account": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 103,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RZ6D/hs6QakHFS3b5Brx2FZ+XrNyxIiJcNO3ePFUBtVlbKQI085I=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "signed_tx": "tx_+JALAfhCuECBWqlAOt8j9DaNebfmN4mbjArlJprjA4HLZPMI/yQDIY1nn9CvQNP7zhTA+9KLg6cJVCLmzN5vABd9pwhCfzcFuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWeg/4bOkGpBxUt2+Qa8dhWfl6zcsSIiXDTt3jxVAbVZWymP7aIo"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuECBWqlAOt8j9DaNebfmN4mbjArlJprjA4HLZPMI/yQDIY1nn9CvQNP7zhTA+9KLg6cJVCLmzN5vABd9pwhCfzcFuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWeg/4bOkGpBxUt2+Qa8dhWfl6zcsSIiXDTt3jxVAbVZWymP7aIo",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "signed_tx": "tx_+NILAfiEuECBWqlAOt8j9DaNebfmN4mbjArlJprjA4HLZPMI/yQDIY1nn9CvQNP7zhTA+9KLg6cJVCLmzN5vABd9pwhCfzcFuECzGcGDnrudHIXb6LcDjKECXdi8a59nKtFmu+7S7C71ejZelBkEQx4jsfPL4WoBkRiPJKs50uxIZrK4u2LAOEIDuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWeg/4bOkGpBxUt2+Qa8dhWfl6zcsSIiXDTt3jxVAbVZWykDfLm0"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuECBWqlAOt8j9DaNebfmN4mbjArlJprjA4HLZPMI/yQDIY1nn9CvQNP7zhTA+9KLg6cJVCLmzN5vABd9pwhCfzcFuECzGcGDnrudHIXb6LcDjKECXdi8a59nKtFmu+7S7C71ejZelBkEQx4jsfPL4WoBkRiPJKs50uxIZrK4u2LAOEIDuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWeg/4bOkGpBxUt2+Qa8dhWfl6zcsSIiXDTt3jxVAbVZWykDfLm0"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuECBWqlAOt8j9DaNebfmN4mbjArlJprjA4HLZPMI/yQDIY1nn9CvQNP7zhTA+9KLg6cJVCLmzN5vABd9pwhCfzcFuECzGcGDnrudHIXb6LcDjKECXdi8a59nKtFmu+7S7C71ejZelBkEQx4jsfPL4WoBkRiPJKs50uxIZrK4u2LAOEIDuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWeg/4bOkGpBxUt2+Qa8dhWfl6zcsSIiXDTt3jxVAbVZWykDfLm0"
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": 103
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 103
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 103,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": 103
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 103
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 103,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "pubkey": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421689,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
      "owner_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg"
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
    "pubkey": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421688,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
      "owner_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg"
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
      "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421687,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "balance": 69999999999969
    },
    {
      "account": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
      "ak_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421686,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
        "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
        "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 104,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
        "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
        "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
      }
    }
  },
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
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
    "block_hash": "kh_2JAbLnwac215zbZsQF8UAQrCUTAme4QLX945eLECKngeA3GjdN",
    "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RaKC+fTRFkMEHA/SRk/MEeH65+x1K9N9K0IzdFfKf2pRrWamTDcA=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "signed_tx": "tx_+JALAfhCuEAAV49Oe0gTXQguJqxrBaQfV3MPZSDy3XbGIgcRLJqjpXbW0Xmr6QdwoTOdQwvBg2FozzeU1SsAdL1MFlT7qt0GuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWigvn00RZDBBwP0kZPzBHh+ufsdSvTfStCM3RXyn9qUa1ndoncx"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAAV49Oe0gTXQguJqxrBaQfV3MPZSDy3XbGIgcRLJqjpXbW0Xmr6QdwoTOdQwvBg2FozzeU1SsAdL1MFlT7qt0GuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWigvn00RZDBBwP0kZPzBHh+ufsdSvTfStCM3RXyn9qUa1ndoncx",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoNr2caI+DnFUN7Raapbpwjz+vqgHzQ2yJA6uWWmLyuepi1F27g==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "signed_tx": "tx_+NILAfiEuEAAV49Oe0gTXQguJqxrBaQfV3MPZSDy3XbGIgcRLJqjpXbW0Xmr6QdwoTOdQwvBg2FozzeU1SsAdL1MFlT7qt0GuEBE/qvDxUgAsQWHXUtnV0sAC8a1yg26uzGyyWmcVyr+QGUi+HDPhGLFHA3nPGhRIrr1NymFwc0q26mvPs84eZoMuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWigvn00RZDBBwP0kZPzBHh+ufsdSvTfStCM3RXyn9qUa1kZTfdu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAAV49Oe0gTXQguJqxrBaQfV3MPZSDy3XbGIgcRLJqjpXbW0Xmr6QdwoTOdQwvBg2FozzeU1SsAdL1MFlT7qt0GuEBE/qvDxUgAsQWHXUtnV0sAC8a1yg26uzGyyWmcVyr+QGUi+HDPhGLFHA3nPGhRIrr1NymFwc0q26mvPs84eZoMuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWigvn00RZDBBwP0kZPzBHh+ufsdSvTfStCM3RXyn9qUa1kZTfdu"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAAV49Oe0gTXQguJqxrBaQfV3MPZSDy3XbGIgcRLJqjpXbW0Xmr6QdwoTOdQwvBg2FozzeU1SsAdL1MFlT7qt0GuEBE/qvDxUgAsQWHXUtnV0sAC8a1yg26uzGyyWmcVyr+QGUi+HDPhGLFHA3nPGhRIrr1NymFwc0q26mvPs84eZoMuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWigvn00RZDBBwP0kZPzBHh+ufsdSvTfStCM3RXyn9qUa1kZTfdu"
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": 104
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 104
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 104,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
    "round": 104
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 104
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 104,
      "contract_id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
    "pubkey": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421683,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
      "owner_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg"
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
    "pubkey": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421682,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
      "owner_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg"
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
      "ak_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421681,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
      "ak_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421680,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2r9kMRB8UUNYAkeXNXnHcfCdJFxfLB7hG7Rxf2PBoVVSFBt62k",
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
      "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421679,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "balance": 69999999999979
    },
    {
      "account": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
      "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421678,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "balance": 69999999999979
    },
    {
      "account": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RaaDBgYCxwTO0AIDzPAH2cpSLz1XrK47keROTRPTqVLbBeoWlbws=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
          "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "signed_tx": "tx_+JALAfhCuECVr/uAvbqB3GWw1FZ5q5YGCGn6TnYI3xI9bfcUuAUCczNZ1ZcYJgFdWQvmbak3KroAgdfZYejA8JHYjnVRwVANuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWmgwYGAscEztACA8zwB9nKUi89V6yuO5HkTk0T06lS2wXrGH3tI"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuECVr/uAvbqB3GWw1FZ5q5YGCGn6TnYI3xI9bfcUuAUCczNZ1ZcYJgFdWQvmbak3KroAgdfZYejA8JHYjnVRwVANuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWmgwYGAscEztACA8zwB9nKUi89V6yuO5HkTk0T06lS2wXrGH3tI",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfK58DoMirXQsDXbFBxRt7f7GlvtMUcE9sVU5YtRrPv9Mo4YqakUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZTFa+pU=",
          "code": "cb_+QGrRgOgydAPNHcR9tkdbjfPDsyu1Gt0YYaFLyAFA326EUBKejXAuQF9uQEs/gPRiEYENwAHbAiCAP5E1kQfADcCRwN3NwAaDoYvABoGggAaBoQCAQM//mSg6VIENwFHBHdrA9iCAHd3AP6eMNZdBDcBRwR3agPaAIIAd3cIPgACBAEDLW5vIHJlc3BvbnNlRjoCAAAaCgaCawPYBgB3dyAIhAcMCAEDSWRpZmZlcmVudCBxdWVzdGlvbhoKCIYvKIYCBwwQDAOvggABAD8PAgwIPgwMDgEDOW5vIHdpbm5pbmcgYmV0RjoODABTAGUCDgEDCW9rKygIAkT8IwACAgIPAgwIPgwMDv7SUVtXBDcBd3caCgCGLxiGAAcMCAwDr4IAAQA/CDwEBlUALRqGhgABAwlvawEDRWJldF9hbHJlYWR5X3Rha2VuKxgAAET8IwACAgIIPAQGuEkvBRED0YhGJXF1ZXJ5X2ZlZRFE1kQfEWluaXQRZKDpUjFnZXRfcXVlc3Rpb24RnjDWXR1yZXNvbHZlEdJRW1clcGxhY2VfYmV0gi8AhTQuMi4wAIz5SOE=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "signed_tx": "tx_+NILAfiEuECVr/uAvbqB3GWw1FZ5q5YGCGn6TnYI3xI9bfcUuAUCczNZ1ZcYJgFdWQvmbak3KroAgdfZYejA8JHYjnVRwVANuEDemjXztjkE2VYdB4HQWdgkYzWL/O52gIxbaXVZ23pK6Vh/1nchmFsGkLvYfnwx32pQqwNUQH0HjQIb9FR2goMLuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWmgwYGAscEztACA8zwB9nKUi89V6yuO5HkTk0T06lS2wXq+zo45"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuECVr/uAvbqB3GWw1FZ5q5YGCGn6TnYI3xI9bfcUuAUCczNZ1ZcYJgFdWQvmbak3KroAgdfZYejA8JHYjnVRwVANuEDemjXztjkE2VYdB4HQWdgkYzWL/O52gIxbaXVZ23pK6Vh/1nchmFsGkLvYfnwx32pQqwNUQH0HjQIb9FR2goMLuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWmgwYGAscEztACA8zwB9nKUi89V6yuO5HkTk0T06lS2wXq+zo45"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuECVr/uAvbqB3GWw1FZ5q5YGCGn6TnYI3xI9bfcUuAUCczNZ1ZcYJgFdWQvmbak3KroAgdfZYejA8JHYjnVRwVANuEDemjXztjkE2VYdB4HQWdgkYzWL/O52gIxbaXVZ23pK6Vh/1nchmFsGkLvYfnwx32pQqwNUQH0HjQIb9FR2goMLuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWmgwYGAscEztACA8zwB9nKUi89V6yuO5HkTk0T06lS2wXq+zo45"
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
    "pubkey": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421675,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
      "owner_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "pubkey": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421674,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
      "owner_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "ABCDEFG",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 106,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "ABCDEFG",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "ABCDEFG",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "ABCDEFG",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RaqAh7sMWhn9bC6B1TqqB8mXu/XotunrPi/hz+Mut64tCx+fIEUU=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "signed_tx": "tx_+JALAfhCuEARexC8UVPOrMu5IaFQvGKFQYhxG5nOcZ60BLO9H89kWUByg++vZD005Sb+/PJcIup5C/NUkutQ9E4Z1bhzJzsDuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWqgIe7DFoZ/WwugdU6qgfJl7v16Lbp6z4v4c/jLreuLQsd+mLES"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEARexC8UVPOrMu5IaFQvGKFQYhxG5nOcZ60BLO9H89kWUByg++vZD005Sb+/PJcIup5C/NUkutQ9E4Z1bhzJzsDuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWqgIe7DFoZ/WwugdU6qgfJl7v16Lbp6z4v4c/jLreuLQsd+mLES",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGxVJIHdpbgYbtuU=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "signed_tx": "tx_+NILAfiEuEARexC8UVPOrMu5IaFQvGKFQYhxG5nOcZ60BLO9H89kWUByg++vZD005Sb+/PJcIup5C/NUkutQ9E4Z1bhzJzsDuEA6BtVskGBXugg69LClKxj27/PRRjC/3AiNpOJ34F1WdEcuIrInOHJu1wuylwwmaI8TwbyLq6rIKs43xddOKrwAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWqgIe7DFoZ/WwugdU6qgfJl7v16Lbp6z4v4c/jLreuLQseBUGW2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEARexC8UVPOrMu5IaFQvGKFQYhxG5nOcZ60BLO9H89kWUByg++vZD005Sb+/PJcIup5C/NUkutQ9E4Z1bhzJzsDuEA6BtVskGBXugg69LClKxj27/PRRjC/3AiNpOJ34F1WdEcuIrInOHJu1wuylwwmaI8TwbyLq6rIKs43xddOKrwAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWqgIe7DFoZ/WwugdU6qgfJl7v16Lbp6z4v4c/jLreuLQseBUGW2"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEARexC8UVPOrMu5IaFQvGKFQYhxG5nOcZ60BLO9H89kWUByg++vZD005Sb+/PJcIup5C/NUkutQ9E4Z1bhzJzsDuEA6BtVskGBXugg69LClKxj27/PRRjC/3AiNpOJ34F1WdEcuIrInOHJu1wuylwwmaI8TwbyLq6rIKs43xddOKrwAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWqgIe7DFoZ/WwugdU6qgfJl7v16Lbp6z4v4c/jLreuLQseBUGW2"
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": 106
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 106
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 106,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": 106
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 106
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 106,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "ABCDEFG",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 107,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "ABCDEFG",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "ABCDEFG",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "ABCDEFG",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8Ra6DVm16XK2QGhvEF7XAZs8HR7rnhHIJEAsmiIX7Z7u29VEghycQ=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "signed_tx": "tx_+JALAfhCuEBXG/NFmMswVhsFjLMhOMtzAOsDlyynLVZJ7fV1r2fnBeIgWIjY3mZJ6lEMqhRNI1mc/rsxSfOHWVBqhh0TxzMIuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWug1ZtelytkBobxBe1wGbPB0e654RyCRALJoiF+2e7tvVR5Uhp4"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBXG/NFmMswVhsFjLMhOMtzAOsDlyynLVZJ7fV1r2fnBeIgWIjY3mZJ6lEMqhRNI1mc/rsxSfOHWVBqhh0TxzMIuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWug1ZtelytkBobxBe1wGbPB0e654RyCRALJoiF+2e7tvVR5Uhp4",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGyVubywgSSB3aW77Ftps",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "signed_tx": "tx_+NILAfiEuEBXG/NFmMswVhsFjLMhOMtzAOsDlyynLVZJ7fV1r2fnBeIgWIjY3mZJ6lEMqhRNI1mc/rsxSfOHWVBqhh0TxzMIuEDXr6lklzgFivgYB/OZiNPYK8ZluJjR4ik6IzfWQw+ubB4fXua5NRFbWnCjeUsU6wZ0r85GX0wYIsebLiK6T9gHuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWug1ZtelytkBobxBe1wGbPB0e654RyCRALJoiF+2e7tvVRhibbd"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBXG/NFmMswVhsFjLMhOMtzAOsDlyynLVZJ7fV1r2fnBeIgWIjY3mZJ6lEMqhRNI1mc/rsxSfOHWVBqhh0TxzMIuEDXr6lklzgFivgYB/OZiNPYK8ZluJjR4ik6IzfWQw+ubB4fXua5NRFbWnCjeUsU6wZ0r85GX0wYIsebLiK6T9gHuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWug1ZtelytkBobxBe1wGbPB0e654RyCRALJoiF+2e7tvVRhibbd"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBXG/NFmMswVhsFjLMhOMtzAOsDlyynLVZJ7fV1r2fnBeIgWIjY3mZJ6lEMqhRNI1mc/rsxSfOHWVBqhh0TxzMIuEDXr6lklzgFivgYB/OZiNPYK8ZluJjR4ik6IzfWQw+ubB4fXua5NRFbWnCjeUsU6wZ0r85GX0wYIsebLiK6T9gHuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWug1ZtelytkBobxBe1wGbPB0e654RyCRALJoiF+2e7tvVRhibbd"
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": 107
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 107
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 107,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": 107
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 107
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 107,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "pubkey": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421669,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
      "owner_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwCs9rhl",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_LwIVSSB3aW6fAKC6C+jkzCIrZVHx82dNrpa0VJC54p2RyDZaBpOD0l3QPiVubywgSSB3aW6fAKAdrAHbSRoMcmZKacfrbfOnJ4yXXSZw0k/Z0DDOe8gh8NUyu2M="
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
    "pubkey": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421668,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
      "owner_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwCs9rhl",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_LwIVSSB3aW6fAKC6C+jkzCIrZVHx82dNrpa0VJC54p2RyDZaBpOD0l3QPiVubywgSSB3aW6fAKAdrAHbSRoMcmZKacfrbfOnJ4yXXSZw0k/Z0DDOe8gh8NUyu2M="
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "ABCDEFG",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 108,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "ABCDEFG",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "ABCDEFG",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "ABCDEFG",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RbKCMNmm4a9IvjAwIZyls/xe1G2Gb6W8/aTrrtY92HzwFXYocvQg=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "signed_tx": "tx_+JALAfhCuEBVXV95yYl4/Y+3LAgtdt6jEFvPYmGg/W3wqLYpbBHbdxQv32bFMkkTeTtGfc56MmgNsXTrhr/LaEQE0SgENzYHuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWygjDZpuGvSL4wMCGcpbP8XtRthm+lvP2k667WPdh88BV06jhM1"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBVXV95yYl4/Y+3LAgtdt6jEFvPYmGg/W3wqLYpbBHbdxQv32bFMkkTeTtGfc56MmgNsXTrhr/LaEQE0SgENzYHuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWygjDZpuGvSL4wMCGcpbP8XtRthm+lvP2k667WPdh88BV06jhM1",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "signed_tx": "tx_+NILAfiEuEBVXV95yYl4/Y+3LAgtdt6jEFvPYmGg/W3wqLYpbBHbdxQv32bFMkkTeTtGfc56MmgNsXTrhr/LaEQE0SgENzYHuEBcTxoMtRVfRvXMufF4uvntVg/isBT/GFGaI2p2RSX70gDVQve1C95T6eeKk+Jqae4LM4DDbHTjUcOD+LsVemYHuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWygjDZpuGvSL4wMCGcpbP8XtRthm+lvP2k667WPdh88BV1gMN6n"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBVXV95yYl4/Y+3LAgtdt6jEFvPYmGg/W3wqLYpbBHbdxQv32bFMkkTeTtGfc56MmgNsXTrhr/LaEQE0SgENzYHuEBcTxoMtRVfRvXMufF4uvntVg/isBT/GFGaI2p2RSX70gDVQve1C95T6eeKk+Jqae4LM4DDbHTjUcOD+LsVemYHuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWygjDZpuGvSL4wMCGcpbP8XtRthm+lvP2k667WPdh88BV1gMN6n"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBVXV95yYl4/Y+3LAgtdt6jEFvPYmGg/W3wqLYpbBHbdxQv32bFMkkTeTtGfc56MmgNsXTrhr/LaEQE0SgENzYHuEBcTxoMtRVfRvXMufF4uvntVg/isBT/GFGaI2p2RSX70gDVQve1C95T6eeKk+Jqae4LM4DDbHTjUcOD+LsVemYHuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEWygjDZpuGvSL4wMCGcpbP8XtRthm+lvP2k667WPdh88BV1gMN6n"
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": 108
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 108
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 108,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": 108
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 108
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 108,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "ABCDEFG",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 109,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "ABCDEFG",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "ABCDEFG",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "ABCDEFG",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RbaB+S8oetESj6S4Y+U296NtJlUVSPDPnK09udfz2xtFpoxsx9dU=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "signed_tx": "tx_+JALAfhCuECzzEl7PVwixY7wJ6NosOV5MtPdHtV3KQTf+ATinC92sScD/5JJAljUGp30X8eY1hlfyK5fcZzxWAho5EAOFaAIuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEW2gfkvKHrREo+kuGPlNvejbSZVFUjwz5ytPbnX89sbRaaPOOJ7t"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuECzzEl7PVwixY7wJ6NosOV5MtPdHtV3KQTf+ATinC92sScD/5JJAljUGp30X8eY1hlfyK5fcZzxWAho5EAOFaAIuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEW2gfkvKHrREo+kuGPlNvejbSZVFUjwz5ytPbnX89sbRaaPOOJ7t",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "signed_tx": "tx_+NILAfiEuEAd9BJy/8IhMW1HbFwyftQvsDyPo/81lKN22m90IhxbDFlarFs1agGP8f7gqJFJetMEiDEVRV1qaIfxWrAkaRICuECzzEl7PVwixY7wJ6NosOV5MtPdHtV3KQTf+ATinC92sScD/5JJAljUGp30X8eY1hlfyK5fcZzxWAho5EAOFaAIuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEW2gfkvKHrREo+kuGPlNvejbSZVFUjwz5ytPbnX89sbRaaP7R8bE"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAd9BJy/8IhMW1HbFwyftQvsDyPo/81lKN22m90IhxbDFlarFs1agGP8f7gqJFJetMEiDEVRV1qaIfxWrAkaRICuECzzEl7PVwixY7wJ6NosOV5MtPdHtV3KQTf+ATinC92sScD/5JJAljUGp30X8eY1hlfyK5fcZzxWAho5EAOFaAIuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEW2gfkvKHrREo+kuGPlNvejbSZVFUjwz5ytPbnX89sbRaaP7R8bE"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAd9BJy/8IhMW1HbFwyftQvsDyPo/81lKN22m90IhxbDFlarFs1agGP8f7gqJFJetMEiDEVRV1qaIfxWrAkaRICuECzzEl7PVwixY7wJ6NosOV5MtPdHtV3KQTf+ATinC92sScD/5JJAljUGp30X8eY1hlfyK5fcZzxWAho5EAOFaAIuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEW2gfkvKHrREo+kuGPlNvejbSZVFUjwz5ytPbnX89sbRaaP7R8bE"
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": 109
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 109
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 109,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": 109
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 109
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 109,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "ABCDEFG",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 110,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "ABCDEFG",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "ABCDEFG",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
        "call_data": "ABCDEFG",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
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
    "block_hash": "kh_rTSMbDzmaf9eTNp93XV91w2t4g2abTivyxun3SCxuWpY6sSg3",
    "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RbqDUDiuzez3Zo+y8Sx+gnCkbQ0RQK3a++2Qf000hy//qRSqnVIc=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "signed_tx": "tx_+JALAfhCuEDWislbaxj7g4xsc+XZdSJgLent7Cv50hyrU3Xxqdz2zL8rtZ69BxKegxXlu8fxr5dEtdxpH/BgZtIdVQjW+MUOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEW6g1A4rs3s92aPsvEsfoJwpG0NEUCt2vvtkH9NNIcv/6kUFJrsJ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDWislbaxj7g4xsc+XZdSJgLent7Cv50hyrU3Xxqdz2zL8rtZ69BxKegxXlu8fxr5dEtdxpH/BgZtIdVQjW+MUOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEW6g1A4rs3s92aPsvEsfoJwpG0NEUCt2vvtkH9NNIcv/6kUFJrsJ",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXGzFJIGNsYWltIHRoaXPxFjTf",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "signed_tx": "tx_+NILAfiEuEDWislbaxj7g4xsc+XZdSJgLent7Cv50hyrU3Xxqdz2zL8rtZ69BxKegxXlu8fxr5dEtdxpH/BgZtIdVQjW+MUOuED0NiDJB2Uo4mmK7I9O/KRBV+CzLx3hXI9Og6DhWLFK2oLMQL6Cn6KbkRsn0htjkJaMx7yKfQwXNTk10Qd6djQGuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEW6g1A4rs3s92aPsvEsfoJwpG0NEUCt2vvtkH9NNIcv/6kUEiXVt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEDWislbaxj7g4xsc+XZdSJgLent7Cv50hyrU3Xxqdz2zL8rtZ69BxKegxXlu8fxr5dEtdxpH/BgZtIdVQjW+MUOuED0NiDJB2Uo4mmK7I9O/KRBV+CzLx3hXI9Og6DhWLFK2oLMQL6Cn6KbkRsn0htjkJaMx7yKfQwXNTk10Qd6djQGuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEW6g1A4rs3s92aPsvEsfoJwpG0NEUCt2vvtkH9NNIcv/6kUEiXVt"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEDWislbaxj7g4xsc+XZdSJgLent7Cv50hyrU3Xxqdz2zL8rtZ69BxKegxXlu8fxr5dEtdxpH/BgZtIdVQjW+MUOuED0NiDJB2Uo4mmK7I9O/KRBV+CzLx3hXI9Og6DhWLFK2oLMQL6Cn6KbkRsn0htjkJaMx7yKfQwXNTk10Qd6djQGuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEW6g1A4rs3s92aPsvEsfoJwpG0NEUCt2vvtkH9NNIcv/6kUEiXVt"
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": 110
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 110
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 110,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": 110
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 110
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 110,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
        "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
        "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
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
    "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
    "call_data": "ABCDEFG",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 111,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
        "call_data": "ABCDEFG",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
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
    "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
        "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
        "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
    "call_data": "ABCDEFG",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
        "call_data": "ABCDEFG",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
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
    "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8Rb6BwuYuUQxDbP2SFkHW4warGyAlaO/45UobvXCeZb2qX/9tf/3o=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "signed_tx": "tx_+JALAfhCuEBr/T9fibSDJYvir2M9gqxdINwtG1yjkBZEORcilDyLWOj3sDSC26mswUcZaWz1orP3QNh7diR2n1Gp7DAS8hMAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEW+gcLmLlEMQ2z9khZB1uMGqxsgJWjv+OVKG71wnmW9ql//TB8EP"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBr/T9fibSDJYvir2M9gqxdINwtG1yjkBZEORcilDyLWOj3sDSC26mswUcZaWz1orP3QNh7diR2n1Gp7DAS8hMAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEW+gcLmLlEMQ2z9khZB1uMGqxsgJWjv+OVKG71wnmW9ql//TB8EP",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "signed_tx": "tx_+NILAfiEuEBB0mvhxbY1Mkm+0I5cFwYhBJ5b8gxntETtSboD6cysKsRlVzB/AxE1NFHEVhSm/3gWw9NUaC9zcoSEiGQRj+8DuEBr/T9fibSDJYvir2M9gqxdINwtG1yjkBZEORcilDyLWOj3sDSC26mswUcZaWz1orP3QNh7diR2n1Gp7DAS8hMAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEW+gcLmLlEMQ2z9khZB1uMGqxsgJWjv+OVKG71wnmW9ql//sXLRS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBB0mvhxbY1Mkm+0I5cFwYhBJ5b8gxntETtSboD6cysKsRlVzB/AxE1NFHEVhSm/3gWw9NUaC9zcoSEiGQRj+8DuEBr/T9fibSDJYvir2M9gqxdINwtG1yjkBZEORcilDyLWOj3sDSC26mswUcZaWz1orP3QNh7diR2n1Gp7DAS8hMAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEW+gcLmLlEMQ2z9khZB1uMGqxsgJWjv+OVKG71wnmW9ql//sXLRS"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBB0mvhxbY1Mkm+0I5cFwYhBJ5b8gxntETtSboD6cysKsRlVzB/AxE1NFHEVhSm/3gWw9NUaC9zcoSEiGQRj+8DuEBr/T9fibSDJYvir2M9gqxdINwtG1yjkBZEORcilDyLWOj3sDSC26mswUcZaWz1orP3QNh7diR2n1Gp7DAS8hMAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEW+gcLmLlEMQ2z9khZB1uMGqxsgJWjv+OVKG71wnmW9ql//sXLRS"
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": 111
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 111
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 111,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": 111
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 111
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 111,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
        "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
        "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
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
    "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
    "call_data": "ABCDEFG",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 112,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
        "call_data": "ABCDEFG",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
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
    "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
        "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
        "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
    "call_data": "ABCDEFG",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
        "call_data": "ABCDEFG",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
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
    "block_hash": "kh_MaKPM4f1ERZ7xWijgWsp8NUYijL1QEs5x3ShipVDho8LpsLeH",
    "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RcKCDFkH2ZYgqhQPNgHqgs0BhdofxuSrDLWxGj/BPDtkFq8ATyik=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "signed_tx": "tx_+JALAfhCuEDkGEM7E9OBHvKxfIY/wFFnJFXj4c1UVerlnDl9I4IhhWW4lRe5z1FLZhN0xzEWBs5T67zvKOCEm8xCGYjwGEIAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXCggxZB9mWIKoUDzYB6oLNAYXaH8bkqwy1sRo/wTw7ZBatlTkdz"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDkGEM7E9OBHvKxfIY/wFFnJFXj4c1UVerlnDl9I4IhhWW4lRe5z1FLZhN0xzEWBs5T67zvKOCEm8xCGYjwGEIAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXCggxZB9mWIKoUDzYB6oLNAYXaH8bkqwy1sRo/wTw7ZBatlTkdz",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoLGfQWXzaLFM/Y1KJ7El3nmz/h2GhOoDIqj8GNYYmAMA30/PDw==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "signed_tx": "tx_+NILAfiEuEBI50H/4H39UZTeYzRK5iOOtu4Usmq0TOU4ksWCIiSOIHeu0G8hJQuXLxz1i2SN4XFRp97Fv7aDGx89f8RAml4LuEDkGEM7E9OBHvKxfIY/wFFnJFXj4c1UVerlnDl9I4IhhWW4lRe5z1FLZhN0xzEWBs5T67zvKOCEm8xCGYjwGEIAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXCggxZB9mWIKoUDzYB6oLNAYXaH8bkqwy1sRo/wTw7ZBasItSD8"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBI50H/4H39UZTeYzRK5iOOtu4Usmq0TOU4ksWCIiSOIHeu0G8hJQuXLxz1i2SN4XFRp97Fv7aDGx89f8RAml4LuEDkGEM7E9OBHvKxfIY/wFFnJFXj4c1UVerlnDl9I4IhhWW4lRe5z1FLZhN0xzEWBs5T67zvKOCEm8xCGYjwGEIAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXCggxZB9mWIKoUDzYB6oLNAYXaH8bkqwy1sRo/wTw7ZBasItSD8"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBI50H/4H39UZTeYzRK5iOOtu4Usmq0TOU4ksWCIiSOIHeu0G8hJQuXLxz1i2SN4XFRp97Fv7aDGx89f8RAml4LuEDkGEM7E9OBHvKxfIY/wFFnJFXj4c1UVerlnDl9I4IhhWW4lRe5z1FLZhN0xzEWBs5T67zvKOCEm8xCGYjwGEIAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXCggxZB9mWIKoUDzYB6oLNAYXaH8bkqwy1sRo/wTw7ZBasItSD8"
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": 112
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 112
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 112,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": 112
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 112
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 112,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "pubkey": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421657,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
      "owner_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg"
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
    "pubkey": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421656,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
      "owner_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg"
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
      "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421655,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "balance": 39999999999971
    },
    {
      "account": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
        "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
        "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "ABCDEFG",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 113,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
        "call_data": "ABCDEFG",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
        "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
        "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "ABCDEFG",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
        "call_data": "ABCDEFG",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RcaBpQz+Q2UkATaNR4zX0ATot53rlhULZc7bIHaXBkqqajK0JTV8=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "signed_tx": "tx_+JALAfhCuECeIpYzT5yBHODo8pqpiMY+KzIX/xQ+Ra5GLr4+KxHPaqFEJ1vXEdjb0KhfHcuHW1ocbNHAsy31LlrPAsJJDcAKuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXGgaUM/kNlJAE2jUeM19AE6Led65YVC2XO2yB2lwZKqmow3ELWO"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuECeIpYzT5yBHODo8pqpiMY+KzIX/xQ+Ra5GLr4+KxHPaqFEJ1vXEdjb0KhfHcuHW1ocbNHAsy31LlrPAsJJDcAKuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXGgaUM/kNlJAE2jUeM19AE6Led65YVC2XO2yB2lwZKqmow3ELWO",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "signed_tx": "tx_+NILAfiEuECeIpYzT5yBHODo8pqpiMY+KzIX/xQ+Ra5GLr4+KxHPaqFEJ1vXEdjb0KhfHcuHW1ocbNHAsy31LlrPAsJJDcAKuEDUUHDDqqN91dZ5WinVS+iVgE01IG+0LbgE6GX4i0WqAiWkmf7vMROTTvsV7aDiLB2f0s9p7oM/s+BRKwiMUg4HuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXGgaUM/kNlJAE2jUeM19AE6Led65YVC2XO2yB2lwZKqmoy6FpuT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuECeIpYzT5yBHODo8pqpiMY+KzIX/xQ+Ra5GLr4+KxHPaqFEJ1vXEdjb0KhfHcuHW1ocbNHAsy31LlrPAsJJDcAKuEDUUHDDqqN91dZ5WinVS+iVgE01IG+0LbgE6GX4i0WqAiWkmf7vMROTTvsV7aDiLB2f0s9p7oM/s+BRKwiMUg4HuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXGgaUM/kNlJAE2jUeM19AE6Led65YVC2XO2yB2lwZKqmoy6FpuT"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuECeIpYzT5yBHODo8pqpiMY+KzIX/xQ+Ra5GLr4+KxHPaqFEJ1vXEdjb0KhfHcuHW1ocbNHAsy31LlrPAsJJDcAKuEDUUHDDqqN91dZ5WinVS+iVgE01IG+0LbgE6GX4i0WqAiWkmf7vMROTTvsV7aDiLB2f0s9p7oM/s+BRKwiMUg4HuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXGgaUM/kNlJAE2jUeM19AE6Led65YVC2XO2yB2lwZKqmoy6FpuT"
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": 113
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 113
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 113,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": 113
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 113
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 113,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "pubkey": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421652,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
      "owner_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg"
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
    "pubkey": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421651,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
      "owner_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwEAOwACBqa58+U=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwBbPD72",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg"
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
      "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421650,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "balance": 39999999999971
    },
    {
      "account": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "ABCDEFG",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 114,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
        "call_data": "ABCDEFG",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
        "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "ABCDEFG",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
        "call_data": "ABCDEFG",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RcqCNcDhboMs/BP9NYLBx2FF08O0nGzF/1YXfV+1MFejYgJLDKUQ=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "signed_tx": "tx_+JALAfhCuECS041d3dpBwSutGH1+kedjLOsjDFGPFnm5d2QE8EXr0iWmtLBw/JpoQmwyVa9rNUc3EFe1OaJpo9aF62HVZGYJuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXKgjXA4W6DLPwT/TWCwcdhRdPDtJxsxf9WF31ftTBXo2IDbg9OQ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuECS041d3dpBwSutGH1+kedjLOsjDFGPFnm5d2QE8EXr0iWmtLBw/JpoQmwyVa9rNUc3EFe1OaJpo9aF62HVZGYJuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXKgjXA4W6DLPwT/TWCwcdhRdPDtJxsxf9WF31ftTBXo2IDbg9OQ",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHSUVtXG11vdGhlciByZWFzb25hYmxlIHRoaW5nebI5PdM=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "signed_tx": "tx_+NILAfiEuEAA2a2LFrAMINL5MmKOtK4/5I+8v6E0Fl3f9H3KmV/SQjvs9tqSKsACC4rtTQqNxqBjIRbAZzcPjLCffYthCE4HuECS041d3dpBwSutGH1+kedjLOsjDFGPFnm5d2QE8EXr0iWmtLBw/JpoQmwyVa9rNUc3EFe1OaJpo9aF62HVZGYJuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXKgjXA4W6DLPwT/TWCwcdhRdPDtJxsxf9WF31ftTBXo2IBkkcio"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAA2a2LFrAMINL5MmKOtK4/5I+8v6E0Fl3f9H3KmV/SQjvs9tqSKsACC4rtTQqNxqBjIRbAZzcPjLCffYthCE4HuECS041d3dpBwSutGH1+kedjLOsjDFGPFnm5d2QE8EXr0iWmtLBw/JpoQmwyVa9rNUc3EFe1OaJpo9aF62HVZGYJuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXKgjXA4W6DLPwT/TWCwcdhRdPDtJxsxf9WF31ftTBXo2IBkkcio"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAA2a2LFrAMINL5MmKOtK4/5I+8v6E0Fl3f9H3KmV/SQjvs9tqSKsACC4rtTQqNxqBjIRbAZzcPjLCffYthCE4HuECS041d3dpBwSutGH1+kedjLOsjDFGPFnm5d2QE8EXr0iWmtLBw/JpoQmwyVa9rNUc3EFe1OaJpo9aF62HVZGYJuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXKgjXA4W6DLPwT/TWCwcdhRdPDtJxsxf9WF31ftTBXo2IBkkcio"
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": 114
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 114
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 114,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": 114
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 114
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 114,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "pubkey": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421647,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
      "owner_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG"
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
    "pubkey": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421646,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
      "owner_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG"
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
      "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421645,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "balance": 39999999999971
    },
    {
      "account": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
      "ak_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421644,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
        "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
        "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "ABCDEFG",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 115,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
        "call_data": "ABCDEFG",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
        "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
        "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "ABCDEFG",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
        "call_data": "ABCDEFG",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
      }
    }
  },
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
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
    "block_hash": "kh_sUNNgTpqJtfHZwjHyGYvF5Bao7vBHSowwuqiHkkao7LbSGkFf",
    "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8Rc6CrmGjltphEiqyAutlzhVcZd0As7wJ0n+jWkxIoPBN1VEtEcUk=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "signed_tx": "tx_+JALAfhCuEA1bT2b6MVmt/SQKIsw0XEEmAH+vsXeXCClIeae5oi3NCQOi7GbwraH6qISi4LlXV3dRf3NWKfbi1ytUmcO7LQPuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXOgq5ho5baYRIqsgLrZc4VXGXdALO8CdJ/o1pMSKDwTdVT6Qo6y"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA1bT2b6MVmt/SQKIsw0XEEmAH+vsXeXCClIeae5oi3NCQOi7GbwraH6qISi4LlXV3dRf3NWKfbi1ytUmcO7LQPuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXOgq5ho5baYRIqsgLrZc4VXGXdALO8CdJ/o1pMSKDwTdVT6Qo6y",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxGeMNZdG58EoIGvY4F+NicHh6Eb3AQTsuBR4JcvVFYZt4mD83h/NDJXiqOhxw==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "signed_tx": "tx_+NILAfiEuEA1bT2b6MVmt/SQKIsw0XEEmAH+vsXeXCClIeae5oi3NCQOi7GbwraH6qISi4LlXV3dRf3NWKfbi1ytUmcO7LQPuEB7SxoczY2npHV8o3d5N47tCDCk78GIzxO8mhBaa6SNe9U8GxFgXWvtCl3VfjmQap5nskda6UqHAsDczcxRmSACuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXOgq5ho5baYRIqsgLrZc4VXGXdALO8CdJ/o1pMSKDwTdVTt7DIb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEA1bT2b6MVmt/SQKIsw0XEEmAH+vsXeXCClIeae5oi3NCQOi7GbwraH6qISi4LlXV3dRf3NWKfbi1ytUmcO7LQPuEB7SxoczY2npHV8o3d5N47tCDCk78GIzxO8mhBaa6SNe9U8GxFgXWvtCl3VfjmQap5nskda6UqHAsDczcxRmSACuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXOgq5ho5baYRIqsgLrZc4VXGXdALO8CdJ/o1pMSKDwTdVTt7DIb"
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEA1bT2b6MVmt/SQKIsw0XEEmAH+vsXeXCClIeae5oi3NCQOi7GbwraH6qISi4LlXV3dRf3NWKfbi1ytUmcO7LQPuEB7SxoczY2npHV8o3d5N47tCDCk78GIzxO8mhBaa6SNe9U8GxFgXWvtCl3VfjmQap5nskda6UqHAsDczcxRmSACuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXOgq5ho5baYRIqsgLrZc4VXGXdALO8CdJ/o1pMSKDwTdVTt7DIb"
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": 115
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 115
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 115,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
    "round": 115
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 115
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 115,
      "contract_id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
    "pubkey": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421641,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
      "owner_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG"
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
    "pubkey": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421640,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 3,
      "active": true,
      "deposit": 10,
      "id": "ct_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
      "owner_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "referrer_ids": [],
      "vm_version": 7
    },
    "contract_state": {
      "ck_AABAf+tK": "cv_LwECOwACCMSftN4=",
      "ck_AAEYQB5m": "cv_nwOgyKtdCwNdsUHFG3t/saW+0xRwT2xVTli1Gs+/0yjhipomvrB3",
      "ck_AAL+Smjk": "cv_kUZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZbnfZ+Y=",
      "ck_AAOaYZmv": "cv_vwGhNUIy",
      "ck_AQAAAAAVSSB3aW588SoT": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAAAabyOw": "cv_ABQG4Fg=",
      "ck_AQAAAAAlbm8sIEkgd2luivWw/A==": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG",
      "ck_AQAAAAAxSSBjbGFpbSB0aGlzJRqesg==": "cv_nwCgugvo5MwiK2VR8fNnTa6WtFSQueKdkcg2WgaTg9Jd0D6PdFUg",
      "ck_AQAAAABdb3RoZXIgcmVhc29uYWJsZSB0aGluZ3kLge7V": "cv_nwCgHawB20kaDHJmSmnH623zpyeMl10mcNJP2dAwznvIIfASjdGG"
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
      "ak_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421639,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
      "ak_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421638,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_EHib4KMBrAJvx95toxf22Xm6F8Beku5JxnAGN2SvPhp12uVk3",
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
      "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421637,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "balance": 39999999999981
    },
    {
      "account": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
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
      "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421636,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "balance": 39999999999981
    },
    {
      "account": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "balance": 69999999999979
    }
  ],
  "version": 1
}
```
