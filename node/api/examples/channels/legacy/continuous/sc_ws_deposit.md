
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
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "tx": "tx_+HIzAaEGxg0THRn6EnayrKAiA7XHtC8jht9LlO75Omp4uAd28NWhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAgCGEjCc5UAAoIGnTOuUnVM9QThcVqCCAFeJ51D7a6A4ldyhd3nuKg7lAgdGp4fe"
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
    "tx": "tx_+LwLAfhCuEA8SP3yaWa1Esu9cpKAAdMio0dkAvSdorjnz4wrdSx5HKIupPoLNHygNM23uv9IMnOiVLDGFUZL26UDwnmYCKsFuHT4cjMBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACggadM65SdUz1BOFxWoIIAV4nnUPtroDiV3KF3ee4qDuUCB0cHknY="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
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
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "tx": "tx_+HIzAaEGxg0THRn6EnayrKAiA7XHtC8jht9LlO75Omp4uAd28NWhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAgCGEjCc5UAAoIGnTOuUnVM9QThcVqCCAFeJ51D7a6A4ldyhd3nuKg7lAgdGp4fe"
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
    "tx": "tx_+LwLAfhCuEB2IeqEF8suaKRzZCtzm2Ux2luV/FxDyqXd2i6ePUowdJhT6V1oqUFTcbOo3eh+fmZh3HDVyLFkckVR/192AVsFuHT4cjMBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACggadM65SdUz1BOFxWoIIAV4nnUPtroDiV3KF3ee4qDuUCB4YWJuc="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "tx": "tx_+P4LAfiEuEA8SP3yaWa1Esu9cpKAAdMio0dkAvSdorjnz4wrdSx5HKIupPoLNHygNM23uv9IMnOiVLDGFUZL26UDwnmYCKsFuEB2IeqEF8suaKRzZCtzm2Ux2luV/FxDyqXd2i6ePUowdJhT6V1oqUFTcbOo3eh+fmZh3HDVyLFkckVR/192AVsFuHT4cjMBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACggadM65SdUz1BOFxWoIIAV4nnUPtroDiV3KF3ee4qDuUCB50QwtI="
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
    "tx": "tx_+P4LAfiEuEA8SP3yaWa1Esu9cpKAAdMio0dkAvSdorjnz4wrdSx5HKIupPoLNHygNM23uv9IMnOiVLDGFUZL26UDwnmYCKsFuEB2IeqEF8suaKRzZCtzm2Ux2luV/FxDyqXd2i6ePUowdJhT6V1oqUFTcbOo3eh+fmZh3HDVyLFkckVR/192AVsFuHT4cjMBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACggadM65SdUz1BOFxWoIIAV4nnUPtroDiV3KF3ee4qDuUCB50QwtI="
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
    "event": "own_deposit_locked"
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
    "event": "own_deposit_locked"
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
    "event": "deposit_locked"
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
    "event": "deposit_locked"
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
    "state": "tx_+P4LAfiEuEA8SP3yaWa1Esu9cpKAAdMio0dkAvSdorjnz4wrdSx5HKIupPoLNHygNM23uv9IMnOiVLDGFUZL26UDwnmYCKsFuEB2IeqEF8suaKRzZCtzm2Ux2luV/FxDyqXd2i6ePUowdJhT6V1oqUFTcbOo3eh+fmZh3HDVyLFkckVR/192AVsFuHT4cjMBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACggadM65SdUz1BOFxWoIIAV4nnUPtroDiV3KF3ee4qDuUCB50QwtI="
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
    "state": "tx_+P4LAfiEuEA8SP3yaWa1Esu9cpKAAdMio0dkAvSdorjnz4wrdSx5HKIupPoLNHygNM23uv9IMnOiVLDGFUZL26UDwnmYCKsFuEB2IeqEF8suaKRzZCtzm2Ux2luV/FxDyqXd2i6ePUowdJhT6V1oqUFTcbOo3eh+fmZh3HDVyLFkckVR/192AVsFuHT4cjMBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACggadM65SdUz1BOFxWoIIAV4nnUPtroDiV3KF3ee4qDuUCB50QwtI="
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
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "tx": "tx_+HIzAaEGxg0THRn6EnayrKAiA7XHtC8jht9LlO75Omp4uAd28NWhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAgCGEjCc5UAAoHr2z45LVPg+SpWirnkAuHaxyvaxLNwH9YdfnLXjR9N4AwKbUsz1"
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
    "tx": "tx_+LwLAfhCuECnXvTpEQfZ9BLNmYFQgVXTJiGYiw/hITcvfAGixcWvGHI/ZwXlb4xRxkolCQ1bTrlOn03sI35FGSpg0Pt+kR4GuHT4cjMBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgevbPjktU+D5KlaKueQC4drHK9rEs3Af1h1+cteNH03gDAjJ5KiA="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
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
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "tx": "tx_+HIzAaEGxg0THRn6EnayrKAiA7XHtC8jht9LlO75Omp4uAd28NWhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAgCGEjCc5UAAoHr2z45LVPg+SpWirnkAuHaxyvaxLNwH9YdfnLXjR9N4AwKbUsz1"
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
    "tx": "tx_+LwLAfhCuEBMcJ3FRq9pR0nj1xnxViL4zSepDjnil3InMXMKkmsXEft9o+3UsNNONAxV7+AJEsV1ZTqG8ZBER9W/fpof+fYOuHT4cjMBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgevbPjktU+D5KlaKueQC4drHK9rEs3Af1h1+cteNH03gDAguQLKA="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "tx": "tx_+P4LAfiEuEBMcJ3FRq9pR0nj1xnxViL4zSepDjnil3InMXMKkmsXEft9o+3UsNNONAxV7+AJEsV1ZTqG8ZBER9W/fpof+fYOuECnXvTpEQfZ9BLNmYFQgVXTJiGYiw/hITcvfAGixcWvGHI/ZwXlb4xRxkolCQ1bTrlOn03sI35FGSpg0Pt+kR4GuHT4cjMBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgevbPjktU+D5KlaKueQC4drHK9rEs3Af1h1+cteNH03gDAjQGp+Y="
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
    "tx": "tx_+P4LAfiEuEBMcJ3FRq9pR0nj1xnxViL4zSepDjnil3InMXMKkmsXEft9o+3UsNNONAxV7+AJEsV1ZTqG8ZBER9W/fpof+fYOuECnXvTpEQfZ9BLNmYFQgVXTJiGYiw/hITcvfAGixcWvGHI/ZwXlb4xRxkolCQ1bTrlOn03sI35FGSpg0Pt+kR4GuHT4cjMBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgevbPjktU+D5KlaKueQC4drHK9rEs3Af1h1+cteNH03gDAjQGp+Y="
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
    "event": "own_deposit_locked"
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
    "event": "own_deposit_locked"
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
    "event": "deposit_locked"
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
    "event": "deposit_locked"
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
    "state": "tx_+P4LAfiEuEBMcJ3FRq9pR0nj1xnxViL4zSepDjnil3InMXMKkmsXEft9o+3UsNNONAxV7+AJEsV1ZTqG8ZBER9W/fpof+fYOuECnXvTpEQfZ9BLNmYFQgVXTJiGYiw/hITcvfAGixcWvGHI/ZwXlb4xRxkolCQ1bTrlOn03sI35FGSpg0Pt+kR4GuHT4cjMBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgevbPjktU+D5KlaKueQC4drHK9rEs3Af1h1+cteNH03gDAjQGp+Y="
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
    "state": "tx_+P4LAfiEuEBMcJ3FRq9pR0nj1xnxViL4zSepDjnil3InMXMKkmsXEft9o+3UsNNONAxV7+AJEsV1ZTqG8ZBER9W/fpof+fYOuECnXvTpEQfZ9BLNmYFQgVXTJiGYiw/hITcvfAGixcWvGHI/ZwXlb4xRxkolCQ1bTrlOn03sI35FGSpg0Pt+kR4GuHT4cjMBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCAIYSMJzlQACgevbPjktU+D5KlaKueQC4drHK9rEs3Af1h1+cteNH03gDAjQGp+Y="
  },
  "version": 1
}
```
