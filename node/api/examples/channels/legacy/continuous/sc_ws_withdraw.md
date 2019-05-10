
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
  "action": "withdraw",
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
    "tx": "tx_+HI0AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgWhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAgCGEjCc5UAAoEUfp6Gv3gLYNHIy08ITGVY9Xv7I69D5Yu0FUzyRePtuBAqOT2uR",
    "updates": [
      {
        "amount": 2,
        "op": "OffChainWithdrawal",
        "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
      }
    ]
  },
  "tag": "withdraw_tx",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "withdraw_tx",
  "payload": {
    "tx": "tx_+LwLAfhCuECmn6QR8/VwIvc9avwtzuauqSn0NmmDZxYud6Oik+Q0pp6Lev/oK++PdEvZciumZpUbBdlfl3LIqHxc31+43NINuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACgRR+noa/eAtg0cjLTwhMZVj1e/sjr0Pli7QVTPJF4+24ECi9pymI="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "withdraw_created"
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
    "tx": "tx_+HI0AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgWhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAgCGEjCc5UAAoEUfp6Gv3gLYNHIy08ITGVY9Xv7I69D5Yu0FUzyRePtuBAqOT2uR",
    "updates": [
      {
        "amount": 2,
        "op": "OffChainWithdrawal",
        "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
      }
    ]
  },
  "tag": "withdraw_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "withdraw_ack",
  "payload": {
    "tx": "tx_+LwLAfhCuEBWNxnIoMVbGTp+NkKKg8NlXbgVe7PbdpiTBsq0qGD3gwDE4waZEjmlWUJKVi3VxHbmdhdKdZ1lFKkVtBfMM3YEuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACgRR+noa/eAtg0cjLTwhMZVj1e/sjr0Pli7QVTPJF4+24ECjOLPuM="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P4LAfiEuEBWNxnIoMVbGTp+NkKKg8NlXbgVe7PbdpiTBsq0qGD3gwDE4waZEjmlWUJKVi3VxHbmdhdKdZ1lFKkVtBfMM3YEuECmn6QR8/VwIvc9avwtzuauqSn0NmmDZxYud6Oik+Q0pp6Lev/oK++PdEvZciumZpUbBdlfl3LIqHxc31+43NINuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACgRR+noa/eAtg0cjLTwhMZVj1e/sjr0Pli7QVTPJF4+24EChZDmcY="
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
    "tx": "tx_+P4LAfiEuEBWNxnIoMVbGTp+NkKKg8NlXbgVe7PbdpiTBsq0qGD3gwDE4waZEjmlWUJKVi3VxHbmdhdKdZ1lFKkVtBfMM3YEuECmn6QR8/VwIvc9avwtzuauqSn0NmmDZxYud6Oik+Q0pp6Lev/oK++PdEvZciumZpUbBdlfl3LIqHxc31+43NINuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACgRR+noa/eAtg0cjLTwhMZVj1e/sjr0Pli7QVTPJF4+24EChZDmcY="
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
    "event": "own_withdraw_locked"
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
    "event": "own_withdraw_locked"
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
    "event": "withdraw_locked"
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
    "event": "withdraw_locked"
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
    "state": "tx_+P4LAfiEuEBWNxnIoMVbGTp+NkKKg8NlXbgVe7PbdpiTBsq0qGD3gwDE4waZEjmlWUJKVi3VxHbmdhdKdZ1lFKkVtBfMM3YEuECmn6QR8/VwIvc9avwtzuauqSn0NmmDZxYud6Oik+Q0pp6Lev/oK++PdEvZciumZpUbBdlfl3LIqHxc31+43NINuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACgRR+noa/eAtg0cjLTwhMZVj1e/sjr0Pli7QVTPJF4+24EChZDmcY="
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
    "state": "tx_+P4LAfiEuEBWNxnIoMVbGTp+NkKKg8NlXbgVe7PbdpiTBsq0qGD3gwDE4waZEjmlWUJKVi3VxHbmdhdKdZ1lFKkVtBfMM3YEuECmn6QR8/VwIvc9avwtzuauqSn0NmmDZxYud6Oik+Q0pp6Lev/oK++PdEvZciumZpUbBdlfl3LIqHxc31+43NINuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACgRR+noa/eAtg0cjLTwhMZVj1e/sjr0Pli7QVTPJF4+24EChZDmcY="
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
  "action": "withdraw",
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
    "tx": "tx_+HI0AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgWhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAgCGEjCc5UAAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/BQOc0hNO",
    "updates": [
      {
        "amount": 2,
        "op": "OffChainWithdrawal",
        "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
      }
    ]
  },
  "tag": "withdraw_tx",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "withdraw_tx",
  "payload": {
    "tx": "tx_+LwLAfhCuED1O7wMWz3k97CV3vccDCOXDocd9pPvb8bJP5vAlkeEs5I/T2sTPlSbn+zHiZZg8tQeItSmoDycE1CbyLhl98kNuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgoz5Owl1o0h0zvFdmPVk2neg/+bAfMgkfFrplodFsVr8FA9gxScw="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "withdraw_created"
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
    "tx": "tx_+HI0AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgWhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAgCGEjCc5UAAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/BQOc0hNO",
    "updates": [
      {
        "amount": 2,
        "op": "OffChainWithdrawal",
        "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
      }
    ]
  },
  "tag": "withdraw_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "withdraw_ack",
  "payload": {
    "tx": "tx_+LwLAfhCuEC+Kq1Ma46dojlaplHUNPB1GoGgriOGmrqFvMuTwgO8WI1Oz5IvSqjKKKSvDLeeatz8SIpPaLBuih0Ta3vR0O0HuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgoz5Owl1o0h0zvFdmPVk2neg/+bAfMgkfFrplodFsVr8FA4hs5Hg="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P4LAfiEuEC+Kq1Ma46dojlaplHUNPB1GoGgriOGmrqFvMuTwgO8WI1Oz5IvSqjKKKSvDLeeatz8SIpPaLBuih0Ta3vR0O0HuED1O7wMWz3k97CV3vccDCOXDocd9pPvb8bJP5vAlkeEs5I/T2sTPlSbn+zHiZZg8tQeItSmoDycE1CbyLhl98kNuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgoz5Owl1o0h0zvFdmPVk2neg/+bAfMgkfFrplodFsVr8FAwJQUb0="
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
    "tx": "tx_+P4LAfiEuEC+Kq1Ma46dojlaplHUNPB1GoGgriOGmrqFvMuTwgO8WI1Oz5IvSqjKKKSvDLeeatz8SIpPaLBuih0Ta3vR0O0HuED1O7wMWz3k97CV3vccDCOXDocd9pPvb8bJP5vAlkeEs5I/T2sTPlSbn+zHiZZg8tQeItSmoDycE1CbyLhl98kNuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgoz5Owl1o0h0zvFdmPVk2neg/+bAfMgkfFrplodFsVr8FAwJQUb0="
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
    "event": "own_withdraw_locked"
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
    "event": "own_withdraw_locked"
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
    "event": "withdraw_locked"
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
    "event": "withdraw_locked"
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
    "state": "tx_+P4LAfiEuEC+Kq1Ma46dojlaplHUNPB1GoGgriOGmrqFvMuTwgO8WI1Oz5IvSqjKKKSvDLeeatz8SIpPaLBuih0Ta3vR0O0HuED1O7wMWz3k97CV3vccDCOXDocd9pPvb8bJP5vAlkeEs5I/T2sTPlSbn+zHiZZg8tQeItSmoDycE1CbyLhl98kNuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgoz5Owl1o0h0zvFdmPVk2neg/+bAfMgkfFrplodFsVr8FAwJQUb0="
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
    "state": "tx_+P4LAfiEuEC+Kq1Ma46dojlaplHUNPB1GoGgriOGmrqFvMuTwgO8WI1Oz5IvSqjKKKSvDLeeatz8SIpPaLBuih0Ta3vR0O0HuED1O7wMWz3k97CV3vccDCOXDocd9pPvb8bJP5vAlkeEs5I/T2sTPlSbn+zHiZZg8tQeItSmoDycE1CbyLhl98kNuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgoz5Owl1o0h0zvFdmPVk2neg/+bAfMgkfFrplodFsVr8FAwJQUb0="
  },
  "version": 1
}
```
