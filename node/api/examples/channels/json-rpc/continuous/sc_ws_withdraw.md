
#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.withdraw",
      "params": {
        "amount": "2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- node
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

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "tx": "tx_+LwLAfhCuECmn6QR8/VwIvc9avwtzuauqSn0NmmDZxYud6Oik+Q0pp6Lev/oK++PdEvZciumZpUbBdlfl3LIqHxc31+43NINuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACgRR+noa/eAtg0cjLTwhMZVj1e/sjr0Pli7QVTPJF4+24ECi9pymI="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
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

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "tx": "tx_+LwLAfhCuEBWNxnIoMVbGTp+NkKKg8NlXbgVe7PbdpiTBsq0qGD3gwDE4waZEjmlWUJKVi3VxHbmdhdKdZ1lFKkVtBfMM3YEuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACgRR+noa/eAtg0cjLTwhMZVj1e/sjr0Pli7QVTPJF4+24ECjOLPuM="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "tx": "tx_+P4LAfiEuEBWNxnIoMVbGTp+NkKKg8NlXbgVe7PbdpiTBsq0qGD3gwDE4waZEjmlWUJKVi3VxHbmdhdKdZ1lFKkVtBfMM3YEuECmn6QR8/VwIvc9avwtzuauqSn0NmmDZxYud6Oik+Q0pp6Lev/oK++PdEvZciumZpUbBdlfl3LIqHxc31+43NINuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACgRR+noa/eAtg0cjLTwhMZVj1e/sjr0Pli7QVTPJF4+24EChZDmcY="
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
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "tx": "tx_+P4LAfiEuEBWNxnIoMVbGTp+NkKKg8NlXbgVe7PbdpiTBsq0qGD3gwDE4waZEjmlWUJKVi3VxHbmdhdKdZ1lFKkVtBfMM3YEuECmn6QR8/VwIvc9avwtzuauqSn0NmmDZxYud6Oik+Q0pp6Lev/oK++PdEvZciumZpUbBdlfl3LIqHxc31+43NINuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACgRR+noa/eAtg0cjLTwhMZVj1e/sjr0Pli7QVTPJF4+24EChZDmcY="
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
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "state": "tx_+P4LAfiEuEBWNxnIoMVbGTp+NkKKg8NlXbgVe7PbdpiTBsq0qGD3gwDE4waZEjmlWUJKVi3VxHbmdhdKdZ1lFKkVtBfMM3YEuECmn6QR8/VwIvc9avwtzuauqSn0NmmDZxYud6Oik+Q0pp6Lev/oK++PdEvZciumZpUbBdlfl3LIqHxc31+43NINuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACgRR+noa/eAtg0cjLTwhMZVj1e/sjr0Pli7QVTPJF4+24EChZDmcY="
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
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "state": "tx_+P4LAfiEuEBWNxnIoMVbGTp+NkKKg8NlXbgVe7PbdpiTBsq0qGD3gwDE4waZEjmlWUJKVi3VxHbmdhdKdZ1lFKkVtBfMM3YEuECmn6QR8/VwIvc9avwtzuauqSn0NmmDZxYud6Oik+Q0pp6Lev/oK++PdEvZciumZpUbBdlfl3LIqHxc31+43NINuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACgRR+noa/eAtg0cjLTwhMZVj1e/sjr0Pli7QVTPJF4+24EChZDmcY="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.withdraw",
      "params": {
        "amount": "2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "tx": "tx_+HI0AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgWhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAgCGEjCc5UAAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/BQOc0hNO",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
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
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "tx": "tx_+LwLAfhCuED1O7wMWz3k97CV3vccDCOXDocd9pPvb8bJP5vAlkeEs5I/T2sTPlSbn+zHiZZg8tQeItSmoDycE1CbyLhl98kNuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgoz5Owl1o0h0zvFdmPVk2neg/+bAfMgkfFrplodFsVr8FA9gxScw="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "tx": "tx_+HI0AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgWhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAgCGEjCc5UAAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/BQOc0hNO",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
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
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "tx": "tx_+LwLAfhCuEC+Kq1Ma46dojlaplHUNPB1GoGgriOGmrqFvMuTwgO8WI1Oz5IvSqjKKKSvDLeeatz8SIpPaLBuih0Ta3vR0O0HuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgoz5Owl1o0h0zvFdmPVk2neg/+bAfMgkfFrplodFsVr8FA4hs5Hg="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "tx": "tx_+P4LAfiEuEC+Kq1Ma46dojlaplHUNPB1GoGgriOGmrqFvMuTwgO8WI1Oz5IvSqjKKKSvDLeeatz8SIpPaLBuih0Ta3vR0O0HuED1O7wMWz3k97CV3vccDCOXDocd9pPvb8bJP5vAlkeEs5I/T2sTPlSbn+zHiZZg8tQeItSmoDycE1CbyLhl98kNuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgoz5Owl1o0h0zvFdmPVk2neg/+bAfMgkfFrplodFsVr8FAwJQUb0="
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
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "tx": "tx_+P4LAfiEuEC+Kq1Ma46dojlaplHUNPB1GoGgriOGmrqFvMuTwgO8WI1Oz5IvSqjKKKSvDLeeatz8SIpPaLBuih0Ta3vR0O0HuED1O7wMWz3k97CV3vccDCOXDocd9pPvb8bJP5vAlkeEs5I/T2sTPlSbn+zHiZZg8tQeItSmoDycE1CbyLhl98kNuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgoz5Owl1o0h0zvFdmPVk2neg/+bAfMgkfFrplodFsVr8FAwJQUb0="
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
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "state": "tx_+P4LAfiEuEC+Kq1Ma46dojlaplHUNPB1GoGgriOGmrqFvMuTwgO8WI1Oz5IvSqjKKKSvDLeeatz8SIpPaLBuih0Ta3vR0O0HuED1O7wMWz3k97CV3vccDCOXDocd9pPvb8bJP5vAlkeEs5I/T2sTPlSbn+zHiZZg8tQeItSmoDycE1CbyLhl98kNuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgoz5Owl1o0h0zvFdmPVk2neg/+bAfMgkfFrplodFsVr8FAwJQUb0="
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
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "state": "tx_+P4LAfiEuEC+Kq1Ma46dojlaplHUNPB1GoGgriOGmrqFvMuTwgO8WI1Oz5IvSqjKKKSvDLeeatz8SIpPaLBuih0Ta3vR0O0HuED1O7wMWz3k97CV3vccDCOXDocd9pPvb8bJP5vAlkeEs5I/T2sTPlSbn+zHiZZg8tQeItSmoDycE1CbyLhl98kNuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgoz5Owl1o0h0zvFdmPVk2neg/+bAfMgkfFrplodFsVr8FAwJQUb0="
    }
  },
  "version": 1
}
```
