
#### initiator ---> node
```javascript
{
  "action": "deposit",
  "payload": {
    "amount": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_a_number",
    "request": {
      "method": "channels.deposit",
      "params": {
        "amount": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "deposit",
  "payload": {
    "amount": 2
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+HIzAaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgWhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAgCGEjCc5UAAoIGnTOuUnVM9QThcVqCCAFeJ51D7a6A4ldyhd3nuKg7lAglKqnZP",
    "updates": [
      {
        "amount": 2,
        "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "op": "OffChainDeposit"
      }
    ]
  },
  "tag": "deposit_tx",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "deposit_tx",
  "payload": {
    "tx": "tx_+LwLAfhCuEBpdn6/h5FeyYL9/JMO3XqEDdmaxrtsqamG4XJJAUNoQI0DtzQVkGHWC4lia9rcsNa9vdBj0a5o8S7fGE3I8Z0FuHT4cjMBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACggadM65SdUz1BOFxWoIIAV4nnUPtroDiV3KF3ee4qDuUCCYBI8r0="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "deposit_created"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+HIzAaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgWhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAgCGEjCc5UAAoIGnTOuUnVM9QThcVqCCAFeJ51D7a6A4ldyhd3nuKg7lAglKqnZP",
    "updates": [
      {
        "amount": 2,
        "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "op": "OffChainDeposit"
      }
    ]
  },
  "tag": "deposit_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "deposit_ack",
  "payload": {
    "tx": "tx_+LwLAfhCuEBa3V9ZXezm+ya0GQGg7RBpS6DbYhiE10oRgSuHpn0JFsdcUz0f2Ldsi1I62JxkLmDAqhxIgYUeya0PP1M4PXsOuHT4cjMBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACggadM65SdUz1BOFxWoIIAV4nnUPtroDiV3KF3ee4qDuUCCXv07Q4="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P4LAfiEuEBa3V9ZXezm+ya0GQGg7RBpS6DbYhiE10oRgSuHpn0JFsdcUz0f2Ldsi1I62JxkLmDAqhxIgYUeya0PP1M4PXsOuEBpdn6/h5FeyYL9/JMO3XqEDdmaxrtsqamG4XJJAUNoQI0DtzQVkGHWC4lia9rcsNa9vdBj0a5o8S7fGE3I8Z0FuHT4cjMBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACggadM65SdUz1BOFxWoIIAV4nnUPtroDiV3KF3ee4qDuUCCZiFbkw="
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P4LAfiEuEBa3V9ZXezm+ya0GQGg7RBpS6DbYhiE10oRgSuHpn0JFsdcUz0f2Ldsi1I62JxkLmDAqhxIgYUeya0PP1M4PXsOuEBpdn6/h5FeyYL9/JMO3XqEDdmaxrtsqamG4XJJAUNoQI0DtzQVkGHWC4lia9rcsNa9vdBj0a5o8S7fGE3I8Z0FuHT4cjMBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACggadM65SdUz1BOFxWoIIAV4nnUPtroDiV3KF3ee4qDuUCCZiFbkw="
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "own_deposit_locked"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "own_deposit_locked"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "deposit_locked"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "deposit_locked"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+P4LAfiEuEBa3V9ZXezm+ya0GQGg7RBpS6DbYhiE10oRgSuHpn0JFsdcUz0f2Ldsi1I62JxkLmDAqhxIgYUeya0PP1M4PXsOuEBpdn6/h5FeyYL9/JMO3XqEDdmaxrtsqamG4XJJAUNoQI0DtzQVkGHWC4lia9rcsNa9vdBj0a5o8S7fGE3I8Z0FuHT4cjMBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACggadM65SdUz1BOFxWoIIAV4nnUPtroDiV3KF3ee4qDuUCCZiFbkw="
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+P4LAfiEuEBa3V9ZXezm+ya0GQGg7RBpS6DbYhiE10oRgSuHpn0JFsdcUz0f2Ldsi1I62JxkLmDAqhxIgYUeya0PP1M4PXsOuEBpdn6/h5FeyYL9/JMO3XqEDdmaxrtsqamG4XJJAUNoQI0DtzQVkGHWC4lia9rcsNa9vdBj0a5o8S7fGE3I8Z0FuHT4cjMBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACggadM65SdUz1BOFxWoIIAV4nnUPtroDiV3KF3ee4qDuUCCZiFbkw="
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "deposit",
  "payload": {
    "amount": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_a_number",
    "request": {
      "method": "channels.deposit",
      "params": {
        "amount": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "deposit",
  "payload": {
    "amount": 2
  }
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+HIzAaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgWhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAgCGEjCc5UAAoHr2z45LVPg+SpWirnkAuHaxyvaxLNwH9YdfnLXjR9N4AwKOScGk",
    "updates": [
      {
        "amount": 2,
        "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "op": "OffChainDeposit"
      }
    ]
  },
  "tag": "deposit_tx",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "deposit_tx",
  "payload": {
    "tx": "tx_+LwLAfhCuEDP8+O7kUlIo+SdURU2HWcGrCfmangbQTdFs8b19FLIDjD+FIaUDJz1lLtpEborLTCP/W35kUtswXXpRd16GT0EuHT4cjMBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgevbPjktU+D5KlaKueQC4drHK9rEs3Af1h1+cteNH03gDAiu/81Q="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "deposit_created"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+HIzAaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgWhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAgCGEjCc5UAAoHr2z45LVPg+SpWirnkAuHaxyvaxLNwH9YdfnLXjR9N4AwKOScGk",
    "updates": [
      {
        "amount": 2,
        "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "op": "OffChainDeposit"
      }
    ]
  },
  "tag": "deposit_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "deposit_ack",
  "payload": {
    "tx": "tx_+LwLAfhCuECxGYZSmO+NcY9yW7+djhTdL5SIz7EfcQkIapFebz/Ky9hx9PGlYOPQXRigXt0/9Zd9OhupORgU740/rf/thrYEuHT4cjMBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgevbPjktU+D5KlaKueQC4drHK9rEs3Af1h1+cteNH03gDAnGGvnw="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P4LAfiEuECxGYZSmO+NcY9yW7+djhTdL5SIz7EfcQkIapFebz/Ky9hx9PGlYOPQXRigXt0/9Zd9OhupORgU740/rf/thrYEuEDP8+O7kUlIo+SdURU2HWcGrCfmangbQTdFs8b19FLIDjD+FIaUDJz1lLtpEborLTCP/W35kUtswXXpRd16GT0EuHT4cjMBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgevbPjktU+D5KlaKueQC4drHK9rEs3Af1h1+cteNH03gDAgtkH4Y="
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P4LAfiEuECxGYZSmO+NcY9yW7+djhTdL5SIz7EfcQkIapFebz/Ky9hx9PGlYOPQXRigXt0/9Zd9OhupORgU740/rf/thrYEuEDP8+O7kUlIo+SdURU2HWcGrCfmangbQTdFs8b19FLIDjD+FIaUDJz1lLtpEborLTCP/W35kUtswXXpRd16GT0EuHT4cjMBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgevbPjktU+D5KlaKueQC4drHK9rEs3Af1h1+cteNH03gDAgtkH4Y="
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "own_deposit_locked"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "own_deposit_locked"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "deposit_locked"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "deposit_locked"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+P4LAfiEuECxGYZSmO+NcY9yW7+djhTdL5SIz7EfcQkIapFebz/Ky9hx9PGlYOPQXRigXt0/9Zd9OhupORgU740/rf/thrYEuEDP8+O7kUlIo+SdURU2HWcGrCfmangbQTdFs8b19FLIDjD+FIaUDJz1lLtpEborLTCP/W35kUtswXXpRd16GT0EuHT4cjMBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgevbPjktU+D5KlaKueQC4drHK9rEs3Af1h1+cteNH03gDAgtkH4Y="
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+P4LAfiEuECxGYZSmO+NcY9yW7+djhTdL5SIz7EfcQkIapFebz/Ky9hx9PGlYOPQXRigXt0/9Zd9OhupORgU740/rf/thrYEuEDP8+O7kUlIo+SdURU2HWcGrCfmangbQTdFs8b19FLIDjD+FIaUDJz1lLtpEborLTCP/W35kUtswXXpRd16GT0EuHT4cjMBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgevbPjktU+D5KlaKueQC4drHK9rEs3Af1h1+cteNH03gDAgtkH4Y="
  },
  "version": 1
}
```
