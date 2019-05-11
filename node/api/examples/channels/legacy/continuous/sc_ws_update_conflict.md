
#### initiator ---> node
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

#### responder ---> node
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

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+JU5AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUG+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAqDfIyBjJa3cm0yXcRvc1Ax1GckU5meyZ3GDH5pVC8PVRkV2uys=",
    "updates": [
      {
        "amount": 2,
        "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "op": "OffChainTransfer",
        "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
      }
    ]
  },
  "tag": "update",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+JU5AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUG+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4ZQlI08=",
    "updates": [
      {
        "amount": 1,
        "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "op": "OffChainTransfer",
        "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
      }
    ]
  },
  "tag": "update",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEDWVVq+T6+8/8GnSgbe9W7Dc6D09DEiCQMUQk5ubPwMTJ/H7a56ib4HIh1/X1xMDoz2ZT0UScWBZ69JDP/vFd0DuJf4lTkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQb4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoNUqd4GTOFacRsLar0VqTNSHraQXvmyQrL/MBqX090LhOlAdbA=="
  }
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEAx1al7l21Uag+ecLMazfJqII0IZM7z2WYjZM1zGyiivorWcF6XWNEUFvLitOJstRNN7fdbKlEY/+TRtkCR+6IEuJf4lTkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQb4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQCoN8jIGMlrdybTJdxG9zUDHUZyRTmZ7JncYMfmlULw9VGkaKCMA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "conflict",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "round": 5
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "conflict",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "round": 5
  },
  "version": 1
}
```

#### responder ---> node
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

#### initiator ---> node
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

#### responder <--- node
```javascript
{
  "action": "conflict",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "round": 5
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "conflict",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "round": 5
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
    "tx": "tx_+JU5AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90Tse7ZkU4=",
    "updates": [
      {
        "amount": 1,
        "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "op": "OffChainTransfer",
        "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
      }
    ]
  },
  "tag": "update",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEA+NSj9YoU6yhd6rvyllDAwjMlUkYw9xfj5HwldFKhO8NiuA4982ysDRv5AZBjRNBQmBaOmfxCDAS5ui9HRZmsCuJf4lTkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQb4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROxp+urmw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+JU5AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAqD+umuKN7Gji9wLmdyY8vN+2j3khw/nkE8xwyPc5Xq1EB5VF7A=",
    "updates": [
      {
        "amount": 2,
        "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "op": "OffChainTransfer",
        "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
      }
    ]
  },
  "tag": "update",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEDdTkwDSWLP4wHPSgzias42ovBki+KRHH635drNOkBFiEq5BCb8VqoiiGc65t4MgIuSsW/n3JNamvAHh/E5dXECuJf4lTkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQb4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCoP66a4o3saOL3AuZ3Jjy837aPeSHD+eQTzHDI9zlerUQz5mM4g=="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "conflict",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "round": 5
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "conflict",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "round": 5
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "conflict",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "round": 5
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "conflict",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "round": 5
  },
  "version": 1
}
```
