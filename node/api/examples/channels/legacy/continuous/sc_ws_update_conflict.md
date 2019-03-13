
#### initiator ---> node (2019-03-18 14:15:56.779)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 1,
    "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
  },
  "tag": "new"
}
```

#### responder ---> node (2019-03-18 14:15:56.779)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 2,
    "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
  },
  "tag": "new"
}
```

#### responder <--- node (2019-03-18 14:15:56.797)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "tx": "tx_+JU5AaEGxg0THRn6EnayrKAiA7XHtC8jht9LlO75Omp4uAd28NUG+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAqDfIyBjJa3cm0yXcRvc1Ax1GckU5meyZ3GDH5pVC8PVRuHe9jg="
  },
  "tag": "update",
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:15:56.802)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "tx": "tx_+JU5AaEGxg0THRn6EnayrKAiA7XHtC8jht9LlO75Omp4uAd28NUG+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4a/QsrE="
  },
  "tag": "update",
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:15:56.804)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuECpOlAuBnwgezZlvmIZkD2Yw4xheb/BTnZaz+jAv2brWWoaUl95yOwZ6ataFXQmXvf3gVB7nGmWljxpHw0wwfIAuJf4lTkBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1Qb4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoNUqd4GTOFacRsLar0VqTNSHraQXvmyQrL/MBqX090LhsL9soA=="
  }
}
```

#### responder ---> node (2019-03-18 14:15:56.805)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEC9lVPohZaTCsPPxbOXsDOZQvX2YPVx+0Z/3AYVkStS3dh9Rg2jmQE3fLj7ryk/lpVqDLSIDmVmDAh2U2evlc0BuJf4lTkBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1Qb4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCoN8jIGMlrdybTJdxG9zUDHUZyRTmZ7JncYMfmlULw9VGqnTrSA=="
  }
}
```

#### responder <--- node (2019-03-18 14:15:56.844)
```javascript
{
  "action": "conflict",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
    "round": 5
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:15:56.847)
```javascript
{
  "action": "conflict",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
    "round": 5
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:15:56.848)
```javascript
{
  "action": "conflict",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
    "round": 5
  },
  "version": 1
}
```

#### responder ---> node (2019-03-18 14:15:56.849)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 1,
    "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
  },
  "tag": "new"
}
```

#### initiator ---> node (2019-03-18 14:15:56.849)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 2,
    "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
  },
  "tag": "new"
}
```

#### initiator <--- node (2019-03-18 14:15:56.853)
```javascript
{
  "action": "conflict",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
    "round": 5
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:15:56.872)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "tx": "tx_+JU5AaEGxg0THRn6EnayrKAiA7XHtC8jht9LlO75Omp4uAd28NUG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsfdTdV0="
  },
  "tag": "update",
  "version": 1
}
```

#### responder ---> node (2019-03-18 14:15:56.874)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEATbgyjHT777sQwUZ5HpCkiIfLk7E3zA389FnfKLUzh42tJbVzAncoecVvYcAWm1fLUBU1xAh5rFr2lLQXOWfkJuJf4lTkBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1Qb4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROxMAAcuQ=="
  }
}
```

#### initiator <--- node (2019-03-18 14:15:56.880)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "tx": "tx_+JU5AaEGxg0THRn6EnayrKAiA7XHtC8jht9LlO75Omp4uAd28NUG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAqD+umuKN7Gji9wLmdyY8vN+2j3khw/nkE8xwyPc5Xq1ECA9/iI="
  },
  "tag": "update",
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:15:56.881)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEALd8FWgz44mZjLGiEBgOU2JH58M+HnlRr2M5jOJXKvBavIiF1EGurOUxsfFK5N+D5444ik74jIm+SbVxuFWDQJuJf4lTkBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1Qb4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCoP66a4o3saOL3AuZ3Jjy837aPeSHD+eQTzHDI9zlerUQB2Ffrg=="
  }
}
```

#### initiator <--- node (2019-03-18 14:15:56.900)
```javascript
{
  "action": "conflict",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
    "round": 5
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:15:56.901)
```javascript
{
  "action": "conflict",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
    "round": 5
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:15:56.902)
```javascript
{
  "action": "conflict",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
    "round": 5
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:15:56.905)
```javascript
{
  "action": "conflict",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
    "round": 5
  },
  "version": 1
}
```
