
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
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "tx": "tx_+HI0AaEGxg0THRn6EnayrKAiA7XHtC8jht9LlO75Omp4uAd28NWhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAgCGEjCc5UAAoEUfp6Gv3gLYNHIy08ITGVY9Xv7I69D5Yu0FUzyRePtuBAiB1DYi"
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
    "tx": "tx_+LwLAfhCuEDWK5IT8u7+ThM6U1uF13WsMsBBuQWvA35wXJeCH+PidpjeivQD4vB3imhRQo8gPPSbNkbvolMajwVYP8BpxzYEuHT4cjQBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACgRR+noa/eAtg0cjLTwhMZVj1e/sjr0Pli7QVTPJF4+24ECFbANeQ="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
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
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "tx": "tx_+HI0AaEGxg0THRn6EnayrKAiA7XHtC8jht9LlO75Omp4uAd28NWhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAgCGEjCc5UAAoEUfp6Gv3gLYNHIy08ITGVY9Xv7I69D5Yu0FUzyRePtuBAiB1DYi"
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
    "tx": "tx_+LwLAfhCuEDZd+OFg28UyfwTEDaw2JQ23oL8/Y8G06oi2YgSmG6pmvH0DbP/mbyTo7ZI5Jzv4veS4MrUQSor0d6Q9fWX8GoKuHT4cjQBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACgRR+noa/eAtg0cjLTwhMZVj1e/sjr0Pli7QVTPJF4+24ECPo7AIM="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "tx": "tx_+P4LAfiEuEDWK5IT8u7+ThM6U1uF13WsMsBBuQWvA35wXJeCH+PidpjeivQD4vB3imhRQo8gPPSbNkbvolMajwVYP8BpxzYEuEDZd+OFg28UyfwTEDaw2JQ23oL8/Y8G06oi2YgSmG6pmvH0DbP/mbyTo7ZI5Jzv4veS4MrUQSor0d6Q9fWX8GoKuHT4cjQBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACgRR+noa/eAtg0cjLTwhMZVj1e/sjr0Pli7QVTPJF4+24ECGAF7UQ="
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "tx": "tx_+P4LAfiEuEDWK5IT8u7+ThM6U1uF13WsMsBBuQWvA35wXJeCH+PidpjeivQD4vB3imhRQo8gPPSbNkbvolMajwVYP8BpxzYEuEDZd+OFg28UyfwTEDaw2JQ23oL8/Y8G06oi2YgSmG6pmvH0DbP/mbyTo7ZI5Jzv4veS4MrUQSor0d6Q9fWX8GoKuHT4cjQBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACgRR+noa/eAtg0cjLTwhMZVj1e/sjr0Pli7QVTPJF4+24ECGAF7UQ="
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
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
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
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
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
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
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
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
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "state": "tx_+P4LAfiEuEDWK5IT8u7+ThM6U1uF13WsMsBBuQWvA35wXJeCH+PidpjeivQD4vB3imhRQo8gPPSbNkbvolMajwVYP8BpxzYEuEDZd+OFg28UyfwTEDaw2JQ23oL8/Y8G06oi2YgSmG6pmvH0DbP/mbyTo7ZI5Jzv4veS4MrUQSor0d6Q9fWX8GoKuHT4cjQBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACgRR+noa/eAtg0cjLTwhMZVj1e/sjr0Pli7QVTPJF4+24ECGAF7UQ="
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "state": "tx_+P4LAfiEuEDWK5IT8u7+ThM6U1uF13WsMsBBuQWvA35wXJeCH+PidpjeivQD4vB3imhRQo8gPPSbNkbvolMajwVYP8BpxzYEuEDZd+OFg28UyfwTEDaw2JQ23oL8/Y8G06oi2YgSmG6pmvH0DbP/mbyTo7ZI5Jzv4veS4MrUQSor0d6Q9fWX8GoKuHT4cjQBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACgRR+noa/eAtg0cjLTwhMZVj1e/sjr0Pli7QVTPJF4+24ECGAF7UQ="
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
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "tx": "tx_+HI0AaEGxg0THRn6EnayrKAiA7XHtC8jht9LlO75Omp4uAd28NWhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAgCGEjCc5UAAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/BQN1p3Fv"
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
    "tx": "tx_+LwLAfhCuEDMNBnwys7ufbsc3CWZ7okYNBLVB+aARDbBkDlmzgCOt1uq+oPRcoVGE5oLUXXjQSUjoH0hdH+9XNI2xTD0xPUCuHT4cjQBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgoz5Owl1o0h0zvFdmPVk2neg/+bAfMgkfFrplodFsVr8FA2NhdBs="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
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
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "tx": "tx_+HI0AaEGxg0THRn6EnayrKAiA7XHtC8jht9LlO75Omp4uAd28NWhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAgCGEjCc5UAAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/BQN1p3Fv"
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
    "tx": "tx_+LwLAfhCuEAEu/G4dIWjTsOQHG4JE/VOsqwzUHaxV+fGdKcnMACtRfEhVG5rnTK+ov15z+9gANoynmRiV2cpO+RjrR8BzMsMuHT4cjQBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgoz5Owl1o0h0zvFdmPVk2neg/+bAfMgkfFrplodFsVr8FA97AHIc="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "tx": "tx_+P4LAfiEuEAEu/G4dIWjTsOQHG4JE/VOsqwzUHaxV+fGdKcnMACtRfEhVG5rnTK+ov15z+9gANoynmRiV2cpO+RjrR8BzMsMuEDMNBnwys7ufbsc3CWZ7okYNBLVB+aARDbBkDlmzgCOt1uq+oPRcoVGE5oLUXXjQSUjoH0hdH+9XNI2xTD0xPUCuHT4cjQBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgoz5Owl1o0h0zvFdmPVk2neg/+bAfMgkfFrplodFsVr8FA5ftFw4="
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "tx": "tx_+P4LAfiEuEAEu/G4dIWjTsOQHG4JE/VOsqwzUHaxV+fGdKcnMACtRfEhVG5rnTK+ov15z+9gANoynmRiV2cpO+RjrR8BzMsMuEDMNBnwys7ufbsc3CWZ7okYNBLVB+aARDbBkDlmzgCOt1uq+oPRcoVGE5oLUXXjQSUjoH0hdH+9XNI2xTD0xPUCuHT4cjQBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgoz5Owl1o0h0zvFdmPVk2neg/+bAfMgkfFrplodFsVr8FA5ftFw4="
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
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
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
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
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "event": "withdraw_locked"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
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
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "state": "tx_+P4LAfiEuEAEu/G4dIWjTsOQHG4JE/VOsqwzUHaxV+fGdKcnMACtRfEhVG5rnTK+ov15z+9gANoynmRiV2cpO+RjrR8BzMsMuEDMNBnwys7ufbsc3CWZ7okYNBLVB+aARDbBkDlmzgCOt1uq+oPRcoVGE5oLUXXjQSUjoH0hdH+9XNI2xTD0xPUCuHT4cjQBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgoz5Owl1o0h0zvFdmPVk2neg/+bAfMgkfFrplodFsVr8FA5ftFw4="
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "state": "tx_+P4LAfiEuEAEu/G4dIWjTsOQHG4JE/VOsqwzUHaxV+fGdKcnMACtRfEhVG5rnTK+ov15z+9gANoynmRiV2cpO+RjrR8BzMsMuEDMNBnwys7ufbsc3CWZ7okYNBLVB+aARDbBkDlmzgCOt1uq+oPRcoVGE5oLUXXjQSUjoH0hdH+9XNI2xTD0xPUCuHT4cjQBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgoz5Owl1o0h0zvFdmPVk2neg/+bAfMgkfFrplodFsVr8FA5ftFw4="
  },
  "version": 1
}
```
