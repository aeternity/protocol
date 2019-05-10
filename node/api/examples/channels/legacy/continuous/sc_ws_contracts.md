
#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAnHQYrA==",
    "code": "cb_+QP1RgKg/ukoFMi2RBUIDNHZ3pMMzHSrPs/uKkwO/vEf7cRnitr5Avv5ASqgaPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8WEbWFpbrjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QHLoLnJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqhGluaXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uMxiAABkYgAAhJGAgIBRf7nJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqFGIAAMBXUIBRf2jyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFFGIAAK9XUGABGVEAW2AAGVlgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tZWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2ADgVKBUpBWW2AgAVFRWVCAkVBQgJBQkFZbUFCCkVBQYgAAjFaFMi4xLjAhVoVW",
    "deposit": 10,
    "vm_version": 3
  },
  "tag": "new_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QTXOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FBvkEjrkEi/kEiIICPQGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmgwMAAbkD+PkD9UYCoP7pKBTItkQVCAzR2d6TDMx0qz7P7ipMDv7xH+3EZ4ra+QL7+QEqoGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFhG1haW64wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPkBy6C5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6oRpbml0uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+5AUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7jMYgAAZGIAAISRgICAUX+5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6hRiAADAV1CAUX9o8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxRRiAACvV1BgARlRAFtgABlZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbWVlgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgA4FSgVKQVltgIAFRUVlQgJFQUICQUJBWW1BQgpFQUGIAAIxWhTIuMS4wCrhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoIz9yhHp4TfRRUoSVD3n476Oqo+7A33pu5LuX8v9hxOA+DIQvQ==",
    "updates": [
      {
        "abi_version": 1,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAnHQYrA==",
        "code": "cb_+QP1RgKg/ukoFMi2RBUIDNHZ3pMMzHSrPs/uKkwO/vEf7cRnitr5Avv5ASqgaPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8WEbWFpbrjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QHLoLnJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqhGluaXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uMxiAABkYgAAhJGAgIBRf7nJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqFGIAAMBXUIBRf2jyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFFGIAAK9XUGABGVEAW2AAGVlgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tZWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2ADgVKBUpBWW2AgAVFRWVCAkVBQgJBQkFZbUFCCkVBQYgAAjFaFMi4xLjAhVoVW",
        "deposit": 10,
        "op": "OffChainNewContract",
        "owner": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "vm_version": 3
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
    "tx": "tx_+QUjCwH4QrhAA4QgOat3r4SK+K2SoTOG39wiNGI4/p9XTAmTIsD9UbG8p6afMIiPgu1OP5aLVUZKsQENeMtntzxryu8ao7lQBrkE2vkE1zkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQb5BI65BIv5BIiCAj0BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoMDAAG5A/j5A/VGAqD+6SgUyLZEFQgM0dnekwzMdKs+z+4qTA7+8R/txGeK2vkC+/kBKqBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxYRtYWluuMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AcuguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeqEaW5pdLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4zGIAAGRiAACEkYCAgFF/uclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoUYgAAwFdQgFF/aPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8UUYgAAr1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW1lZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYAOBUoFSkFZbYCABUVFZUICRUFCAkFCQVltQUIKRUFBiAACMVoUyLjEuMAq4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKCM/coR6eE30UVKElQ95+O+jqqPuwN96buS7l/L/YcTgJuFGps="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QTXOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FBvkEjrkEi/kEiIICPQGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmgwMAAbkD+PkD9UYCoP7pKBTItkQVCAzR2d6TDMx0qz7P7ipMDv7xH+3EZ4ra+QL7+QEqoGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFhG1haW64wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPkBy6C5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6oRpbml0uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+5AUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7jMYgAAZGIAAISRgICAUX+5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6hRiAADAV1CAUX9o8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxRRiAACvV1BgARlRAFtgABlZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbWVlgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgA4FSgVKQVltgIAFRUVlQgJFQUICQUJBWW1BQgpFQUGIAAIxWhTIuMS4wCrhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoIz9yhHp4TfRRUoSVD3n476Oqo+7A33pu5LuX8v9hxOA+DIQvQ==",
    "updates": [
      {
        "abi_version": 1,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAnHQYrA==",
        "code": "cb_+QP1RgKg/ukoFMi2RBUIDNHZ3pMMzHSrPs/uKkwO/vEf7cRnitr5Avv5ASqgaPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8WEbWFpbrjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QHLoLnJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqhGluaXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uMxiAABkYgAAhJGAgIBRf7nJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqFGIAAMBXUIBRf2jyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFFGIAAK9XUGABGVEAW2AAGVlgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tZWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2ADgVKBUpBWW2AgAVFRWVCAkVBQgJBQkFZbUFCCkVBQYgAAjFaFMi4xLjAhVoVW",
        "deposit": 10,
        "op": "OffChainNewContract",
        "owner": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "vm_version": 3
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QUjCwH4QrhAn97VoFwTvEdI1xGr/dFXXbZNNCjn66b4u04bGV5+xWMsOsLRXlJKyuoDpskzy17LfCF1mxfHS/GsYGN4odkBDrkE2vkE1zkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQb5BI65BIv5BIiCAj0BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoMDAAG5A/j5A/VGAqD+6SgUyLZEFQgM0dnekwzMdKs+z+4qTA7+8R/txGeK2vkC+/kBKqBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxYRtYWluuMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AcuguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeqEaW5pdLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4zGIAAGRiAACEkYCAgFF/uclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoUYgAAwFdQgFF/aPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8UUYgAAr1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW1lZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYAOBUoFSkFZbYCABUVFZUICRUFCAkFCQVltQUIKRUFBiAACMVoUyLjEuMAq4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKCM/coR6eE30UVKElQ95+O+jqqPuwN96buS7l/L/YcTgPTCWa8="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QVlCwH4hLhAA4QgOat3r4SK+K2SoTOG39wiNGI4/p9XTAmTIsD9UbG8p6afMIiPgu1OP5aLVUZKsQENeMtntzxryu8ao7lQBrhAn97VoFwTvEdI1xGr/dFXXbZNNCjn66b4u04bGV5+xWMsOsLRXlJKyuoDpskzy17LfCF1mxfHS/GsYGN4odkBDrkE2vkE1zkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQb5BI65BIv5BIiCAj0BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoMDAAG5A/j5A/VGAqD+6SgUyLZEFQgM0dnekwzMdKs+z+4qTA7+8R/txGeK2vkC+/kBKqBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxYRtYWluuMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AcuguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeqEaW5pdLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4zGIAAGRiAACEkYCAgFF/uclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoUYgAAwFdQgFF/aPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8UUYgAAr1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW1lZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYAOBUoFSkFZbYCABUVFZUICRUFCAkFCQVltQUIKRUFBiAACMVoUyLjEuMAq4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKCM/coR6eE30UVKElQ95+O+jqqPuwN96buS7l/L/YcTgNbQi/k="
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
    "state": "tx_+QVlCwH4hLhAA4QgOat3r4SK+K2SoTOG39wiNGI4/p9XTAmTIsD9UbG8p6afMIiPgu1OP5aLVUZKsQENeMtntzxryu8ao7lQBrhAn97VoFwTvEdI1xGr/dFXXbZNNCjn66b4u04bGV5+xWMsOsLRXlJKyuoDpskzy17LfCF1mxfHS/GsYGN4odkBDrkE2vkE1zkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQb5BI65BIv5BIiCAj0BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoMDAAG5A/j5A/VGAqD+6SgUyLZEFQgM0dnekwzMdKs+z+4qTA7+8R/txGeK2vkC+/kBKqBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxYRtYWluuMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AcuguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeqEaW5pdLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4zGIAAGRiAACEkYCAgFF/uclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoUYgAAwFdQgFF/aPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8UUYgAAr1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW1lZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYAOBUoFSkFZbYCABUVFZUICRUFCAkFCQVltQUIKRUFBiAACMVoUyLjEuMAq4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKCM/coR6eE30UVKElQ95+O+jqqPuwN96buS7l/L/YcTgNbQi/k="
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
        "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
        "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FB/jWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQXMSDYKchQbN/BdXL3PgW4GBwYGgLkzPIGiw15gFwyhlgEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgaPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAqwKABpIYzv3s6vpo73EJCQlnZk691a1DppFVuPFwVZkV9XtTR+I8=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhAICk+6RJP3Fif5pQODnE8gWwbqI06Zgd5eD2ddfSffHP/NtCj+SzHG5HWptmFUFttVHth3jpgayTH30EOMT+VCLkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQf41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEFzEg2CnIUGzfwXVy9z4FuBgcGBoC5MzyBosNeYBcMoZYBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKsCgAaSGM797Or6aO9xCQkJZ2ZOvdWtQ6aRVbjxcFWZFfV6hTtoI"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FB/jWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQXMSDYKchQbN/BdXL3PgW4GBwYGgLkzPIGiw15gFwyhlgEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgaPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAqwKABpIYzv3s6vpo73EJCQlnZk691a1DppFVuPFwVZkV9XtTR+I8=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhAX3Lkb2zdZnacQ5NGWfu8PaOyYL1E2zd44FYbU5AD2RCIfIrvjzLjeB4LvdWVS8AJnVLNzrb6v5VQmp/iAX87CbkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQf41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEFzEg2CnIUGzfwXVy9z4FuBgcGBoC5MzyBosNeYBcMoZYBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKsCgAaSGM797Or6aO9xCQkJZ2ZOvdWtQ6aRVbjxcFWZFfV5g8Xt5"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAICk+6RJP3Fif5pQODnE8gWwbqI06Zgd5eD2ddfSffHP/NtCj+SzHG5HWptmFUFttVHth3jpgayTH30EOMT+VCLhAX3Lkb2zdZnacQ5NGWfu8PaOyYL1E2zd44FYbU5AD2RCIfIrvjzLjeB4LvdWVS8AJnVLNzrb6v5VQmp/iAX87CbkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQf41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEFzEg2CnIUGzfwXVy9z4FuBgcGBoC5MzyBosNeYBcMoZYBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKsCgAaSGM797Or6aO9xCQkJZ2ZOvdWtQ6aRVbjxcFWZFfV4UMoIT"
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
    "state": "tx_+QGsCwH4hLhAICk+6RJP3Fif5pQODnE8gWwbqI06Zgd5eD2ddfSffHP/NtCj+SzHG5HWptmFUFttVHth3jpgayTH30EOMT+VCLhAX3Lkb2zdZnacQ5NGWfu8PaOyYL1E2zd44FYbU5AD2RCIfIrvjzLjeB4LvdWVS8AJnVLNzrb6v5VQmp/iAX87CbkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQf41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEFzEg2CnIUGzfwXVy9z4FuBgcGBoC5MzyBosNeYBcMoZYBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKsCgAaSGM797Or6aO9xCQkJZ2ZOvdWtQ6aRVbjxcFWZFfV4UMoIT"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "dry_run",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
  },
  "tag": "call_contract"
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
        "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "dry_run",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
  },
  "tag": "call_contract"
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
        "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "dry_run",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "dry_run",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 8,
    "contract_id": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
    "gas_price": 1,
    "gas_used": 192,
    "height": 8,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACr8s/aY"
  },
  "tag": "call_contract",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
    "round": 7
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 7,
    "contract_id": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
    "gas_price": 1,
    "gas_used": 192,
    "height": 7,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACr8s/aY"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
    "round": 7
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 7,
    "contract_id": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
    "gas_price": 1,
    "gas_used": 192,
    "height": 7,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACr8s/aY"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
    "round": 7
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 7,
    "contract_id": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
    "gas_price": 1,
    "gas_used": 192,
    "height": 7,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACr8s/aY"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
    "round": 7
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 7,
    "contract_id": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
    "gas_price": 1,
    "gas_used": 192,
    "height": 7,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACr8s/aY"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "clean_contract_calls"
}
```

#### initiator <--- node
```javascript
{
  "action": "calls_pruned",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
    "round": 7
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "call_not_found",
    "request": {
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
        "round": 7
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
        "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
        "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FCPjWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQXMSDYKchQbN/BdXL3PgW4GBwYGgLkzPIGiw15gFwyhlgEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgaPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAqwKBmNmU3LwTMKrAhSxwIUR59mTgDbVqjhQNnALqIc1ncQ5mkxak=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhAsiGALSOnzLx95Bk8unNXuxeRKqRRxisVaIKMajNFLhSkieah4h96xwIu0FpsRjFgblzGjHOZSQlsAH/iUvpoCrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQj41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEFzEg2CnIUGzfwXVy9z4FuBgcGBoC5MzyBosNeYBcMoZYBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKsCgZjZlNy8EzCqwIUscCFEefZk4A21ao4UDZwC6iHNZ3EPscgv1"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FCPjWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQXMSDYKchQbN/BdXL3PgW4GBwYGgLkzPIGiw15gFwyhlgEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgaPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAqwKBmNmU3LwTMKrAhSxwIUR59mTgDbVqjhQNnALqIc1ncQ5mkxak=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhAFTUbMymALIdq1DFUQLov+rItP4g6pIc5IVxUoT5Gt3XlXI+zYYyeFC2aoAv+BMghSuF3bR77a9ZqsabtfLH1B7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQj41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEFzEg2CnIUGzfwXVy9z4FuBgcGBoC5MzyBosNeYBcMoZYBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKsCgZjZlNy8EzCqwIUscCFEefZk4A21ao4UDZwC6iHNZ3ENFKkBe"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAFTUbMymALIdq1DFUQLov+rItP4g6pIc5IVxUoT5Gt3XlXI+zYYyeFC2aoAv+BMghSuF3bR77a9ZqsabtfLH1B7hAsiGALSOnzLx95Bk8unNXuxeRKqRRxisVaIKMajNFLhSkieah4h96xwIu0FpsRjFgblzGjHOZSQlsAH/iUvpoCrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQj41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEFzEg2CnIUGzfwXVy9z4FuBgcGBoC5MzyBosNeYBcMoZYBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKsCgZjZlNy8EzCqwIUscCFEefZk4A21ao4UDZwC6iHNZ3EMR8cBv"
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
    "state": "tx_+QGsCwH4hLhAFTUbMymALIdq1DFUQLov+rItP4g6pIc5IVxUoT5Gt3XlXI+zYYyeFC2aoAv+BMghSuF3bR77a9ZqsabtfLH1B7hAsiGALSOnzLx95Bk8unNXuxeRKqRRxisVaIKMajNFLhSkieah4h96xwIu0FpsRjFgblzGjHOZSQlsAH/iUvpoCrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQj41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEFzEg2CnIUGzfwXVy9z4FuBgcGBoC5MzyBosNeYBcMoZYBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKsCgZjZlNy8EzCqwIUscCFEefZk4A21ao4UDZwC6iHNZ3EMR8cBv"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "dry_run",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
  },
  "tag": "call_contract"
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
        "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "dry_run",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
  },
  "tag": "call_contract"
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
        "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "dry_run",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "dry_run",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 9,
    "contract_id": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
    "gas_price": 1,
    "gas_used": 192,
    "height": 9,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACr8s/aY"
  },
  "tag": "call_contract",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
    "round": 8
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 8,
    "contract_id": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
    "gas_price": 1,
    "gas_used": 192,
    "height": 8,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACr8s/aY"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
    "round": 8
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 8,
    "contract_id": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5",
    "gas_price": 1,
    "gas_used": 192,
    "height": 8,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACr8s/aY"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
    ],
    "contracts": [
      "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
    ]
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "poi": "pi_+QjLPAH5Aar5AaegUHXVJYllXPYCKsNzFPm556q8IgudzPRI4O/BDFpobNP5AYP4lKBQddUliWVc9gIqw3MU+bnnqrwiC53M9Ejg78EMWmhs0/hxgICAgICAoO0CFjxibIfdehu8wgGaVHmkULhlWpsI0fCWsUChDyMJgICAgKCQ1bLD69k9BcQwVvuyoPXBJe++idIJ/lwoO4qPYlt0YaCmyjgxBha42v7WL6pOfqG1Ttf6NYVnqZHqR+T0JmGLxYCAgID4T6CQ1bLD69k9BcQwVvuyoPXBJe++idIJ/lwoO4qPYlt0Ye2gMbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aLygoBAIY/qiUiX/X4SaCmyjgxBha42v7WL6pOfqG1Ttf6NYVnqZHqR+T0JmGLxeegPEg2CnIUGzfwXVy9z4FuBgcGBoC5MzyBosNeYBcMoZaFxAoBAAr4T6DtAhY8YmyH3XobvMIBmlR5pFC4ZVqbCNHwlrFAoQ8jCe2gNxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAHj4qAjoqXI5ZEb6//BQUWWVlPkHd4lWRhzVFmXY/6F2X4ZBMDA+Qby+QbvoCP+J+CKG9HLoyiF11XYCmZ637Cc43DhBKz5ZV3DDp7r+QbL+IagCHQOBl3W9IhcdkmZJCJrKJ+h0G8+ZeIKUZ3W5p9/Nez4YyC4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///////////////////////////////////////////hmoCP+J+CKG9HLoyiF11XYCmZ637Cc43DhBKz5ZV3DDp7r+EOhAMxINgpyFBs38F1cvc+BbgYHBgaAuTM8gaLDXmAXDKGWoFfuIRzcN3UiqZeS8ooxO7bH4x9PphQ5GgpJtO3WWhJu+ESgJ6ky/mLaY+D64bXs7TR5BIRxO0hOakcKlSHrfu7sP7/iEKA1jHy+JkYGJXeg4QZT9QYTyIjuaukMdPKoxXeDh8vbz/hToDWMfL4mRgYld6DhBlP1BhPIiO5q6Qx08qjFd4OHy9vP8aCFlE6Nir08G/FQ+dPMIRjPZKt+jIKfH4aEhiH2DCC/C4CAgICAgICAgICAgICAgAD4RKA/cNKMPbnMACszBp/R0S52OAbwRhxnBpoCOSMcfJ92pOIgoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QSBoFfuIRzcN3UiqZeS8ooxO7bH4x9PphQ5GgpJtO3WWhJu+QRdgKAnqTL+Ytpj4PrhteztNHkEhHE7SE5qRwqVIet+7uw/v4CAgICAgICAgICAgICAuQQq+QQnKAGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmgwMAAbkD+PkD9UYCoP7pKBTItkQVCAzR2d6TDMx0qz7P7ipMDv7xH+3EZ4ra+QL7+QEqoGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFhG1haW64wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPkBy6C5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6oRpbml0uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+5AUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7jMYgAAZGIAAISRgICAUX+5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6hRiAADAV1CAUX9o8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxRRiAACvV1BgARlRAFtgABlZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbWVlgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgA4FSgVKQVltgIAFRUVlQgJFQUICQUJBWW1BQgpFQUGIAAIxWhTIuMS4wgAHACvh0oIWUTo2KvTwb8VD508whGM9kq36Mgp8fhoSGIfYMIL8L+FGgP3DSjD25zAArMwaf0dEudjgG8EYcZwaaAjkjHHyfdqSgCHQOBl3W9IhcdkmZJCJrKJ+h0G8+ZeIKUZ3W5p9/NeyAgICAgICAgICAgICAgIDAwC95Gqk="
  },
  "tag": "poi",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
    ],
    "contracts": [
      "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
    ]
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "poi": "pi_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AAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7jMYgAAZGIAAISRgICAUX+5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6hRiAADAV1CAUX9o8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxRRiAACvV1BgARlRAFtgABlZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbWVlgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgA4FSgVKQVltgIAFRUVlQgJFQUICQUJBWW1BQgpFQUGIAAIxWhTIuMS4wgAHACvh0oIWUTo2KvTwb8VD508whGM9kq36Mgp8fhoSGIfYMIL8L+FGgP3DSjD25zAArMwaf0dEudjgG8EYcZwaaAjkjHHyfdqSgCHQOBl3W9IhcdkmZJCJrKJ+h0G8+ZeIKUZ3W5p9/NeyAgICAgICAgICAgICAgIDAwC95Gqk="
  },
  "tag": "poi",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: accounts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: contracts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: accounts, contracts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_found",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_found",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: accounts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: contracts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: accounts, contracts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_found",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_found",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
    "code": "cb_+QW1RgKg2lZpnzaTbMnkiHSWtrDsi8S15f+OP6poqJ7cHBpu7OD5BEX4yaBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjqoLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2u4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////+QKLoOIjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEhGluaXS4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTIuMS4whY3lSg==",
    "deposit": 10,
    "vm_version": 3
  },
  "tag": "new_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+Qa3OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FCfkGbrkGa/kGaIICPQGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmgwMAAbkFuPkFtUYCoNpWaZ82k2zJ5Ih0lraw7IvEteX/jj+qaKie3Bwabuzg+QRF+MmgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD46qCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNruGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///////////////////////////////////////////kCi6DiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRIRpbml0uMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC5AaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoUyLjEuMAq4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAVoKnmKHZ5S/tiCpZyBlSFrzXuW+VeruAz93izbhLLDMknyyQQ4Q==",
    "updates": [
      {
        "abi_version": 1,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
        "code": "cb_+QW1RgKg2lZpnzaTbMnkiHSWtrDsi8S15f+OP6poqJ7cHBpu7OD5BEX4yaBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjqoLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2u4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////+QKLoOIjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEhGluaXS4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTIuMS4whY3lSg==",
        "deposit": 10,
        "op": "OffChainNewContract",
        "owner": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "vm_version": 3
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
    "tx": "tx_+QcDCwH4QrhAfS6d/OjqzPYwYxjAM7qSY6bXKoK3q8rnxF6yvD9OfFJyky9z0h9d2nS5KwsrPxfS6eG/Z6Flug2LQKiYQa4MD7kGuvkGtzkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQn5Bm65Bmv5BmiCAj0BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoMDAAG5Bbj5BbVGAqDaVmmfNpNsyeSIdJa2sOyLxLXl/44/qmiontwcGm7s4PkERfjJoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Oqgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGlja7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoug4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdLjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQGgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC5AUFiAACPYgAAwpGAgIBRf0nsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3FGIAATZXUICAUX/iIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRBRiAADRV1CAUX+zVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCThRiAAEbV1BgARlRAFtgABlZYCABkIFSYCCQA2AAWZCBUoFSWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW2AAUVGQVltgIAFRUZBQg5JQgJFQUIBZkIFSWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2AAWZCBUoFSWWAgAZCBUmAgkANgA4FSgVKQUJBWW1BZUFBgAFFgAWAAUVEBWZCBUpBQYABSWZBWW1BQWVBQYgAAylaFMi4xLjAKuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOIjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFaCp5ih2eUv7YgqWcgZUha817lvlXq7gM/d4s24SywzJJ+dyW5k="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+Qa3OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FCfkGbrkGa/kGaIICPQGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmgwMAAbkFuPkFtUYCoNpWaZ82k2zJ5Ih0lraw7IvEteX/jj+qaKie3Bwabuzg+QRF+MmgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD46qCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNruGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///////////////////////////////////////////kCi6DiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRIRpbml0uMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC5AaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoUyLjEuMAq4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAVoKnmKHZ5S/tiCpZyBlSFrzXuW+VeruAz93izbhLLDMknyyQQ4Q==",
    "updates": [
      {
        "abi_version": 1,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
        "code": "cb_+QW1RgKg2lZpnzaTbMnkiHSWtrDsi8S15f+OP6poqJ7cHBpu7OD5BEX4yaBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjqoLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2u4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////+QKLoOIjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEhGluaXS4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTIuMS4whY3lSg==",
        "deposit": 10,
        "op": "OffChainNewContract",
        "owner": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "vm_version": 3
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QcDCwH4QrhAMBIp8c35zsU1IdtTeN5x41ffCJy9cOSKPo3HhQMh0uvCOoPVbuWwM0TMrWeOgxJ01Tsp2W5FJ10AcAf3xYL3DbkGuvkGtzkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQn5Bm65Bmv5BmiCAj0BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoMDAAG5Bbj5BbVGAqDaVmmfNpNsyeSIdJa2sOyLxLXl/44/qmiontwcGm7s4PkERfjJoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Oqgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGlja7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoug4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdLjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQGgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC5AUFiAACPYgAAwpGAgIBRf0nsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3FGIAATZXUICAUX/iIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRBRiAADRV1CAUX+zVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCThRiAAEbV1BgARlRAFtgABlZYCABkIFSYCCQA2AAWZCBUoFSWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW2AAUVGQVltgIAFRUZBQg5JQgJFQUIBZkIFSWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2AAWZCBUoFSWWAgAZCBUmAgkANgA4FSgVKQUJBWW1BZUFBgAFFgAWAAUVEBWZCBUpBQYABSWZBWW1BQWVBQYgAAylaFMi4xLjAKuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOIjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFaCp5ih2eUv7YgqWcgZUha817lvlXq7gM/d4s24SywzJJ3HZ5vw="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QdFCwH4hLhAMBIp8c35zsU1IdtTeN5x41ffCJy9cOSKPo3HhQMh0uvCOoPVbuWwM0TMrWeOgxJ01Tsp2W5FJ10AcAf3xYL3DbhAfS6d/OjqzPYwYxjAM7qSY6bXKoK3q8rnxF6yvD9OfFJyky9z0h9d2nS5KwsrPxfS6eG/Z6Flug2LQKiYQa4MD7kGuvkGtzkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQn5Bm65Bmv5BmiCAj0BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoMDAAG5Bbj5BbVGAqDaVmmfNpNsyeSIdJa2sOyLxLXl/44/qmiontwcGm7s4PkERfjJoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Oqgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGlja7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoug4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdLjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQGgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC5AUFiAACPYgAAwpGAgIBRf0nsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3FGIAATZXUICAUX/iIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRBRiAADRV1CAUX+zVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCThRiAAEbV1BgARlRAFtgABlZYCABkIFSYCCQA2AAWZCBUoFSWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW2AAUVGQVltgIAFRUZBQg5JQgJFQUIBZkIFSWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2AAWZCBUoFSWWAgAZCBUmAgkANgA4FSgVKQUJBWW1BZUFBgAFFgAWAAUVEBWZCBUpBQYABSWZBWW1BQWVBQYgAAylaFMi4xLjAKuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOIjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFaCp5ih2eUv7YgqWcgZUha817lvlXq7gM/d4s24SywzJJ85AXQs="
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
    "state": "tx_+QdFCwH4hLhAMBIp8c35zsU1IdtTeN5x41ffCJy9cOSKPo3HhQMh0uvCOoPVbuWwM0TMrWeOgxJ01Tsp2W5FJ10AcAf3xYL3DbhAfS6d/OjqzPYwYxjAM7qSY6bXKoK3q8rnxF6yvD9OfFJyky9z0h9d2nS5KwsrPxfS6eG/Z6Flug2LQKiYQa4MD7kGuvkGtzkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBQn5Bm65Bmv5BmiCAj0BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoMDAAG5Bbj5BbVGAqDaVmmfNpNsyeSIdJa2sOyLxLXl/44/qmiontwcGm7s4PkERfjJoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Oqgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGlja7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoug4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdLjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQGgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC5AUFiAACPYgAAwpGAgIBRf0nsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3FGIAATZXUICAUX/iIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRBRiAADRV1CAUX+zVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCThRiAAEbV1BgARlRAFtgABlZYCABkIFSYCCQA2AAWZCBUoFSWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW2AAUVGQVltgIAFRUZBQg5JQgJFQUIBZkIFSWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2AAWZCBUoFSWWAgAZCBUmAgkANgA4FSgVKQUJBWW1BZUFBgAFFgAWAAUVEBWZCBUpBQYABSWZBWW1BQWVBQYgAAylaFMi4xLjAKuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOIjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFaCp5ih2eUv7YgqWcgZUha817lvlXq7gM/d4s24SywzJJ85AXQs="
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUK+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBZhU/AzYn1CLxSbLFtojZnRIyU/+tybxouZCcFqa305GAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKAuagASh9ngcYvnQKOFf/7V6cxWHawavZqRftgvkB5wer9gOFg=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhAWo6CLa/kAeWtpmfNrtL9Yq+pvBcvNX32lleycEHFEWhj6hqixU9P7hHsocBJ+mtGcpw0zLxzwNNvtAPUflcvBbkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FCvi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgLmoAEofZ4HGL50CjhX/+1enMVh2sGr2akX7YL5AecHp2hnbb"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUK+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBZhU/AzYn1CLxSbLFtojZnRIyU/+tybxouZCcFqa305GAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKAuagASh9ngcYvnQKOFf/7V6cxWHawavZqRftgvkB5wer9gOFg=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhACBLx5IhzgHeWwanM4XqQWLPyws2vfojMX/9YWb18jP2eV41fzAgeAxkHWPS6DXgROW0gKPwfWVGaaVXM0lZCCLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FCvi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgLmoAEofZ4HGL50CjhX/+1enMVh2sGr2akX7YL5AecHpIHhNp"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhACBLx5IhzgHeWwanM4XqQWLPyws2vfojMX/9YWb18jP2eV41fzAgeAxkHWPS6DXgROW0gKPwfWVGaaVXM0lZCCLhAWo6CLa/kAeWtpmfNrtL9Yq+pvBcvNX32lleycEHFEWhj6hqixU9P7hHsocBJ+mtGcpw0zLxzwNNvtAPUflcvBbkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FCvi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgLmoAEofZ4HGL50CjhX/+1enMVh2sGr2akX7YL5AecHrAQG1s"
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
    "state": "tx_+QGLCwH4hLhACBLx5IhzgHeWwanM4XqQWLPyws2vfojMX/9YWb18jP2eV41fzAgeAxkHWPS6DXgROW0gKPwfWVGaaVXM0lZCCLhAWo6CLa/kAeWtpmfNrtL9Yq+pvBcvNX32lleycEHFEWhj6hqixU9P7hHsocBJ+mtGcpw0zLxzwNNvtAPUflcvBbkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FCvi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgLmoAEofZ4HGL50CjhX/+1enMVh2sGr2akX7YL5AecHrAQG1s"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "dry_run",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "dry_run",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "dry_run",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "dry_run",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 11,
    "contract_id": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "gas_price": 1,
    "gas_used": 220,
    "height": 11,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
  },
  "tag": "call_contract",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": 10
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 10,
    "contract_id": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "gas_price": 1,
    "gas_used": 220,
    "height": 10,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": 10
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 10,
    "contract_id": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "gas_price": 1,
    "gas_used": 220,
    "height": 10,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUL+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBZhU/AzYn1CLxSbLFtojZnRIyU/+tybxouZCcFqa305GAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKBvK6nmW8DfMVCJ+2ANh/9sNGsLV4HbLvuCb4bdN1BGiq/FA0s=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhA82Cc821B3lNitOzbjT+00gjiOIVglClU8RZXH9DflKKse1zh3JVq78xDF1zbxj0JzzPlMXN6yUAOlbkvFNePDrkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FC/i2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgbyup5lvA3zFQiftgDYf/bDRrC1eB2y77gm+G3TdQRoqX0ufc"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUL+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBZhU/AzYn1CLxSbLFtojZnRIyU/+tybxouZCcFqa305GAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKBvK6nmW8DfMVCJ+2ANh/9sNGsLV4HbLvuCb4bdN1BGiq/FA0s=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhAVsdi9Qj97xijXKCaTGO9qRCe3kz5bwjltzOjekH7P84LO7mcyTXJqKrxAsJtBZxG1PTnZrtG1pX/XSo323aoB7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FC/i2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgbyup5lvA3zFQiftgDYf/bDRrC1eB2y77gm+G3TdQRopEmVxA"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAVsdi9Qj97xijXKCaTGO9qRCe3kz5bwjltzOjekH7P84LO7mcyTXJqKrxAsJtBZxG1PTnZrtG1pX/XSo323aoB7hA82Cc821B3lNitOzbjT+00gjiOIVglClU8RZXH9DflKKse1zh3JVq78xDF1zbxj0JzzPlMXN6yUAOlbkvFNePDrkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FC/i2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgbyup5lvA3zFQiftgDYf/bDRrC1eB2y77gm+G3TdQRopEt5QZ"
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
    "state": "tx_+QGLCwH4hLhAVsdi9Qj97xijXKCaTGO9qRCe3kz5bwjltzOjekH7P84LO7mcyTXJqKrxAsJtBZxG1PTnZrtG1pX/XSo323aoB7hA82Cc821B3lNitOzbjT+00gjiOIVglClU8RZXH9DflKKse1zh3JVq78xDF1zbxj0JzzPlMXN6yUAOlbkvFNePDrkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FC/i2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgbyup5lvA3zFQiftgDYf/bDRrC1eB2y77gm+G3TdQRopEt5QZ"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUM+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBZhU/AzYn1CLxSbLFtojZnRIyU/+tybxouZCcFqa305GAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKAWLbKlULFVJL4u9nMGGDXhf25RZqoK4WUfCcYej9J9VvV+vDc=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhAYgkwExwmFxhbGDJ/wZ6VLX0NHPFMGuRpMUWWybtzTLPxmrAuKSyH5+SBLUSvD21lcarDa4Nt+qZrxd1faPmaC7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FDPi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgFi2ypVCxVSS+LvZzBhg14X9uUWaqCuFlHwnGHo/SfVawGw/5"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUM+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBZhU/AzYn1CLxSbLFtojZnRIyU/+tybxouZCcFqa305GAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKAWLbKlULFVJL4u9nMGGDXhf25RZqoK4WUfCcYej9J9VvV+vDc=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhAfjBbV2F1xMCUecvvAdc1Ai7DesijV9FrNTdtMzlm+HyyhKFzWMCU+84fWPxHPAcXQ0tpmRd33ZREJh9ndlPPC7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FDPi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgFi2ypVCxVSS+LvZzBhg14X9uUWaqCuFlHwnGHo/SfVYWFnkF"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAYgkwExwmFxhbGDJ/wZ6VLX0NHPFMGuRpMUWWybtzTLPxmrAuKSyH5+SBLUSvD21lcarDa4Nt+qZrxd1faPmaC7hAfjBbV2F1xMCUecvvAdc1Ai7DesijV9FrNTdtMzlm+HyyhKFzWMCU+84fWPxHPAcXQ0tpmRd33ZREJh9ndlPPC7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FDPi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgFi2ypVCxVSS+LvZzBhg14X9uUWaqCuFlHwnGHo/SfVYuEcPa"
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
    "state": "tx_+QGLCwH4hLhAYgkwExwmFxhbGDJ/wZ6VLX0NHPFMGuRpMUWWybtzTLPxmrAuKSyH5+SBLUSvD21lcarDa4Nt+qZrxd1faPmaC7hAfjBbV2F1xMCUecvvAdc1Ai7DesijV9FrNTdtMzlm+HyyhKFzWMCU+84fWPxHPAcXQ0tpmRd33ZREJh9ndlPPC7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FDPi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgFi2ypVCxVSS+LvZzBhg14X9uUWaqCuFlHwnGHo/SfVYuEcPa"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUN+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBZhU/AzYn1CLxSbLFtojZnRIyU/+tybxouZCcFqa305GAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKAv2aEoTjc4OUr+hlRsrrOf12jYYjaDRbfbMf+qaB/0wv6FsHs=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhAPOSZbA9PBLgfbkwpLOPIBHIVHArmRy0MvLWf0pnNNBl7omwhUgavA1b53DGeYZvaHNPshfaUFVMxvDuDZ2OSB7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FDfi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgL9mhKE43ODlK/oZUbK6zn9do2GI2g0W32zH/qmgf9MLJ6B2V"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUN+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBZhU/AzYn1CLxSbLFtojZnRIyU/+tybxouZCcFqa305GAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKAv2aEoTjc4OUr+hlRsrrOf12jYYjaDRbfbMf+qaB/0wv6FsHs=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhA7auytYek2qKBHz6qStPitmSAVI0D3QHfxNl3p440nMbzI24U6P7Bc5zPZ6ahV9JILQEJpMGQ4KhDwVP8ywLRBLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FDfi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgL9mhKE43ODlK/oZUbK6zn9do2GI2g0W32zH/qmgf9MIwLGxh"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": 12
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAPOSZbA9PBLgfbkwpLOPIBHIVHArmRy0MvLWf0pnNNBl7omwhUgavA1b53DGeYZvaHNPshfaUFVMxvDuDZ2OSB7hA7auytYek2qKBHz6qStPitmSAVI0D3QHfxNl3p440nMbzI24U6P7Bc5zPZ6ahV9JILQEJpMGQ4KhDwVP8ywLRBLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FDfi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgL9mhKE43ODlK/oZUbK6zn9do2GI2g0W32zH/qmgf9MIxGf0b"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 12,
    "contract_id": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "gas_price": 1,
    "gas_used": 220,
    "height": 12,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAPOSZbA9PBLgfbkwpLOPIBHIVHArmRy0MvLWf0pnNNBl7omwhUgavA1b53DGeYZvaHNPshfaUFVMxvDuDZ2OSB7hA7auytYek2qKBHz6qStPitmSAVI0D3QHfxNl3p440nMbzI24U6P7Bc5zPZ6ahV9JILQEJpMGQ4KhDwVP8ywLRBLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FDfi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgL9mhKE43ODlK/oZUbK6zn9do2GI2g0W32zH/qmgf9MIxGf0b"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": 12
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 12,
    "contract_id": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "gas_price": 1,
    "gas_used": 220,
    "height": 12,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": 13
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 13,
    "contract_id": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "gas_price": 1,
    "gas_used": 220,
    "height": 13,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": 13
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 13,
    "contract_id": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "gas_price": 1,
    "gas_used": 220,
    "height": 13,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": 10
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 10,
    "contract_id": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "gas_price": 1,
    "gas_used": 220,
    "height": 10,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": 10
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 10,
    "contract_id": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "gas_price": 1,
    "gas_used": 220,
    "height": 10,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "clean_contract_calls"
}
```

#### initiator <--- node
```javascript
{
  "action": "calls_pruned",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": 10
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "call_not_found",
    "request": {
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "round": 10
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUO+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBZhU/AzYn1CLxSbLFtojZnRIyU/+tybxouZCcFqa305GAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKDwxoGINkWxjAJYlGXERVMiwXz7bK+QzqzDNQfCClXs8cQ1e+c=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhAv61ngIMRyemHwuF4/Z38278RZdjsNoO5XxlplmtB5nsXPA4BwK7emoiHCxq4D/fYUH74vyWS9cVExlqFJypWA7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FDvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg8MaBiDZFsYwCWJRlxEVTIsF8+2yvkM6swzUHwgpV7PGy4iES"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUO+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBZhU/AzYn1CLxSbLFtojZnRIyU/+tybxouZCcFqa305GAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKDwxoGINkWxjAJYlGXERVMiwXz7bK+QzqzDNQfCClXs8cQ1e+c=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhAhR+jOH+n60Egx71m29iLu/O3qGhDUciiQKrOzcxSIqKTnQ18c8nrN/t3o+ZJFVdqnS8Z0HSHUMj56X/0roKWC7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FDvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg8MaBiDZFsYwCWJRlxEVTIsF8+2yvkM6swzUHwgpV7PHtlziS"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAhR+jOH+n60Egx71m29iLu/O3qGhDUciiQKrOzcxSIqKTnQ18c8nrN/t3o+ZJFVdqnS8Z0HSHUMj56X/0roKWC7hAv61ngIMRyemHwuF4/Z38278RZdjsNoO5XxlplmtB5nsXPA4BwK7emoiHCxq4D/fYUH74vyWS9cVExlqFJypWA7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FDvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg8MaBiDZFsYwCWJRlxEVTIsF8+2yvkM6swzUHwgpV7PEQG73k"
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
    "state": "tx_+QGLCwH4hLhAhR+jOH+n60Egx71m29iLu/O3qGhDUciiQKrOzcxSIqKTnQ18c8nrN/t3o+ZJFVdqnS8Z0HSHUMj56X/0roKWC7hAv61ngIMRyemHwuF4/Z38278RZdjsNoO5XxlplmtB5nsXPA4BwK7emoiHCxq4D/fYUH74vyWS9cVExlqFJypWA7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FDvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg8MaBiDZFsYwCWJRlxEVTIsF8+2yvkM6swzUHwgpV7PEQG73k"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "dry_run",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "dry_run",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "dry_run",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "dry_run",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 15,
    "contract_id": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "gas_price": 1,
    "gas_used": 220,
    "height": 15,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
  },
  "tag": "call_contract",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": 14
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 14,
    "contract_id": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "gas_price": 1,
    "gas_used": 220,
    "height": 14,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": 14
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 14,
    "contract_id": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "gas_price": 1,
    "gas_used": 220,
    "height": 14,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUP+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBZhU/AzYn1CLxSbLFtojZnRIyU/+tybxouZCcFqa305GAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKCPHkutFz4h7Xa5QwlI33tkmXuywyxBCLTO0Rq/4ar+nFvUR9Q=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhAdnrzqdfOL/559Y8uKdAzlJ9wnni3laKBgveyYtADiYBJfxuOHFhojeH9A8v/+f/Esw2y4G1WkLQJP4zG4+C1ALkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FD/i2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgjx5LrRc+Ie12uUMJSN97ZJl7ssMsQQi0ztEav+Gq/pzWYJH9"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUP+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBZhU/AzYn1CLxSbLFtojZnRIyU/+tybxouZCcFqa305GAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKCPHkutFz4h7Xa5QwlI33tkmXuywyxBCLTO0Rq/4ar+nFvUR9Q=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhANx6klsM/B5qfHBH9dxZEP0E+wLOSZ1unhaz1/txCAfNSgG2jRHc7lZ0Xv82LqGEfCThMdYgBBVgmb4CnE9ucArkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FD/i2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgjx5LrRc+Ie12uUMJSN97ZJl7ssMsQQi0ztEav+Gq/pys+nf3"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhANx6klsM/B5qfHBH9dxZEP0E+wLOSZ1unhaz1/txCAfNSgG2jRHc7lZ0Xv82LqGEfCThMdYgBBVgmb4CnE9ucArhAdnrzqdfOL/559Y8uKdAzlJ9wnni3laKBgveyYtADiYBJfxuOHFhojeH9A8v/+f/Esw2y4G1WkLQJP4zG4+C1ALkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FD/i2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgjx5LrRc+Ie12uUMJSN97ZJl7ssMsQQi0ztEav+Gq/pz8d967"
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
    "state": "tx_+QGLCwH4hLhANx6klsM/B5qfHBH9dxZEP0E+wLOSZ1unhaz1/txCAfNSgG2jRHc7lZ0Xv82LqGEfCThMdYgBBVgmb4CnE9ucArhAdnrzqdfOL/559Y8uKdAzlJ9wnni3laKBgveyYtADiYBJfxuOHFhojeH9A8v/+f/Esw2y4G1WkLQJP4zG4+C1ALkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FD/i2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgjx5LrRc+Ie12uUMJSN97ZJl7ssMsQQi0ztEav+Gq/pz8d967"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUQ+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBZhU/AzYn1CLxSbLFtojZnRIyU/+tybxouZCcFqa305GAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKAZypUom+IULnil8Vk7s+0diTmCHL2NkNYMOdpwJ+ynXLKJ2bw=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhAxM+AvKXN09siTufbNK0HwaNZtFNLMYfvHHc3PC4FzKz5JcxVgaGYRdSFbT6JX+2EEkfMoqMf25Q8O9g7cJfXCrkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FEPi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgGcqVKJviFC54pfFZO7PtHYk5ghy9jZDWDDnacCfsp1w1pcTc"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUQ+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBZhU/AzYn1CLxSbLFtojZnRIyU/+tybxouZCcFqa305GAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKAZypUom+IULnil8Vk7s+0diTmCHL2NkNYMOdpwJ+ynXLKJ2bw=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhAulLbTSRHcbPtsf0nQfpCDZXY9wFne7IecMaGKDb6sfhFHZVCeT+F6IiVDAs2LAZ30c9a0XtUmHV+YCWNjNzAArkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FEPi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgGcqVKJviFC54pfFZO7PtHYk5ghy9jZDWDDnacCfsp1yuYS83"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAulLbTSRHcbPtsf0nQfpCDZXY9wFne7IecMaGKDb6sfhFHZVCeT+F6IiVDAs2LAZ30c9a0XtUmHV+YCWNjNzAArhAxM+AvKXN09siTufbNK0HwaNZtFNLMYfvHHc3PC4FzKz5JcxVgaGYRdSFbT6JX+2EEkfMoqMf25Q8O9g7cJfXCrkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FEPi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgGcqVKJviFC54pfFZO7PtHYk5ghy9jZDWDDnacCfsp1xJGkxC"
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
    "state": "tx_+QGLCwH4hLhAulLbTSRHcbPtsf0nQfpCDZXY9wFne7IecMaGKDb6sfhFHZVCeT+F6IiVDAs2LAZ30c9a0XtUmHV+YCWNjNzAArhAxM+AvKXN09siTufbNK0HwaNZtFNLMYfvHHc3PC4FzKz5JcxVgaGYRdSFbT6JX+2EEkfMoqMf25Q8O9g7cJfXCrkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FEPi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgGcqVKJviFC54pfFZO7PtHYk5ghy9jZDWDDnacCfsp1xJGkxC"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUR+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBZhU/AzYn1CLxSbLFtojZnRIyU/+tybxouZCcFqa305GAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKACYgN7Qe4khAx/cQ3w1cyb4F6V056oZv8XRH0gctZ+UgKj6IY=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhAubTaM1FqYuXfJetFcBphut9CEtYLxhrymZeI5bbkvGeM1O7+AyNOmKkfbwSpZdZfKfDvIcuUlRxD8GyxBglADrkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FEfi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgAmIDe0HuJIQMf3EN8NXMm+BeldOeqGb/F0R9IHLWflLJAsem"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUR+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBZhU/AzYn1CLxSbLFtojZnRIyU/+tybxouZCcFqa305GAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKACYgN7Qe4khAx/cQ3w1cyb4F6V056oZv8XRH0gctZ+UgKj6IY=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhAiXfQzQboEK6+OJeplNV/AygomJjnkQd2nOlNs1ShfiSWIeyERsKQjhw4U7Ph6hTffjxCO5N2bwBuoDF572A6CLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FEfi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgAmIDe0HuJIQMf3EN8NXMm+BeldOeqGb/F0R9IHLWflLag2g0"
  }
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": 16
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAiXfQzQboEK6+OJeplNV/AygomJjnkQd2nOlNs1ShfiSWIeyERsKQjhw4U7Ph6hTffjxCO5N2bwBuoDF572A6CLhAubTaM1FqYuXfJetFcBphut9CEtYLxhrymZeI5bbkvGeM1O7+AyNOmKkfbwSpZdZfKfDvIcuUlRxD8GyxBglADrkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FEfi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgAmIDe0HuJIQMf3EN8NXMm+BeldOeqGb/F0R9IHLWflLZ5inV"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 16,
    "contract_id": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "gas_price": 1,
    "gas_used": 220,
    "height": 16,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAiXfQzQboEK6+OJeplNV/AygomJjnkQd2nOlNs1ShfiSWIeyERsKQjhw4U7Ph6hTffjxCO5N2bwBuoDF572A6CLhAubTaM1FqYuXfJetFcBphut9CEtYLxhrymZeI5bbkvGeM1O7+AyNOmKkfbwSpZdZfKfDvIcuUlRxD8GyxBglADrkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FEfi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQWYVPwM2J9Qi8UmyxbaI2Z0SMlP/rcm8aLmQnBamt9ORgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgAmIDe0HuJIQMf3EN8NXMm+BeldOeqGb/F0R9IHLWflLZ5inV"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": 16
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 16,
    "contract_id": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "gas_price": 1,
    "gas_used": 220,
    "height": 16,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": 17
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 17,
    "contract_id": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "gas_price": 1,
    "gas_used": 220,
    "height": 17,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "round": 17
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 17,
    "contract_id": "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4",
    "gas_price": 1,
    "gas_used": 220,
    "height": 17,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
    ],
    "contracts": [
      "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
    ]
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "poi": "pi_+QuiPAH5Acr5Aceg6tTJ9RjLDI/UbBNjUQnVaxAUojMlnRKpj8EEIidkI0X5AaP4SaA7qbeS3rxB/J8g4Afw5dQcMqoJnugowv2UkveAHzo+5+egOFT8DNifUIvFJssW2iNmdEjJT/63JvGi5kJwWprfTkaFxAoBAAr4T6DK98MD3uitLxWPC69X5oiV3NFNWJTvS1nRZotGW3ofde2gMbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aLygoBAIY/qiUiX+v4tKDq1Mn1GMsMj9RsE2NRCdVrEBSiMyWdEqmPwQQiJ2QjRfiRgICAgICAoO0CFjxibIfdehu8wgGaVHmkULhlWpsI0fCWsUChDyMJgICgO6m3kt68QfyfIOAH8OXUHDKqCZ7oKML9lJL3gB86PueAoMr3wwPe6K0vFY8Lr1fmiJXc0U1YlO9LWdFmi0Zbeh91oKbKODEGFrja/tYvqk5+obVO1/o1hWepkepH5PQmYYvFgICAgPhPoO0CFjxibIfdehu8wgGaVHmkULhlWpsI0fCWsUChDyMJ7aA3HFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIvKCgEAhiRhOcqAAePioHsRa8E6J2zBDv77Fl1vJn+v6WipZaCkAF+QP9s5Ec7YwMD5Can5Caagp6pxt8H+vwKk33ySSeyaNvufQnGmRRnP7yHIFzDGrWD5CYL4ZqAVaiNPbxb1nROfE0C66bQnbZgclArLhJIVIS1S0xfBX/hDILhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF/hEoB3cqLle1ryvDXI00L62hGL8UKTN2Cnd3VxpFOi9gdiM4hCgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnen4dKBIER5XC7xxbur+BQq0j0FPtJBdjUer3LAh9f2Bgo7xRfhRoBVqI09vFvWdE58TQLrptCdtmByUCsuEkhUhLVLTF8FfoMMN5omVEejhhfhAqs9cOijYD5ArIrSxrLGPPIGxA0Z3gICAgICAgICAgICAgICA+QZBoGFzCYRTQqZXEZrM7LSgQssgEsGyZ3/o97u7DLqaC2kR+QYdgKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjICAgICAgICAgICAgICAuQXq+QXnKAGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmgwMAAbkFuPkFtUYCoNpWaZ82k2zJ5Ih0lraw7IvEteX/jj+qaKie3Bwabuzg+QRF+MmgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD46qCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNruGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///////////////////////////////////////////kCi6DiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRIRpbml0uMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC5AaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoUyLjEuMIABwAr4dKCnqnG3wf6/AqTffJJJ7Jo2+59CcaZFGc/vIcgXMMatYPhRgICAgICAgICAoOtVWdUq0Wv+YU41YUUdTqktiDMcZUw5phNrJbwyCSOjgICgxE4zJ+TR+w/Xqby7X1eYJoZLU7SL63nBtRQsDLxlTlOAgICA+Oagww3miZUR6OGF+ECqz1w6KNgPkCsitLGssY88gbEDRnf4wyC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPhToM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p8aBIER5XC7xxbur+BQq0j0FPtJBdjUer3LAh9f2Bgo7xRYCAgICAgICAgICAgICAgAD4ZaDrVVnVKtFr/mFONWFFHU6pLYgzHGVMOaYTayW8Mgkjo/hCoBhU/AzYn1CLxSbLFtojZnRIyU/+tybxouZCcFqa305GoGFzCYRTQqZXEZrM7LSgQssgEsGyZ3/o97u7DLqaC2kRwMBcyEDc"
  },
  "tag": "poi",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
    ],
    "contracts": [
      "ct_2A67iNjuNd2erJdzDMCzVeJkj82cS1krGGFbQeheBhFELktpo4"
    ]
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "poi": "pi_+QuiPAH5Acr5Aceg6tTJ9RjLDI/UbBNjUQnVaxAUojMlnRKpj8EEIidkI0X5AaP4SaA7qbeS3rxB/J8g4Afw5dQcMqoJnugowv2UkveAHzo+5+egOFT8DNifUIvFJssW2iNmdEjJT/63JvGi5kJwWprfTkaFxAoBAAr4T6DK98MD3uitLxWPC69X5oiV3NFNWJTvS1nRZotGW3ofde2gMbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aLygoBAIY/qiUiX+v4tKDq1Mn1GMsMj9RsE2NRCdVrEBSiMyWdEqmPwQQiJ2QjRfiRgICAgICAoO0CFjxibIfdehu8wgGaVHmkULhlWpsI0fCWsUChDyMJgICgO6m3kt68QfyfIOAH8OXUHDKqCZ7oKML9lJL3gB86PueAoMr3wwPe6K0vFY8Lr1fmiJXc0U1YlO9LWdFmi0Zbeh91oKbKODEGFrja/tYvqk5+obVO1/o1hWepkepH5PQmYYvFgICAgPhPoO0CFjxibIfdehu8wgGaVHmkULhlWpsI0fCWsUChDyMJ7aA3HFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIvKCgEAhiRhOcqAAePioHsRa8E6J2zBDv77Fl1vJn+v6WipZaCkAF+QP9s5Ec7YwMD5Can5Caagp6pxt8H+vwKk33ySSeyaNvufQnGmRRnP7yHIFzDGrWD5CYL4ZqAVaiNPbxb1nROfE0C66bQnbZgclArLhJIVIS1S0xfBX/hDILhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF/hEoB3cqLle1ryvDXI00L62hGL8UKTN2Cnd3VxpFOi9gdiM4hCgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnen4dKBIER5XC7xxbur+BQq0j0FPtJBdjUer3LAh9f2Bgo7xRfhRoBVqI09vFvWdE58TQLrptCdtmByUCsuEkhUhLVLTF8FfoMMN5omVEejhhfhAqs9cOijYD5ArIrSxrLGPPIGxA0Z3gICAgICAgICAgICAgICA+QZBoGFzCYRTQqZXEZrM7LSgQssgEsGyZ3/o97u7DLqaC2kR+QYdgKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjICAgICAgICAgICAgICAuQXq+QXnKAGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmgwMAAbkFuPkFtUYCoNpWaZ82k2zJ5Ih0lraw7IvEteX/jj+qaKie3Bwabuzg+QRF+MmgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD46qCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNruGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///////////////////////////////////////////kCi6DiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRIRpbml0uMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC5AaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoUyLjEuMIABwAr4dKCnqnG3wf6/AqTffJJJ7Jo2+59CcaZFGc/vIcgXMMatYPhRgICAgICAgICAoOtVWdUq0Wv+YU41YUUdTqktiDMcZUw5phNrJbwyCSOjgICgxE4zJ+TR+w/Xqby7X1eYJoZLU7SL63nBtRQsDLxlTlOAgICA+Oagww3miZUR6OGF+ECqz1w6KNgPkCsitLGssY88gbEDRnf4wyC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPhToM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p8aBIER5XC7xxbur+BQq0j0FPtJBdjUer3LAh9f2Bgo7xRYCAgICAgICAgICAgICAgAD4ZaDrVVnVKtFr/mFONWFFHU6pLYgzHGVMOaYTayW8Mgkjo/hCoBhU/AzYn1CLxSbLFtojZnRIyU/+tybxouZCcFqa305GoGFzCYRTQqZXEZrM7LSgQssgEsGyZ3/o97u7DLqaC2kRwMBcyEDc"
  },
  "tag": "poi",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: accounts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: contracts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: accounts, contracts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_found",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_found",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: accounts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: contracts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: accounts, contracts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_found",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_found",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAnHQYrA==",
    "code": "cb_+Q08RgKgnah8HG5i8Hcxgqfpf/YViaWsF9xn5gugEO9fcFC8+zj5CiP40aAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDItnZXRfYmFsYW5jZbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QGUoChhWzgmK00kF7owGlfTf0IXbL47tExEq9XJIHKPxqNpjXdpdGhkcmF3X2Zyb225ASAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AS6gR7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsiId2l0aGRyYXe4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPkB8aCJoaWWu46V2xUXMZ+Awz3MUZ7rpQAgWjmdn5mpfOadD4pzcGVuZF9mcm9tuQGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QGMoIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nhXNwZW5kuQEgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QHLoLnJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqhGluaXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////+QE0oNa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13jmdldF9iYWxhbmNlX29muMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC5AupiAAE7YgABW5GAgIBRf7nJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqFGIAAq9XUICAUX/Wv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdxRiAAGGV1CAgFF/KGFbOCYrTSQXujAaV9N/Qhdsvju0TESr1ckgco/Go2kUYgABmldQgIBRf0e3vKexm5ojL3PjvxoQ1lkZj3AJxG2zefBnFvmGfxrIFGIAArtXUICAUX+MC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpxRiAALOV1CAgFF/iaGllruOldsVFzGfgMM9zFGe66UAIFo5nZ+ZqXzmnQ8UYgACI1dQgFF/JSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwUYgACpldQYAEZUQBbYAAZWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW1lZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYAOBUoFSkFZbYCABUVGQUFlQgJFQUIAxkFCQVltgIAFRgFGQYCABUZFQWVCAgpJQklBQYABgAGAAg1mQgVJZYCABkIFSYCCQA39Ht7ynsZuaIy9z478aENZZGY9wCcRts3nwZxb5hn8ayIFSYACGWvFQgJFQUFszgZCRUFswMWAAYABgAIVZYCABkIFSYCCQA2ABgVKFYABa8VCBgQOQUJFQUJBWW2AgAVGAUZBgIAGAUZBgIAFRklBZUIGBhJNQk1CTUFBgAGAAYACDWZCBUllgIAGQgVJgIJADf0e3vKexm5ojL3PjvxoQ1lkZj3AJxG2zefBnFvmGfxrIgVJgAIda8VBgAGAAYACEWWAgAZCBUmAgkANgAYFShGAAWvFQgTGSUFBQkFZbUFlQUDAxkFZbUFCCkVBQYgABY1ZbYCABUVGQUFlQgJFQUGIAAfRWW2AgAVGAUZBgIAFRkVBZUICCklCSUFBiAAH6VoUyLjEuMFpia+4=",
    "deposit": 10,
    "vm_version": 3
  },
  "tag": "new_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_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AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPkBy6C5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6oRpbml0uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+5AUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///////////////////////////////////////////kBNKDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtd45nZXRfYmFsYW5jZV9vZrjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQLqYgABO2IAAVuRgICAUX+5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6hRiAAKvV1CAgFF/1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcUYgABhldQgIBRfyhhWzgmK00kF7owGlfTf0IXbL47tExEq9XJIHKPxqNpFGIAAZpXUICAUX9Ht7ynsZuaIy9z478aENZZGY9wCcRts3nwZxb5hn8ayBRiAAK7V1CAgFF/jAt2+/jT3WJAx/X8mmqIq5idH48B7FqmRC/tWic4jqcUYgACzldQgIBRf4mhpZa7jpXbFRcxn4DDPcxRnuulACBaOZ2fmal85p0PFGIAAiNXUIBRfyUk52A6qQ/AUHbqdi5s6si+bkOFHZWVHBXYWCmXOFkMFGIAAqZXUGABGVEAW2AAGVlgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tZWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2ADgVKBUpBWW2AgAVFRkFBZUICRUFCAMZBQkFZbYCABUYBRkGAgAVGRUFlQgIKSUJJQUGAAYABgAINZkIFSWWAgAZCBUmAgkAN/R7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsiBUmAAhlrxUICRUFBbM4GQkVBbMDFgAGAAYACFWWAgAZCBUmAgkANgAYFShWAAWvFQgYEDkFCRUFCQVltgIAFRgFGQYCABgFGQYCABUZJQWVCBgYSTUJNQk1BQYABgAGAAg1mQgVJZYCABkIFSYCCQA39Ht7ynsZuaIy9z478aENZZGY9wCcRts3nwZxb5hn8ayIFSYACHWvFQYABgAGAAhFlgIAGQgVJgIJADYAGBUoRgAFrxUIExklBQUJBWW1BZUFAwMZBWW1BQgpFQUGIAAWNWW2AgAVFRkFBZUICRUFBiAAH0VltgIAFRgFGQYCABUZFQWVCAgpJQklBQYgAB+laFMi4xLjAKuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILnJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgMn6/22UQbBOl9eVW5TShJMerazDAnXstSp2MZzvLvBn3XbRx",
    "updates": [
      {
        "abi_version": 1,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAnHQYrA==",
        "code": "cb_+Q08RgKgnah8HG5i8Hcxgqfpf/YViaWsF9xn5gugEO9fcFC8+zj5CiP40aAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDItnZXRfYmFsYW5jZbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QGUoChhWzgmK00kF7owGlfTf0IXbL47tExEq9XJIHKPxqNpjXdpdGhkcmF3X2Zyb225ASAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AS6gR7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsiId2l0aGRyYXe4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPkB8aCJoaWWu46V2xUXMZ+Awz3MUZ7rpQAgWjmdn5mpfOadD4pzcGVuZF9mcm9tuQGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QGMoIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nhXNwZW5kuQEgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QHLoLnJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqhGluaXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////+QE0oNa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13jmdldF9iYWxhbmNlX29muMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC5AupiAAE7YgABW5GAgIBRf7nJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqFGIAAq9XUICAUX/Wv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdxRiAAGGV1CAgFF/KGFbOCYrTSQXujAaV9N/Qhdsvju0TESr1ckgco/Go2kUYgABmldQgIBRf0e3vKexm5ojL3PjvxoQ1lkZj3AJxG2zefBnFvmGfxrIFGIAArtXUICAUX+MC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpxRiAALOV1CAgFF/iaGllruOldsVFzGfgMM9zFGe66UAIFo5nZ+ZqXzmnQ8UYgACI1dQgFF/JSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwUYgACpldQYAEZUQBbYAAZWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW1lZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYAOBUoFSkFZbYCABUVGQUFlQgJFQUIAxkFCQVltgIAFRgFGQYCABUZFQWVCAgpJQklBQYABgAGAAg1mQgVJZYCABkIFSYCCQA39Ht7ynsZuaIy9z478aENZZGY9wCcRts3nwZxb5hn8ayIFSYACGWvFQgJFQUFszgZCRUFswMWAAYABgAIVZYCABkIFSYCCQA2ABgVKFYABa8VCBgQOQUJFQUJBWW2AgAVGAUZBgIAGAUZBgIAFRklBZUIGBhJNQk1CTUFBgAGAAYACDWZCBUllgIAGQgVJgIJADf0e3vKexm5ojL3PjvxoQ1lkZj3AJxG2zefBnFvmGfxrIgVJgAIda8VBgAGAAYACEWWAgAZCBUmAgkANgAYFShGAAWvFQgTGSUFBQkFZbUFlQUDAxkFZbUFCCkVBQYgABY1ZbYCABUVGQUFlQgJFQUGIAAfRWW2AgAVGAUZBgIAFRkVBZUICCklCSUFBiAAH6VoUyLjEuMFpia+4=",
        "deposit": 10,
        "op": "OffChainNewContract",
        "owner": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "vm_version": 3
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
    "tx": "tx_+Q5qCwH4QrhAJqjYwe1wlcqrj7Ub3DKnJ1y5h9fPsrQJaqxqcgu2rPb6NiapOALSTGkLvlla5OkL5aSEHs1Ae8Tox0Lo0Qd6CLkOIfkOHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRL5DdW5DdL5Dc+CAj0BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoMDAAG5DT/5DTxGAqCdqHwcbmLwdzGCp+l/9hWJpawX3GfmC6AQ719wULz7OPkKI/jRoCUk52A6qQ/AUHbqdi5s6si+bkOFHZWVHBXYWCmXOFkMi2dldF9iYWxhbmNluGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AZSgKGFbOCYrTSQXujAaV9N/Qhdsvju0TESr1ckgco/Go2mNd2l0aGRyYXdfZnJvbbkBIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPkBLqBHt7ynsZuaIy9z478aENZZGY9wCcRts3nwZxb5hn8ayIh3aXRoZHJhd7jAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QHxoImhpZa7jpXbFRcxn4DDPcxRnuulACBaOZ2fmal85p0PinNwZW5kX2Zyb225AYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABYP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AYygjAt2+/jT3WJAx/X8mmqIq5idH48B7FqmRC/tWic4jqeFc3BlbmS5ASAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AcuguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeqEaW5pdLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5ATSg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXeOZ2V0X2JhbGFuY2Vfb2a4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkC6mIAATtiAAFbkYCAgFF/uclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoUYgACr1dQgIBRf9a/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13FGIAAYZXUICAUX8oYVs4JitNJBe6MBpX039CF2y+O7RMRKvVySByj8ajaRRiAAGaV1CAgFF/R7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsgUYgACu1dQgIBRf4wLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nFGIAAs5XUICAUX+JoaWWu46V2xUXMZ+Awz3MUZ7rpQAgWjmdn5mpfOadDxRiAAIjV1CAUX8lJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDBRiAAKmV1BgARlRAFtgABlZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbWVlgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgA4FSgVKQVltgIAFRUZBQWVCAkVBQgDGQUJBWW2AgAVGAUZBgIAFRkVBZUICCklCSUFBgAGAAYACDWZCBUllgIAGQgVJgIJADf0e3vKexm5ojL3PjvxoQ1lkZj3AJxG2zefBnFvmGfxrIgVJgAIZa8VCAkVBQWzOBkJFQWzAxYABgAGAAhVlgIAGQgVJgIJADYAGBUoVgAFrxUIGBA5BQkVBQkFZbYCABUYBRkGAgAYBRkGAgAVGSUFlQgYGEk1CTUJNQUGAAYABgAINZkIFSWWAgAZCBUmAgkAN/R7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsiBUmAAh1rxUGAAYABgAIRZYCABkIFSYCCQA2ABgVKEYABa8VCBMZJQUFCQVltQWVBQMDGQVltQUIKRUFBiAAFjVltgIAFRUZBQWVCAkVBQYgAB9FZbYCABUYBRkGAgAVGRUFlQgIKSUJJQUGIAAfpWhTIuMS4wCrhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoDJ+v9tlEGwTpfXlVuU0oSTHq2swwJ17LUqdjGc7y7wZtRotQw=="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_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AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPkBy6C5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6oRpbml0uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+5AUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///////////////////////////////////////////kBNKDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtd45nZXRfYmFsYW5jZV9vZrjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQLqYgABO2IAAVuRgICAUX+5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6hRiAAKvV1CAgFF/1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcUYgABhldQgIBRfyhhWzgmK00kF7owGlfTf0IXbL47tExEq9XJIHKPxqNpFGIAAZpXUICAUX9Ht7ynsZuaIy9z478aENZZGY9wCcRts3nwZxb5hn8ayBRiAAK7V1CAgFF/jAt2+/jT3WJAx/X8mmqIq5idH48B7FqmRC/tWic4jqcUYgACzldQgIBRf4mhpZa7jpXbFRcxn4DDPcxRnuulACBaOZ2fmal85p0PFGIAAiNXUIBRfyUk52A6qQ/AUHbqdi5s6si+bkOFHZWVHBXYWCmXOFkMFGIAAqZXUGABGVEAW2AAGVlgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tZWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2ADgVKBUpBWW2AgAVFRkFBZUICRUFCAMZBQkFZbYCABUYBRkGAgAVGRUFlQgIKSUJJQUGAAYABgAINZkIFSWWAgAZCBUmAgkAN/R7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsiBUmAAhlrxUICRUFBbM4GQkVBbMDFgAGAAYACFWWAgAZCBUmAgkANgAYFShWAAWvFQgYEDkFCRUFCQVltgIAFRgFGQYCABgFGQYCABUZJQWVCBgYSTUJNQk1BQYABgAGAAg1mQgVJZYCABkIFSYCCQA39Ht7ynsZuaIy9z478aENZZGY9wCcRts3nwZxb5hn8ayIFSYACHWvFQYABgAGAAhFlgIAGQgVJgIJADYAGBUoRgAFrxUIExklBQUJBWW1BZUFAwMZBWW1BQgpFQUGIAAWNWW2AgAVFRkFBZUICRUFBiAAH0VltgIAFRgFGQYCABUZFQWVCAgpJQklBQYgAB+laFMi4xLjAKuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILnJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgMn6/22UQbBOl9eVW5TShJMerazDAnXstSp2MZzvLvBn3XbRx",
    "updates": [
      {
        "abi_version": 1,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAnHQYrA==",
        "code": "cb_+Q08RgKgnah8HG5i8Hcxgqfpf/YViaWsF9xn5gugEO9fcFC8+zj5CiP40aAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDItnZXRfYmFsYW5jZbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QGUoChhWzgmK00kF7owGlfTf0IXbL47tExEq9XJIHKPxqNpjXdpdGhkcmF3X2Zyb225ASAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AS6gR7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsiId2l0aGRyYXe4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPkB8aCJoaWWu46V2xUXMZ+Awz3MUZ7rpQAgWjmdn5mpfOadD4pzcGVuZF9mcm9tuQGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QGMoIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nhXNwZW5kuQEgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QHLoLnJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqhGluaXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////+QE0oNa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13jmdldF9iYWxhbmNlX29muMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC5AupiAAE7YgABW5GAgIBRf7nJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqFGIAAq9XUICAUX/Wv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdxRiAAGGV1CAgFF/KGFbOCYrTSQXujAaV9N/Qhdsvju0TESr1ckgco/Go2kUYgABmldQgIBRf0e3vKexm5ojL3PjvxoQ1lkZj3AJxG2zefBnFvmGfxrIFGIAArtXUICAUX+MC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpxRiAALOV1CAgFF/iaGllruOldsVFzGfgMM9zFGe66UAIFo5nZ+ZqXzmnQ8UYgACI1dQgFF/JSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwUYgACpldQYAEZUQBbYAAZWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW1lZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYAOBUoFSkFZbYCABUVGQUFlQgJFQUIAxkFCQVltgIAFRgFGQYCABUZFQWVCAgpJQklBQYABgAGAAg1mQgVJZYCABkIFSYCCQA39Ht7ynsZuaIy9z478aENZZGY9wCcRts3nwZxb5hn8ayIFSYACGWvFQgJFQUFszgZCRUFswMWAAYABgAIVZYCABkIFSYCCQA2ABgVKFYABa8VCBgQOQUJFQUJBWW2AgAVGAUZBgIAGAUZBgIAFRklBZUIGBhJNQk1CTUFBgAGAAYACDWZCBUllgIAGQgVJgIJADf0e3vKexm5ojL3PjvxoQ1lkZj3AJxG2zefBnFvmGfxrIgVJgAIda8VBgAGAAYACEWWAgAZCBUmAgkANgAYFShGAAWvFQgTGSUFBQkFZbUFlQUDAxkFZbUFCCkVBQYgABY1ZbYCABUVGQUFlQgJFQUGIAAfRWW2AgAVGAUZBgIAFRkVBZUICCklCSUFBiAAH6VoUyLjEuMFpia+4=",
        "deposit": 10,
        "op": "OffChainNewContract",
        "owner": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "vm_version": 3
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_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AAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AcuguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeqEaW5pdLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5ATSg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXeOZ2V0X2JhbGFuY2Vfb2a4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkC6mIAATtiAAFbkYCAgFF/uclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoUYgACr1dQgIBRf9a/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13FGIAAYZXUICAUX8oYVs4JitNJBe6MBpX039CF2y+O7RMRKvVySByj8ajaRRiAAGaV1CAgFF/R7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsgUYgACu1dQgIBRf4wLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nFGIAAs5XUICAUX+JoaWWu46V2xUXMZ+Awz3MUZ7rpQAgWjmdn5mpfOadDxRiAAIjV1CAUX8lJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDBRiAAKmV1BgARlRAFtgABlZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbWVlgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgA4FSgVKQVltgIAFRUZBQWVCAkVBQgDGQUJBWW2AgAVGAUZBgIAFRkVBZUICCklCSUFBgAGAAYACDWZCBUllgIAGQgVJgIJADf0e3vKexm5ojL3PjvxoQ1lkZj3AJxG2zefBnFvmGfxrIgVJgAIZa8VCAkVBQWzOBkJFQWzAxYABgAGAAhVlgIAGQgVJgIJADYAGBUoVgAFrxUIGBA5BQkVBQkFZbYCABUYBRkGAgAYBRkGAgAVGSUFlQgYGEk1CTUJNQUGAAYABgAINZkIFSWWAgAZCBUmAgkAN/R7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsiBUmAAh1rxUGAAYABgAIRZYCABkIFSYCCQA2ABgVKEYABa8VCBMZJQUFCQVltQWVBQMDGQVltQUIKRUFBiAAFjVltgIAFRUZBQWVCAkVBQYgAB9FZbYCABUYBRkGAgAVGRUFlQgIKSUJJQUGIAAfpWhTIuMS4wCrhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoDJ+v9tlEGwTpfXlVuU0oSTHq2swwJ17LUqdjGc7y7wZtPUkPQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_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AAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AcuguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeqEaW5pdLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5ATSg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXeOZ2V0X2JhbGFuY2Vfb2a4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkC6mIAATtiAAFbkYCAgFF/uclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoUYgACr1dQgIBRf9a/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13FGIAAYZXUICAUX8oYVs4JitNJBe6MBpX039CF2y+O7RMRKvVySByj8ajaRRiAAGaV1CAgFF/R7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsgUYgACu1dQgIBRf4wLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nFGIAAs5XUICAUX+JoaWWu46V2xUXMZ+Awz3MUZ7rpQAgWjmdn5mpfOadDxRiAAIjV1CAUX8lJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDBRiAAKmV1BgARlRAFtgABlZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbWVlgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgA4FSgVKQVltgIAFRUZBQWVCAkVBQgDGQUJBWW2AgAVGAUZBgIAFRkVBZUICCklCSUFBgAGAAYACDWZCBUllgIAGQgVJgIJADf0e3vKexm5ojL3PjvxoQ1lkZj3AJxG2zefBnFvmGfxrIgVJgAIZa8VCAkVBQWzOBkJFQWzAxYABgAGAAhVlgIAGQgVJgIJADYAGBUoVgAFrxUIGBA5BQkVBQkFZbYCABUYBRkGAgAYBRkGAgAVGSUFlQgYGEk1CTUJNQUGAAYABgAINZkIFSWWAgAZCBUmAgkAN/R7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsiBUmAAh1rxUGAAYABgAIRZYCABkIFSYCCQA2ABgVKEYABa8VCBMZJQUFCQVltQWVBQMDGQVltQUIKRUFBiAAFjVltgIAFRUZBQWVCAkVBQYgAB9FZbYCABUYBRkGAgAVGRUFlQgIKSUJJQUGIAAfpWhTIuMS4wCrhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoDJ+v9tlEGwTpfXlVuU0oSTHq2swwJ17LUqdjGc7y7wZ0nYxRg=="
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
    "state": "tx_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AAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AcuguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeqEaW5pdLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5ATSg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXeOZ2V0X2JhbGFuY2Vfb2a4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkC6mIAATtiAAFbkYCAgFF/uclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoUYgACr1dQgIBRf9a/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13FGIAAYZXUICAUX8oYVs4JitNJBe6MBpX039CF2y+O7RMRKvVySByj8ajaRRiAAGaV1CAgFF/R7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsgUYgACu1dQgIBRf4wLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nFGIAAs5XUICAUX+JoaWWu46V2xUXMZ+Awz3MUZ7rpQAgWjmdn5mpfOadDxRiAAIjV1CAUX8lJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDBRiAAKmV1BgARlRAFtgABlZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbWVlgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgA4FSgVKQVltgIAFRUZBQWVCAkVBQgDGQUJBWW2AgAVGAUZBgIAFRkVBZUICCklCSUFBgAGAAYACDWZCBUllgIAGQgVJgIJADf0e3vKexm5ojL3PjvxoQ1lkZj3AJxG2zefBnFvmGfxrIgVJgAIZa8VCAkVBQWzOBkJFQWzAxYABgAGAAhVlgIAGQgVJgIJADYAGBUoVgAFrxUIGBA5BQkVBQkFZbYCABUYBRkGAgAYBRkGAgAVGSUFlQgYGEk1CTUJNQUGAAYABgAINZkIFSWWAgAZCBUmAgkAN/R7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsiBUmAAh1rxUGAAYABgAIRZYCABkIFSYCCQA2ABgVKEYABa8VCBMZJQUFCQVltQWVBQMDGQVltQUIKRUFBiAAFjVltgIAFRUZBQWVCAkVBQYgAB9FZbYCABUYBRkGAgAVGRUFlQgIKSUJJQUGIAAfpWhTIuMS4wCrhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoDJ+v9tlEGwTpfXlVuU0oSTHq2swwJ17LUqdjGc7y7wZ0nYxRg=="
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUT+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBfqAMT8CGqxIJ6ug4WvHgYACBijRyJ5nYMnCddGri9GFAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKDrTrKgzdumUjmBGYKOHsVE7eR/rJ8qzc41ehVmUAvSbt0+GJo=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhAA5x45HCAX60uWSVyi4c3E5rwQTWVZ1WRA8f02lZsGxnKrQ2N58rgEdrz+7Y1ACBGYk7kI4f8hmo/9QUAbGgAA7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FE/i2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg606yoM3bplI5gRmCjh7FRO3kf6yfKs3ONXoVZlAL0m63m4PU"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUT+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBfqAMT8CGqxIJ6ug4WvHgYACBijRyJ5nYMnCddGri9GFAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKDrTrKgzdumUjmBGYKOHsVE7eR/rJ8qzc41ehVmUAvSbt0+GJo=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhA7uVMbiPvlq+F0E6VAMfORHiCU/c9Dlq52+1bePhh31XxGiLHNrsGV/LXkhLaugNuHKCxm9KW3w+n0TryosYTDLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FE/i2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg606yoM3bplI5gRmCjh7FRO3kf6yfKs3ONXoVZlAL0m7+C8NY"
  }
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 19
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAA5x45HCAX60uWSVyi4c3E5rwQTWVZ1WRA8f02lZsGxnKrQ2N58rgEdrz+7Y1ACBGYk7kI4f8hmo/9QUAbGgAA7hA7uVMbiPvlq+F0E6VAMfORHiCU/c9Dlq52+1bePhh31XxGiLHNrsGV/LXkhLaugNuHKCxm9KW3w+n0TryosYTDLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FE/i2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg606yoM3bplI5gRmCjh7FRO3kf6yfKs3ONXoVZlAL0m6TsLp0"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 19,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 718,
    "height": 19,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAqAOOdZ"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAA5x45HCAX60uWSVyi4c3E5rwQTWVZ1WRA8f02lZsGxnKrQ2N58rgEdrz+7Y1ACBGYk7kI4f8hmo/9QUAbGgAA7hA7uVMbiPvlq+F0E6VAMfORHiCU/c9Dlq52+1bePhh31XxGiLHNrsGV/LXkhLaugNuHKCxm9KW3w+n0TryosYTDLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FE/i2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg606yoM3bplI5gRmCjh7FRO3kf6yfKs3ONXoVZlAL0m6TsLp0"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 19
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 19,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 718,
    "height": 19,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAqAOOdZ"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FFPjWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmwKCTuBGKR77/BGo3F8TZskjmIqH5PgUm84X3wfUM8wRvFZaZDco=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhACPoF9oOmkH/rYo3v+EmgMXVgvO6P/pS3xiiNUKm8cjEN70C/BpU2OMzg8rdopdmRs7swyUGDb4svhEToBtQyA7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRT41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgk7gRike+/wRqNxfE2bJI5iKh+T4FJvOF98H1DPMEbxVSTTM7"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FFPjWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmwKCTuBGKR77/BGo3F8TZskjmIqH5PgUm84X3wfUM8wRvFZaZDco=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhAuQ59WzFB5snwh/QszToTOKSlOwgHiN5lBzuXHb0g/lw697gltqO9CbL+w0pugFXkq49SrQA6yjjVPlXA2RFJBbkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRT41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgk7gRike+/wRqNxfE2bJI5iKh+T4FJvOF98H1DPMEbxWbJhY1"
  }
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 20
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhACPoF9oOmkH/rYo3v+EmgMXVgvO6P/pS3xiiNUKm8cjEN70C/BpU2OMzg8rdopdmRs7swyUGDb4svhEToBtQyA7hAuQ59WzFB5snwh/QszToTOKSlOwgHiN5lBzuXHb0g/lw697gltqO9CbL+w0pugFXkq49SrQA6yjjVPlXA2RFJBbkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRT41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgk7gRike+/wRqNxfE2bJI5iKh+T4FJvOF98H1DPMEbxVBQuEW"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 20,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 600,
    "height": 20,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/qiUiX+EhHPBI"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 20
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhACPoF9oOmkH/rYo3v+EmgMXVgvO6P/pS3xiiNUKm8cjEN70C/BpU2OMzg8rdopdmRs7swyUGDb4svhEToBtQyA7hAuQ59WzFB5snwh/QszToTOKSlOwgHiN5lBzuXHb0g/lw697gltqO9CbL+w0pugFXkq49SrQA6yjjVPlXA2RFJBbkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRT41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgk7gRike+/wRqNxfE2bJI5iKh+T4FJvOF98H1DPMEbxVBQuEW"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 20,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 600,
    "height": 20,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/qiUiX+EhHPBI"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FFfjWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EwKDrDJhnZZc48xf0ihZZ7WxE4aNDO+HUikxZCmugIp5t7d8ZkZk=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhAR1tyT17Q1sTLnOPSDNukkgV0K4bRN7Xt7mxQO/2ufWkkYVuWfyqO0O7KR3DPNErAGxM3oVoa3ofhTSC/nPiGCrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRX41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCg6wyYZ2WXOPMX9IoWWe1sROGjQzvh1IpMWQproCKebe2vk+iB"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FFfjWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EwKDrDJhnZZc48xf0ihZZ7WxE4aNDO+HUikxZCmugIp5t7d8ZkZk=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhAWTwfulBi6sqNTJlJ0/Dj8XNhQCBVlkjDITMiO3QHq7L9lCrwX20upYTN1N7d2BmYLG/Z7n4wBeisGFsZ1GJ7BrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRX41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCg6wyYZ2WXOPMX9IoWWe1sROGjQzvh1IpMWQproCKebe141vIV"
  }
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 21
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAR1tyT17Q1sTLnOPSDNukkgV0K4bRN7Xt7mxQO/2ufWkkYVuWfyqO0O7KR3DPNErAGxM3oVoa3ofhTSC/nPiGCrhAWTwfulBi6sqNTJlJ0/Dj8XNhQCBVlkjDITMiO3QHq7L9lCrwX20upYTN1N7d2BmYLG/Z7n4wBeisGFsZ1GJ7BrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRX41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCg6wyYZ2WXOPMX9IoWWe1sROGjQzvh1IpMWQproCKebe3quzHi"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 21,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 600,
    "height": 21,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkYTnKgAE9XpJ4"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAR1tyT17Q1sTLnOPSDNukkgV0K4bRN7Xt7mxQO/2ufWkkYVuWfyqO0O7KR3DPNErAGxM3oVoa3ofhTSC/nPiGCrhAWTwfulBi6sqNTJlJ0/Dj8XNhQCBVlkjDITMiO3QHq7L9lCrwX20upYTN1N7d2BmYLG/Z7n4wBeisGFsZ1GJ7BrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRX41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCg6wyYZ2WXOPMX9IoWWe1sROGjQzvh1IpMWQproCKebe3quzHi"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 21
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 21,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 600,
    "height": 21,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkYTnKgAE9XpJ4"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5ceuTo=",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5ceuTo=",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5ceuTo=",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5ceuTo=",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5ceuTo=",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QE+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FFvj2uPT48oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgjAt2+/jT3WJAx/X8mmqIq5idH48B7FqmRC/tWic4jqcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPAoFRU0hMJT9Yu5D6VlgEPQhnQz77yOUarXKocuu/JJ84jsirGfA==",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5ceuTo=",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QGKCwH4QrhAkkw7S04VVltQ17OFSoBnqxxBll16DoKw8R751N7LWT9ZFZ5KxNS4l36ymC8MrBEL7MkyVwLu4ZQemtTqqcmAB7kBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRb49rj0+PKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwKBUVNITCU/WLuQ+lZYBD0IZ0M++8jlGq1yqHLrvySfOI1PKn54="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QE+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FFvj2uPT48oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgjAt2+/jT3WJAx/X8mmqIq5idH48B7FqmRC/tWic4jqcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPAoFRU0hMJT9Yu5D6VlgEPQhnQz77yOUarXKocuu/JJ84jsirGfA==",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5ceuTo=",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QGKCwH4QrhASvhTNhBSsK48zSB7+0zsLY8ubRYH4rQ1tgVK528MGUyaUl+xFj6MoLP4x7rBEJ23Dy8UW22bkDZBQ4Vmr6HiCbkBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRb49rj0+PKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwKBUVNITCU/WLuQ+lZYBD0IZ0M++8jlGq1yqHLrvySfOI4C47a0="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QHMCwH4hLhASvhTNhBSsK48zSB7+0zsLY8ubRYH4rQ1tgVK528MGUyaUl+xFj6MoLP4x7rBEJ23Dy8UW22bkDZBQ4Vmr6HiCbhAkkw7S04VVltQ17OFSoBnqxxBll16DoKw8R751N7LWT9ZFZ5KxNS4l36ymC8MrBEL7MkyVwLu4ZQemtTqqcmAB7kBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRb49rj0+PKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwKBUVNITCU/WLuQ+lZYBD0IZ0M++8jlGq1yqHLrvySfOI3pXchI="
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
    "state": "tx_+QHMCwH4hLhASvhTNhBSsK48zSB7+0zsLY8ubRYH4rQ1tgVK528MGUyaUl+xFj6MoLP4x7rBEJ23Dy8UW22bkDZBQ4Vmr6HiCbhAkkw7S04VVltQ17OFSoBnqxxBll16DoKw8R751N7LWT9ZFZ5KxNS4l36ymC8MrBEL7MkyVwLu4ZQemtTqqcmAB7kBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRb49rj0+PKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwKBUVNITCU/WLuQ+lZYBD0IZ0M++8jlGq1yqHLrvySfOI3pXchI="
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUX+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBfqAMT8CGqxIJ6ug4WvHgYACBijRyJ5nYMnCddGri9GFAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKBNxs27j6SY7WqIMKckiZwKCdfFzGc7NJmAcL9VcY9/rMpJ8HI=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhAyOVwpPaIaewlGOaMmljcyH5CMdhicJFCk+osRsJEt8cuBHGQF9Y8/80L8PA7zr8TZdcfHBFqQi7ok/vH54WLDrkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FF/i2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgTcbNu4+kmO1qiDCnJImcCgnXxcxnOzSZgHC/VXGPf6wRT0c3"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUX+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBfqAMT8CGqxIJ6ug4WvHgYACBijRyJ5nYMnCddGri9GFAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKBNxs27j6SY7WqIMKckiZwKCdfFzGc7NJmAcL9VcY9/rMpJ8HI=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhAoZCznA2Eb32xj/pdIqlWGyCEy0TkFekLerd+K5GvUA+2PLCD4qx+PGnCP4mOpsqTDf+WX+apHtkmA7zijQr1B7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FF/i2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgTcbNu4+kmO1qiDCnJImcCgnXxcxnOzSZgHC/VXGPf6yV+Oxo"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 23
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAoZCznA2Eb32xj/pdIqlWGyCEy0TkFekLerd+K5GvUA+2PLCD4qx+PGnCP4mOpsqTDf+WX+apHtkmA7zijQr1B7hAyOVwpPaIaewlGOaMmljcyH5CMdhicJFCk+osRsJEt8cuBHGQF9Y8/80L8PA7zr8TZdcfHBFqQi7ok/vH54WLDrkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FF/i2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgTcbNu4+kmO1qiDCnJImcCgnXxcxnOzSZgHC/VXGPf6wPwoo1"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 23,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 718,
    "height": 23,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAfn8n3G"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAoZCznA2Eb32xj/pdIqlWGyCEy0TkFekLerd+K5GvUA+2PLCD4qx+PGnCP4mOpsqTDf+WX+apHtkmA7zijQr1B7hAyOVwpPaIaewlGOaMmljcyH5CMdhicJFCk+osRsJEt8cuBHGQF9Y8/80L8PA7zr8TZdcfHBFqQi7ok/vH54WLDrkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FF/i2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgTcbNu4+kmO1qiDCnJImcCgnXxcxnOzSZgHC/VXGPf6wPwoo1"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 23
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 23,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 718,
    "height": 23,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAfn8n3G"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FGPjWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmwKBYB/doKYOo2FvnXvG0PpUuPQkS4iUSe2NfpNatTsyyRSuUrE8=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhAfsncYURY68awI3OCruwwwdXXkBjGV5MZ/ycC7uePhdz7StL6iqsJO5b5M4GO1c373l70uuYRZZz3tZWieFjcBrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRj41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgWAf3aCmDqNhb517xtD6VLj0JEuIlEntjX6TWrU7MskXULPsX"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FGPjWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmwKBYB/doKYOo2FvnXvG0PpUuPQkS4iUSe2NfpNatTsyyRSuUrE8=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhARqA0m53lkwYXS+qppW+bW6P55+fQHjft3vQEX6v9g6KcNRdyUICuGBaNogjr0jGEBJRz4q0pSAkb/ArSs9CaD7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRj41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgWAf3aCmDqNhb517xtD6VLj0JEuIlEntjX6TWrU7MskVFGyq0"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 24
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhARqA0m53lkwYXS+qppW+bW6P55+fQHjft3vQEX6v9g6KcNRdyUICuGBaNogjr0jGEBJRz4q0pSAkb/ArSs9CaD7hAfsncYURY68awI3OCruwwwdXXkBjGV5MZ/ycC7uePhdz7StL6iqsJO5b5M4GO1c373l70uuYRZZz3tZWieFjcBrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRj41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgWAf3aCmDqNhb517xtD6VLj0JEuIlEntjX6TWrU7MskVF817H"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 24,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 600,
    "height": 24,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/qiUiX+TWYF0W"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhARqA0m53lkwYXS+qppW+bW6P55+fQHjft3vQEX6v9g6KcNRdyUICuGBaNogjr0jGEBJRz4q0pSAkb/ArSs9CaD7hAfsncYURY68awI3OCruwwwdXXkBjGV5MZ/ycC7uePhdz7StL6iqsJO5b5M4GO1c373l70uuYRZZz3tZWieFjcBrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRj41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgWAf3aCmDqNhb517xtD6VLj0JEuIlEntjX6TWrU7MskVF817H"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 24
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 24,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 600,
    "height": 24,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/qiUiX+TWYF0W"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FGfjWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EwKAQJsunV5m5qz/6zdyd1lkWW1ObAKwo4TtM/VCSKiTOQ49s/8U=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhAL9L/CplOxfFDautLiNWoDpvvfUToPGvbxONN01ibTqB4um1EyvVxMYnvlbWIsJVzyK7ocDteQ3DOW33YXrGvA7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRn41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgECbLp1eZuas/+s3cndZZFltTmwCsKOE7TP1QkiokzkPRpJk5"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FGfjWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EwKAQJsunV5m5qz/6zdyd1lkWW1ObAKwo4TtM/VCSKiTOQ49s/8U=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhAsN0mCKIO1DJnyKRQMcMKZLtv0X5QyOTwSqfq6oONbqOKQcvx24m0TPd3ctIErB10hMiQweVeFs9TrWcKNQwbDbkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRn41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgECbLp1eZuas/+s3cndZZFltTmwCsKOE7TP1QkiokzkPpz8m7"
  }
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 25
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAL9L/CplOxfFDautLiNWoDpvvfUToPGvbxONN01ibTqB4um1EyvVxMYnvlbWIsJVzyK7ocDteQ3DOW33YXrGvA7hAsN0mCKIO1DJnyKRQMcMKZLtv0X5QyOTwSqfq6oONbqOKQcvx24m0TPd3ctIErB10hMiQweVeFs9TrWcKNQwbDbkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRn41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgECbLp1eZuas/+s3cndZZFltTmwCsKOE7TP1QkiokzkP/WQhN"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 25,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 600,
    "height": 25,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkYTnKgAE9XpJ4"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 25
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAL9L/CplOxfFDautLiNWoDpvvfUToPGvbxONN01ibTqB4um1EyvVxMYnvlbWIsJVzyK7ocDteQ3DOW33YXrGvA7hAsN0mCKIO1DJnyKRQMcMKZLtv0X5QyOTwSqfq6oONbqOKQcvx24m0TPd3ctIErB10hMiQweVeFs9TrWcKNQwbDbkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRn41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgECbLp1eZuas/+s3cndZZFltTmwCsKOE7TP1QkiokzkP/WQhN"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 25,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 600,
    "height": 25,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkYTnKgAE9XpJ4"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv71OkQ=",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv71OkQ=",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv71OkQ=",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv71OkQ=",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv71OkQ=",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QE+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FGvj2uPT48oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgjAt2+/jT3WJAx/X8mmqIq5idH48B7FqmRC/tWic4jqcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALAoGlc3iXNajTUHcqlBDmE50K1z18+svGHnN0nVXnyOcvT/wrgLg==",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv71OkQ=",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QGKCwH4QrhAwPXI4+xkU5xeywLiwTBmzPv8Cux1orpPvmCBSJsP6KxDQaQ/wHtVUmY+6QDlHqmMEIBJQFzjQIlbrzP7Kdh2BbkBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRr49rj0+PKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwKBpXN4lzWo01B3KpQQ5hOdCtc9fPrLxh5zdJ1V58jnL04hNefU="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QE+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FGvj2uPT48oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgjAt2+/jT3WJAx/X8mmqIq5idH48B7FqmRC/tWic4jqcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALAoGlc3iXNajTUHcqlBDmE50K1z18+svGHnN0nVXnyOcvT/wrgLg==",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv71OkQ=",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QGKCwH4QrhAEKEpu9lzqRhKs9eCkNp4m8/jYnr4psoZLhDFHzi9fCYOZsz+anFmnHFCOYzkao/XvlSFxpp/NN3caAkLKI5tA7kBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRr49rj0+PKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwKBpXN4lzWo01B3KpQQ5hOdCtc9fPrLxh5zdJ1V58jnL0wsTMls="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QHMCwH4hLhAEKEpu9lzqRhKs9eCkNp4m8/jYnr4psoZLhDFHzi9fCYOZsz+anFmnHFCOYzkao/XvlSFxpp/NN3caAkLKI5tA7hAwPXI4+xkU5xeywLiwTBmzPv8Cux1orpPvmCBSJsP6KxDQaQ/wHtVUmY+6QDlHqmMEIBJQFzjQIlbrzP7Kdh2BbkBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRr49rj0+PKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwKBpXN4lzWo01B3KpQQ5hOdCtc9fPrLxh5zdJ1V58jnL01cs0UE="
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
    "state": "tx_+QHMCwH4hLhAEKEpu9lzqRhKs9eCkNp4m8/jYnr4psoZLhDFHzi9fCYOZsz+anFmnHFCOYzkao/XvlSFxpp/NN3caAkLKI5tA7hAwPXI4+xkU5xeywLiwTBmzPv8Cux1orpPvmCBSJsP6KxDQaQ/wHtVUmY+6QDlHqmMEIBJQFzjQIlbrzP7Kdh2BbkBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRr49rj0+PKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwKBpXN4lzWo01B3KpQQ5hOdCtc9fPrLxh5zdJ1V58jnL01cs0UE="
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUb+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBfqAMT8CGqxIJ6ug4WvHgYACBijRyJ5nYMnCddGri9GFAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKDvtDHiUS9zD5pD+BVD7gsSy8Ph1Tgr/W6SPrvFpPnGUmUyBFU=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhAsVhyJTkDgLd2KBywvvG0WbicvHiPOwcJyV0lCwp+w5/UzW6GA0Zt6bJaye8a5n3VytRjMBSz/nSC9HYQFGk1BLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FG/i2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg77Qx4lEvcw+aQ/gVQ+4LEsvD4dU4K/1ukj67xaT5xlJK6cBg"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUb+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBfqAMT8CGqxIJ6ug4WvHgYACBijRyJ5nYMnCddGri9GFAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKDvtDHiUS9zD5pD+BVD7gsSy8Ph1Tgr/W6SPrvFpPnGUmUyBFU=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhA4PGIZ/eCSZeWmkcfv4jzjD4ym0SCgH6dtb0zFy3bE7ZRs1g1FBsc/wa2kEl2Oov72jHt4pLzCG8vKIIJ80sQBLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FG/i2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg77Qx4lEvcw+aQ/gVQ+4LEsvD4dU4K/1ukj67xaT5xlLO1pRl"
  }
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 27
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAsVhyJTkDgLd2KBywvvG0WbicvHiPOwcJyV0lCwp+w5/UzW6GA0Zt6bJaye8a5n3VytRjMBSz/nSC9HYQFGk1BLhA4PGIZ/eCSZeWmkcfv4jzjD4ym0SCgH6dtb0zFy3bE7ZRs1g1FBsc/wa2kEl2Oov72jHt4pLzCG8vKIIJ80sQBLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FG/i2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg77Qx4lEvcw+aQ/gVQ+4LEsvD4dU4K/1ukj67xaT5xlI3yvvr"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 27,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 718,
    "height": 27,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUTF3JV"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
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
    "state": "tx_+QGLCwH4hLhAsVhyJTkDgLd2KBywvvG0WbicvHiPOwcJyV0lCwp+w5/UzW6GA0Zt6bJaye8a5n3VytRjMBSz/nSC9HYQFGk1BLhA4PGIZ/eCSZeWmkcfv4jzjD4ym0SCgH6dtb0zFy3bE7ZRs1g1FBsc/wa2kEl2Oov72jHt4pLzCG8vKIIJ80sQBLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FG/i2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg77Qx4lEvcw+aQ/gVQ+4LEsvD4dU4K/1ukj67xaT5xlI3yvvr"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 27
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 27,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 718,
    "height": 27,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUTF3JV"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FHPjWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmwKBdGcxHER9FsJLo63xc4JkiUT7DItVNCxUgy/gTs9lyV8unQF4=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhA2uHFkqGymOpQiITAIHWYH6O9haRSNCf75LH2vK0mTNBJRzBhFfKzLV3gibrvNL98SqTWXpiJI5NptMojQo16ALkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRz41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgXRnMRxEfRbCS6Ot8XOCZIlE+wyLVTQsVIMv4E7PZclf/2TPY"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FHPjWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmwKBdGcxHER9FsJLo63xc4JkiUT7DItVNCxUgy/gTs9lyV8unQF4=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhAYNCXkxKOMmkX+Su/r9++c9sdfiUhhDa86Xhz7eYHyRHtltlaJDH6NR6jZElLuLm5ljKGHxA95CO03LhcHfn8ArkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRz41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgXRnMRxEfRbCS6Ot8XOCZIlE+wyLVTQsVIMv4E7PZcld2ed4P"
  }
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 28
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAYNCXkxKOMmkX+Su/r9++c9sdfiUhhDa86Xhz7eYHyRHtltlaJDH6NR6jZElLuLm5ljKGHxA95CO03LhcHfn8ArhA2uHFkqGymOpQiITAIHWYH6O9haRSNCf75LH2vK0mTNBJRzBhFfKzLV3gibrvNL98SqTWXpiJI5NptMojQo16ALkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRz41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgXRnMRxEfRbCS6Ot8XOCZIlE+wyLVTQsVIMv4E7PZcleldxCu"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 28,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 600,
    "height": 28,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/qiUiX+TWYF0W"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
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
    "state": "tx_+QGsCwH4hLhAYNCXkxKOMmkX+Su/r9++c9sdfiUhhDa86Xhz7eYHyRHtltlaJDH6NR6jZElLuLm5ljKGHxA95CO03LhcHfn8ArhA2uHFkqGymOpQiITAIHWYH6O9haRSNCf75LH2vK0mTNBJRzBhFfKzLV3gibrvNL98SqTWXpiJI5NptMojQo16ALkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBRz41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgXRnMRxEfRbCS6Ot8XOCZIlE+wyLVTQsVIMv4E7PZcleldxCu"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 28
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 28,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 600,
    "height": 28,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/qiUiX+TWYF0W"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FHfjWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EwKBg3HyGOK/6Mxk6dH0T+06hmlSoDzHLtjBiU2h1QM7CHXWRH7I=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhA/aE0rHQ/w6k8zywbzQ7FUSh/Si7OfbGkAGbm/vMmGYQ0PzCj9teKYvf1BqL8LYGS7YlrN6O5glxozPpNd9d2BrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBR341rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgYNx8hjiv+jMZOnR9E/tOoZpUqA8xy7YwYlNodUDOwh2QuXh8"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FHfjWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EwKBg3HyGOK/6Mxk6dH0T+06hmlSoDzHLtjBiU2h1QM7CHXWRH7I=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhAxvA9uobO+T+56gvBkwidtlKYxoA/oGe2G4YxZzlU6TKR4yXmU+KVQI3O2rvegSQM330RFwoBPKXLbEEv1uAZA7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBR341rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgYNx8hjiv+jMZOnR9E/tOoZpUqA8xy7YwYlNodUDOwh0q/W2s"
  }
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
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
    "state": "tx_+QGsCwH4hLhAxvA9uobO+T+56gvBkwidtlKYxoA/oGe2G4YxZzlU6TKR4yXmU+KVQI3O2rvegSQM330RFwoBPKXLbEEv1uAZA7hA/aE0rHQ/w6k8zywbzQ7FUSh/Si7OfbGkAGbm/vMmGYQ0PzCj9teKYvf1BqL8LYGS7YlrN6O5glxozPpNd9d2BrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBR341rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgYNx8hjiv+jMZOnR9E/tOoZpUqA8xy7YwYlNodUDOwh3EY2ie"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 29
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 29,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 600,
    "height": 29,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkYTnKgAOLHGSX"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAxvA9uobO+T+56gvBkwidtlKYxoA/oGe2G4YxZzlU6TKR4yXmU+KVQI3O2rvegSQM330RFwoBPKXLbEEv1uAZA7hA/aE0rHQ/w6k8zywbzQ7FUSh/Si7OfbGkAGbm/vMmGYQ0PzCj9teKYvf1BqL8LYGS7YlrN6O5glxozPpNd9d2BrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBR341rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgYNx8hjiv+jMZOnR9E/tOoZpUqA8xy7YwYlNodUDOwh3EY2ie"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 29
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 29,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 600,
    "height": 29,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkYTnKgAOLHGSX"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 26
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 26,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 22521,
    "height": 26,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUTF3JV"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 26
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 26,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 22521,
    "height": 26,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUTF3JV"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "clean_contract_calls"
}
```

#### initiator <--- node
```javascript
{
  "action": "calls_pruned",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 26
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "call_not_found",
    "request": {
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": 26
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUe+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBfqAMT8CGqxIJ6ug4WvHgYACBijRyJ5nYMnCddGri9GFAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKChmgGJ0RkFr86LpUGbDWXtK2DRzkYBy+Hb5PflbkTqpv6BRP0=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhAd1PuJl86UMrf2uhFxc+yiQuajZiqzcoM50hm9j+54r1z8Hku6oSepEiykN9gi1CPnga2nwjPab0+rlZiZKtOA7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FHvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgoZoBidEZBa/Oi6VBmw1l7Stg0c5GAcvh2+T35W5E6qZr1Z2L"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUe+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBfqAMT8CGqxIJ6ug4WvHgYACBijRyJ5nYMnCddGri9GFAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKChmgGJ0RkFr86LpUGbDWXtK2DRzkYBy+Hb5PflbkTqpv6BRP0=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhAbAqrFWPY+02aQzdC14lE0QsujAjqI2/AR4wDaatSR0eX+5x3tKpIyozNbCHtw+zRfUakts18VNZx7DGHsN22CbkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FHvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgoZoBidEZBa/Oi6VBmw1l7Stg0c5GAcvh2+T35W5E6qbUajJV"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 30
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAbAqrFWPY+02aQzdC14lE0QsujAjqI2/AR4wDaatSR0eX+5x3tKpIyozNbCHtw+zRfUakts18VNZx7DGHsN22CbhAd1PuJl86UMrf2uhFxc+yiQuajZiqzcoM50hm9j+54r1z8Hku6oSepEiykN9gi1CPnga2nwjPab0+rlZiZKtOA7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FHvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgoZoBidEZBa/Oi6VBmw1l7Stg0c5GAcvh2+T35W5E6qYdJoX/"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 30,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 718,
    "height": 30,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUTF3JV"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
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
    "state": "tx_+QGLCwH4hLhAbAqrFWPY+02aQzdC14lE0QsujAjqI2/AR4wDaatSR0eX+5x3tKpIyozNbCHtw+zRfUakts18VNZx7DGHsN22CbhAd1PuJl86UMrf2uhFxc+yiQuajZiqzcoM50hm9j+54r1z8Hku6oSepEiykN9gi1CPnga2nwjPab0+rlZiZKtOA7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FHvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgoZoBidEZBa/Oi6VBmw1l7Stg0c5GAcvh2+T35W5E6qYdJoX/"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 30
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 30,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 718,
    "height": 30,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUTF3JV"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FH/jWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EwKDZ5+//XY2Pq8L76sOjBksTqkI//LI+yoo2zsKHF+5aul6iOE8=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhAU8KfrK8cX6zsKu8bM1zPOUrug6y/hp+izZ6qtNzeJm3QVunH609Dl0aD6lk1acmfddTntZZFsV0/hFbW9EpKB7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBR/41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCg2efv/12Nj6vC++rDowZLE6pCP/yyPsqKNs7ChxfuWroOD2tV"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FH/jWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EwKDZ5+//XY2Pq8L76sOjBksTqkI//LI+yoo2zsKHF+5aul6iOE8=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhATFQHefgQeNwqcfxZrqv2kRRXLywI3WZ42AsC/+4jESW2kNYguEDQEEVeomj46arAT4x2umSHi4UwMVNeTIw2DbkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBR/41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCg2efv/12Nj6vC++rDowZLE6pCP/yyPsqKNs7ChxfuWroCyAuP"
  }
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 31
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhATFQHefgQeNwqcfxZrqv2kRRXLywI3WZ42AsC/+4jESW2kNYguEDQEEVeomj46arAT4x2umSHi4UwMVNeTIw2DbhAU8KfrK8cX6zsKu8bM1zPOUrug6y/hp+izZ6qtNzeJm3QVunH609Dl0aD6lk1acmfddTntZZFsV0/hFbW9EpKB7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBR/41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCg2efv/12Nj6vC++rDowZLE6pCP/yyPsqKNs7ChxfuWroVah7W"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 31,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 600,
    "height": 31,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkYTnKgAOLHGSX"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhATFQHefgQeNwqcfxZrqv2kRRXLywI3WZ42AsC/+4jESW2kNYguEDQEEVeomj46arAT4x2umSHi4UwMVNeTIw2DbhAU8KfrK8cX6zsKu8bM1zPOUrug6y/hp+izZ6qtNzeJm3QVunH609Dl0aD6lk1acmfddTntZZFsV0/hFbW9EpKB7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBR/41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCg2efv/12Nj6vC++rDowZLE6pCP/yyPsqKNs7ChxfuWroVah7W"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 31
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 31,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 600,
    "height": 31,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkYTnKgAOLHGSX"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FIPjWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmwKCJJFhRltdi+YqSVhCq14u1RX8FDa5W1YJDfhESohFCNNbvdEM=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhAJq+e1nghUTCXAuEVXt2YqpYY8n2jeGepsDfIxYm/BBIdYYfD2xY16y8qMYpDSzd3a8gLxbsvWBusdveV/qslBbkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSD41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgiSRYUZbXYvmKklYQqteLtUV/BQ2uVtWCQ34REqIRQjQ6V6AH"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FIPjWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmwKCJJFhRltdi+YqSVhCq14u1RX8FDa5W1YJDfhESohFCNNbvdEM=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhAMcXMGi6ZK6Hae5dPFsyOmzzV10N8Yp4R8WH6O0NpKnPumHeHDL31TdP3k3xKh/uksB8kUz/zDhgD1Czz5BIoCLkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSD41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgiSRYUZbXYvmKklYQqteLtUV/BQ2uVtWCQ34REqIRQjSwBWcy"
  }
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 32
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAJq+e1nghUTCXAuEVXt2YqpYY8n2jeGepsDfIxYm/BBIdYYfD2xY16y8qMYpDSzd3a8gLxbsvWBusdveV/qslBbhAMcXMGi6ZK6Hae5dPFsyOmzzV10N8Yp4R8WH6O0NpKnPumHeHDL31TdP3k3xKh/uksB8kUz/zDhgD1Czz5BIoCLkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSD41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgiSRYUZbXYvmKklYQqteLtUV/BQ2uVtWCQ34REqIRQjTai59P"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 32,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 600,
    "height": 32,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/qiUiX+TWYF0W"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAJq+e1nghUTCXAuEVXt2YqpYY8n2jeGepsDfIxYm/BBIdYYfD2xY16y8qMYpDSzd3a8gLxbsvWBusdveV/qslBbhAMcXMGi6ZK6Hae5dPFsyOmzzV10N8Yp4R8WH6O0NpKnPumHeHDL31TdP3k3xKh/uksB8kUz/zDhgD1Czz5BIoCLkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSD41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgiSRYUZbXYvmKklYQqteLtUV/BQ2uVtWCQ34REqIRQjTai59P"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 32
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 32,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 600,
    "height": 32,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/qiUiX+TWYF0W"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1K4BjA=",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1K4BjA=",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1K4BjA=",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1K4BjA=",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1K4BjA=",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QE+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FIfj2uPT48oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgjAt2+/jT3WJAx/X8mmqIq5idH48B7FqmRC/tWic4jqcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPAoMiJGMwkqpGuReaeK7mpYi5T7WWORAS9MIM4mNJNq8nY2Q5XXw==",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1K4BjA=",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QGKCwH4QrhA2k0OjNinlJEs/bmGE2aRbfrRzRyjWzBfDeeC+DkGECTJaOSC8H5fIlPgVdxBLZ8t6vAKIW4RJuLEvcVCTaQyCLkBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSH49rj0+PKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwKDIiRjMJKqRrkXmniu5qWIuU+1ljkQEvTCDOJjSTavJ2E0OpXQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QE+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FIfj2uPT48oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgjAt2+/jT3WJAx/X8mmqIq5idH48B7FqmRC/tWic4jqcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPAoMiJGMwkqpGuReaeK7mpYi5T7WWORAS9MIM4mNJNq8nY2Q5XXw==",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1K4BjA=",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QGKCwH4QrhAksoFcbpe1JAC6Wl81RukicmCipmwMO6MtsBF+gsyTpMAECFWlVYBx9GUhvEeRe9I0/sOPex8h6WGoEqS7VorC7kBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSH49rj0+PKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwKDIiRjMJKqRrkXmniu5qWIuU+1ljkQEvTCDOJjSTavJ2GPO4vw="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QHMCwH4hLhAksoFcbpe1JAC6Wl81RukicmCipmwMO6MtsBF+gsyTpMAECFWlVYBx9GUhvEeRe9I0/sOPex8h6WGoEqS7VorC7hA2k0OjNinlJEs/bmGE2aRbfrRzRyjWzBfDeeC+DkGECTJaOSC8H5fIlPgVdxBLZ8t6vAKIW4RJuLEvcVCTaQyCLkBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSH49rj0+PKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwKDIiRjMJKqRrkXmniu5qWIuU+1ljkQEvTCDOJjSTavJ2DTvHrM="
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
    "state": "tx_+QHMCwH4hLhAksoFcbpe1JAC6Wl81RukicmCipmwMO6MtsBF+gsyTpMAECFWlVYBx9GUhvEeRe9I0/sOPex8h6WGoEqS7VorC7hA2k0OjNinlJEs/bmGE2aRbfrRzRyjWzBfDeeC+DkGECTJaOSC8H5fIlPgVdxBLZ8t6vAKIW4RJuLEvcVCTaQyCLkBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSH49rj0+PKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwKDIiRjMJKqRrkXmniu5qWIuU+1ljkQEvTCDOJjSTavJ2DTvHrM="
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUi+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBfqAMT8CGqxIJ6ug4WvHgYACBijRyJ5nYMnCddGri9GFAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKCepTlvYTdXUNgyx5o0mNZ570++p/wFQyz3LEs6Y0KjmOYiLYk=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhA7zO8WKUUixwZa5AO56K9x33fHDznI6bwWmhZe/uyioHspcslmjNVNDeq8UEcTShI/vz9IUxENw3mDJ7I48tjBbkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FIvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgnqU5b2E3V1DYMseaNJjWee9Pvqf8BUMs9yxLOmNCo5ii/jZ7"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUi+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBfqAMT8CGqxIJ6ug4WvHgYACBijRyJ5nYMnCddGri9GFAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKCepTlvYTdXUNgyx5o0mNZ570++p/wFQyz3LEs6Y0KjmOYiLYk=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhAwc97wiT9SWBvXBrpqAFS4iQN9Q3tixj7UaQ8L5QlUNxEFWlb9Sp9KuJr8w7vQTsGcYBLU+NwrEFGwJs5QXeKA7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FIvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgnqU5b2E3V1DYMseaNJjWee9Pvqf8BUMs9yxLOmNCo5gbYk8Z"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 34
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAwc97wiT9SWBvXBrpqAFS4iQN9Q3tixj7UaQ8L5QlUNxEFWlb9Sp9KuJr8w7vQTsGcYBLU+NwrEFGwJs5QXeKA7hA7zO8WKUUixwZa5AO56K9x33fHDznI6bwWmhZe/uyioHspcslmjNVNDeq8UEcTShI/vz9IUxENw3mDJ7I48tjBbkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FIvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgnqU5b2E3V1DYMseaNJjWee9Pvqf8BUMs9yxLOmNCo5jRbWGD"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 34,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 718,
    "height": 34,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKTmJT3"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAwc97wiT9SWBvXBrpqAFS4iQN9Q3tixj7UaQ8L5QlUNxEFWlb9Sp9KuJr8w7vQTsGcYBLU+NwrEFGwJs5QXeKA7hA7zO8WKUUixwZa5AO56K9x33fHDznI6bwWmhZe/uyioHspcslmjNVNDeq8UEcTShI/vz9IUxENw3mDJ7I48tjBbkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FIvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgnqU5b2E3V1DYMseaNJjWee9Pvqf8BUMs9yxLOmNCo5jRbWGD"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 34
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 34,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 718,
    "height": 34,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKTmJT3"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FI/jWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EwKDf+7+GGKRw38ik655eCWs+bvuXFHW+qKgisP5OO9yQqPLzJZc=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhAn2fig/iMsz358WTdVQa1OZe+BJCVQ9JaO10DFv4PkgYDFMnijydmyS56WHRInzkONebj4+y2QL63ua4bOoXgArkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSP41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCg3/u/hhikcN/IpOueXglrPm77lxR1vqioIrD+TjvckKi9HxTH"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FI/jWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EwKDf+7+GGKRw38ik655eCWs+bvuXFHW+qKgisP5OO9yQqPLzJZc=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhAYPy1qiciXowEc7Lwa01Pv2/tiu/EPna+eNTjusxnBGe8IVICCRzli8qgLLXa6hA/1kcNoXExX24iGvyHevUMA7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSP41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCg3/u/hhikcN/IpOueXglrPm77lxR1vqioIrD+TjvckKi9v3/j"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 35
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAYPy1qiciXowEc7Lwa01Pv2/tiu/EPna+eNTjusxnBGe8IVICCRzli8qgLLXa6hA/1kcNoXExX24iGvyHevUMA7hAn2fig/iMsz358WTdVQa1OZe+BJCVQ9JaO10DFv4PkgYDFMnijydmyS56WHRInzkONebj4+y2QL63ua4bOoXgArkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSP41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCg3/u/hhikcN/IpOueXglrPm77lxR1vqioIrD+TjvckKjBinAH"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 35,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 600,
    "height": 35,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkYTnKgAa2pgUZ"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAYPy1qiciXowEc7Lwa01Pv2/tiu/EPna+eNTjusxnBGe8IVICCRzli8qgLLXa6hA/1kcNoXExX24iGvyHevUMA7hAn2fig/iMsz358WTdVQa1OZe+BJCVQ9JaO10DFv4PkgYDFMnijydmyS56WHRInzkONebj4+y2QL63ua4bOoXgArkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSP41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCg3/u/hhikcN/IpOueXglrPm77lxR1vqioIrD+TjvckKjBinAH"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 35
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 35,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 600,
    "height": 35,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkYTnKgAa2pgUZ"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FJPjWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmwKBK4Bq4bjI25IYgeAQRl50MgL4g3iAAi0ObYIdefF1My9uFxWY=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhAdDgvkER3K679+M/SYh1EuYxmdCj3Q0zgaSc8crZsbocIXBOp7BxeRYObiTFiVluo4Mezx8kVGYixd8URq76BB7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBST41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgSuAauG4yNuSGIHgEEZedDIC+IN4gAItDm2CHXnxdTMtO+U4y"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FJPjWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmwKBK4Bq4bjI25IYgeAQRl50MgL4g3iAAi0ObYIdefF1My9uFxWY=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhAnoraY8aChGzbIcJr/Da/8WrcJ5XXtlf87z+BPBMS5tzpNlqMzs+1AAWkYyT/pnbH3hXt3g1QKh4p8bGNw1i2DbkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBST41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgSuAauG4yNuSGIHgEEZedDIC+IN4gAItDm2CHXnxdTMtWlKf9"
  }
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 36
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAdDgvkER3K679+M/SYh1EuYxmdCj3Q0zgaSc8crZsbocIXBOp7BxeRYObiTFiVluo4Mezx8kVGYixd8URq76BB7hAnoraY8aChGzbIcJr/Da/8WrcJ5XXtlf87z+BPBMS5tzpNlqMzs+1AAWkYyT/pnbH3hXt3g1QKh4p8bGNw1i2DbkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBST41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgSuAauG4yNuSGIHgEEZedDIC+IN4gAItDm2CHXnxdTMvTp4b0"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 36,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 600,
    "height": 36,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/qiUiX+TWYF0W"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
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
    "state": "tx_+QGsCwH4hLhAdDgvkER3K679+M/SYh1EuYxmdCj3Q0zgaSc8crZsbocIXBOp7BxeRYObiTFiVluo4Mezx8kVGYixd8URq76BB7hAnoraY8aChGzbIcJr/Da/8WrcJ5XXtlf87z+BPBMS5tzpNlqMzs+1AAWkYyT/pnbH3hXt3g1QKh4p8bGNw1i2DbkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBST41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgSuAauG4yNuSGIHgEEZedDIC+IN4gAItDm2CHXnxdTMvTp4b0"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 36
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 36,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 600,
    "height": 36,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/qiUiX+TWYF0W"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAmoF82g=",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAmoF82g=",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAmoF82g=",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAmoF82g=",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAmoF82g=",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QE+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FJfj2uPT48oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgjAt2+/jT3WJAx/X8mmqIq5idH48B7FqmRC/tWic4jqcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALAoFhbvtWX9oilxQLgbEeL1vVuMcPpfcp7kPkOZJYL40hs1dqYlQ==",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAmoF82g=",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QGKCwH4QrhAW/VSL5xbJ39WyThPEZfTSNCrHJTZwBJoU4CRP8hpe1mv7qpVqhvxk1Q3U58EIW4eKaDcJTEFeQRHa7SSZkwBC7kBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSX49rj0+PKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwKBYW77Vl/aIpcUC4GxHi9b1bjHD6X3Ke5D5DmSWC+NIbDFGB+0="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QE+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FJfj2uPT48oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgjAt2+/jT3WJAx/X8mmqIq5idH48B7FqmRC/tWic4jqcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALAoFhbvtWX9oilxQLgbEeL1vVuMcPpfcp7kPkOZJYL40hs1dqYlQ==",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAmoF82g=",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QGKCwH4QrhAepwVEPukswW2kURJsv1MMCg64JdkGHd+4fe832DFizfXOLrZUzCnKUN49Sou9zL5/k+NhWZBB68Dxi7PobMfCrkBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSX49rj0+PKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwKBYW77Vl/aIpcUC4GxHi9b1bjHD6X3Ke5D5DmSWC+NIbNXYUVg="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QHMCwH4hLhAW/VSL5xbJ39WyThPEZfTSNCrHJTZwBJoU4CRP8hpe1mv7qpVqhvxk1Q3U58EIW4eKaDcJTEFeQRHa7SSZkwBC7hAepwVEPukswW2kURJsv1MMCg64JdkGHd+4fe832DFizfXOLrZUzCnKUN49Sou9zL5/k+NhWZBB68Dxi7PobMfCrkBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSX49rj0+PKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwKBYW77Vl/aIpcUC4GxHi9b1bjHD6X3Ke5D5DmSWC+NIbJrdZZA="
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
    "state": "tx_+QHMCwH4hLhAW/VSL5xbJ39WyThPEZfTSNCrHJTZwBJoU4CRP8hpe1mv7qpVqhvxk1Q3U58EIW4eKaDcJTEFeQRHa7SSZkwBC7hAepwVEPukswW2kURJsv1MMCg64JdkGHd+4fe832DFizfXOLrZUzCnKUN49Sou9zL5/k+NhWZBB68Dxi7PobMfCrkBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSX49rj0+PKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwKBYW77Vl/aIpcUC4GxHi9b1bjHD6X3Ke5D5DmSWC+NIbJrdZZA="
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUm+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBfqAMT8CGqxIJ6ug4WvHgYACBijRyJ5nYMnCddGri9GFAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKAkKvbP9u1qPLHjx/xIUBhXD22mCfCHHavXdGhmzqHQ8701AsQ=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhAnl8mt6GB1cjum74Fao8U65x9J6UIPQNvU0foreW38xg8xf6JpUwwolIJM7nvm40mhaFJ29E4I4k5w+tHS4axD7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FJvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgJCr2z/btajyx48f8SFAYVw9tpgnwhx2r13RoZs6h0PNGfBe3"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUm+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBfqAMT8CGqxIJ6ug4WvHgYACBijRyJ5nYMnCddGri9GFAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKAkKvbP9u1qPLHjx/xIUBhXD22mCfCHHavXdGhmzqHQ8701AsQ=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhAe8x48gx2G51c75WXolWOqLwE833NgicpsAF44NH9hlm+33dq6XsTi01Z2XI1HYOUWx8QP65hWxjnA4yokB4jB7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FJvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgJCr2z/btajyx48f8SFAYVw9tpgnwhx2r13RoZs6h0PMBQZdA"
  }
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 38
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAe8x48gx2G51c75WXolWOqLwE833NgicpsAF44NH9hlm+33dq6XsTi01Z2XI1HYOUWx8QP65hWxjnA4yokB4jB7hAnl8mt6GB1cjum74Fao8U65x9J6UIPQNvU0foreW38xg8xf6JpUwwolIJM7nvm40mhaFJ29E4I4k5w+tHS4axD7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FJvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgJCr2z/btajyx48f8SFAYVw9tpgnwhx2r13RoZs6h0PO6WNzY"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 38,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 718,
    "height": 38,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAArMtts"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAe8x48gx2G51c75WXolWOqLwE833NgicpsAF44NH9hlm+33dq6XsTi01Z2XI1HYOUWx8QP65hWxjnA4yokB4jB7hAnl8mt6GB1cjum74Fao8U65x9J6UIPQNvU0foreW38xg8xf6JpUwwolIJM7nvm40mhaFJ29E4I4k5w+tHS4axD7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FJvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgJCr2z/btajyx48f8SFAYVw9tpgnwhx2r13RoZs6h0PO6WNzY"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 38
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 38,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 718,
    "height": 38,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAArMtts"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FJ/jWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EwKAvHvwUWC/j34u3URG5BL1svqxaSLaYRrX6pD9cCwQCKeViZmQ=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhAPb96/7lPZc6U0TWSLElfC3v0wsNyQXEdPuRlQBV1DLC3V5TlqvCzgdZeTUL7C0td6+WdUXOGZpdqJM+Ry4izD7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSf41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgLx78FFgv49+Lt1ERuQS9bL6sWki2mEa1+qQ/XAsEAilZeNQ2"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FJ/jWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EwKAvHvwUWC/j34u3URG5BL1svqxaSLaYRrX6pD9cCwQCKeViZmQ=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhAeB5m/zoudC4Mz/uHB+vZ/cHa/iru4VL1MIUjA/OcNoJm9NO2uNoqL7a2ghfEMkbm+YpXeuYhh20Sz1qe6ElMALkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSf41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgLx78FFgv49+Lt1ERuQS9bL6sWki2mEa1+qQ/XAsEAimFGYzx"
  }
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 39
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAPb96/7lPZc6U0TWSLElfC3v0wsNyQXEdPuRlQBV1DLC3V5TlqvCzgdZeTUL7C0td6+WdUXOGZpdqJM+Ry4izD7hAeB5m/zoudC4Mz/uHB+vZ/cHa/iru4VL1MIUjA/OcNoJm9NO2uNoqL7a2ghfEMkbm+YpXeuYhh20Sz1qe6ElMALkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSf41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgLx78FFgv49+Lt1ERuQS9bL6sWki2mEa1+qQ/XAsEAilH7HAD"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 39,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 600,
    "height": 39,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkYTnKgAa2pgUZ"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAPb96/7lPZc6U0TWSLElfC3v0wsNyQXEdPuRlQBV1DLC3V5TlqvCzgdZeTUL7C0td6+WdUXOGZpdqJM+Ry4izD7hAeB5m/zoudC4Mz/uHB+vZ/cHa/iru4VL1MIUjA/OcNoJm9NO2uNoqL7a2ghfEMkbm+YpXeuYhh20Sz1qe6ElMALkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSf41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgLx78FFgv49+Lt1ERuQS9bL6sWki2mEa1+qQ/XAsEAilH7HAD"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 39
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 39,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 600,
    "height": 39,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkYTnKgAa2pgUZ"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FKPjWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmwKAeJ0wiO36eJDIlvi6G3HqIKLQscvBcPEcLnF2a0ReGGt3v/q4=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhA/MTV2csmetT8mzNCwIq+6/vhAO3IT0tu43Ym3I8r4AYeiNd7/cSXGqrSF3JRTUgYtMHiGN4nm6SbKkNQiWl/C7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSj41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgHidMIjt+niQyJb4uhtx6iCi0LHLwXDxHC5xdmtEXhhqw7tBP"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FKPjWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX6gDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhQEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmwKAeJ0wiO36eJDIlvi6G3HqIKLQscvBcPEcLnF2a0ReGGt3v/q4=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhA1ZEOJZNhH65/HxSZou4+HqtzVBeAhdj8ISiLAgk/kOCDiT5QodLniD7IpaVlXxdPz6CXGRt+ot5lRiDGlTjBCLkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSj41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgHidMIjt+niQyJb4uhtx6iCi0LHLwXDxHC5xdmtEXhhrnFV3b"
  }
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 40
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhA1ZEOJZNhH65/HxSZou4+HqtzVBeAhdj8ISiLAgk/kOCDiT5QodLniD7IpaVlXxdPz6CXGRt+ot5lRiDGlTjBCLhA/MTV2csmetT8mzNCwIq+6/vhAO3IT0tu43Ym3I8r4AYeiNd7/cSXGqrSF3JRTUgYtMHiGN4nm6SbKkNQiWl/C7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSj41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgHidMIjt+niQyJb4uhtx6iCi0LHLwXDxHC5xdmtEXhhoSULyp"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 40,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 600,
    "height": 40,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/qiUiX+ZkmnBe"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhA1ZEOJZNhH65/HxSZou4+HqtzVBeAhdj8ISiLAgk/kOCDiT5QodLniD7IpaVlXxdPz6CXGRt+ot5lRiDGlTjBCLhA/MTV2csmetT8mzNCwIq+6/vhAO3IT0tu43Ym3I8r4AYeiNd7/cSXGqrSF3JRTUgYtMHiGN4nm6SbKkNQiWl/C7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSj41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF+oAxPwIarEgnq6Dha8eBgAIGKNHInmdgycJ10auL0YUBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgHidMIjt+niQyJb4uhtx6iCi0LHLwXDxHC5xdmtEXhhoSULyp"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "round": 40
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 40,
    "contract_id": "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr",
    "gas_price": 1,
    "gas_used": 600,
    "height": 40,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/qiUiX+ZkmnBe"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
    ],
    "contracts": [
      "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
    ]
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "poi": "pi_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AAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPkBy6C5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6oRpbml0uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+5AUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///////////////////////////////////////////kBNKDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtd45nZXRfYmFsYW5jZV9vZrjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQLqYgABO2IAAVuRgICAUX+5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6hRiAAKvV1CAgFF/1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcUYgABhldQgIBRfyhhWzgmK00kF7owGlfTf0IXbL47tExEq9XJIHKPxqNpFGIAAZpXUICAUX9Ht7ynsZuaIy9z478aENZZGY9wCcRts3nwZxb5hn8ayBRiAAK7V1CAgFF/jAt2+/jT3WJAx/X8mmqIq5idH48B7FqmRC/tWic4jqcUYgACzldQgIBRf4mhpZa7jpXbFRcxn4DDPcxRnuulACBaOZ2fmal85p0PFGIAAiNXUIBRfyUk52A6qQ/AUHbqdi5s6si+bkOFHZWVHBXYWCmXOFkMFGIAAqZXUGABGVEAW2AAGVlgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tZWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2ADgVKBUpBWW2AgAVFRkFBZUICRUFCAMZBQkFZbYCABUYBRkGAgAVGRUFlQgIKSUJJQUGAAYABgAINZkIFSWWAgAZCBUmAgkAN/R7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsiBUmAAhlrxUICRUFBbM4GQkVBbMDFgAGAAYACFWWAgAZCBUmAgkANgAYFShWAAWvFQgYEDkFCRUFCQVltgIAFRgFGQYCABgFGQYCABUZJQWVCBgYSTUJNQk1BQYABgAGAAg1mQgVJZYCABkIFSYCCQA39Ht7ynsZuaIy9z478aENZZGY9wCcRts3nwZxb5hn8ayIFSYACHWvFQYABgAGAAhFlgIAGQgVJgIJADYAGBUoRgAFrxUIExklBQUJBWW1BZUFAwMZBWW1BQgpFQUGIAAWNWW2AgAVFRkFBZUICRUFBiAAH0VltgIAFRgFGQYCABUZFQWVCAgpJQklBQYgAB+laFMi4xLjCAAcAK+FOgNYx8viZGBiV3oOEGU/UGE8iI7mrpDHTyqMV3g4fL28/xoIWUTo2KvTwb8VD508whGM9kq36Mgp8fhoSGIfYMIL8LgICAgICAgICAgICAgICAAPhEoD9w0ow9ucwAKzMGn9HRLnY4BvBGHGcGmgI5Ixx8n3ak4iCgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD4lKCEeq/sWDToISyjF5mcLsr+tsdUO+10nsziJDkph8LaS/hxgICAgICAgICAoOtVWdUq0Wv+YU41YUUdTqktiDMcZUw5phNrJbwyCSOjgICgxE4zJ+TR+w/Xqby7X1eYJoZLU7SL63nBtRQsDLxlTlOAgKC5B5vn/FKjJuY0a3BJNH+i/lhxi2FLhhswZaMmX5xZRYD4dKCFlE6Nir08G/FQ+dPMIRjPZKt+jIKfH4aEhiH2DCC/C/hRoD9w0ow9ucwAKzMGn9HRLnY4BvBGHGcGmgI5Ixx8n3akoAh0DgZd1vSIXHZJmSQiayifodBvPmXiClGd1uaffzXsgICAgICAgICAgICAgICA+GWguQeb5/xSoybmNGtwSTR/ov5YcYthS4YbMGWjJl+cWUX4QqAagDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhaArEjtgwuisJzNVubaQYPUSfzqnx/3jQdF5FvUMOm7YUsDA4Vf3jQ=="
  },
  "tag": "poi",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
    ],
    "contracts": [
      "ct_2uKhvG9gNuByJp1h2AzcmaSfbescaFFLyzyWXttRxt1N5tG9mr"
    ]
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "poi": "pi_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AAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPkBy6C5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6oRpbml0uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+5AUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///////////////////////////////////////////kBNKDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtd45nZXRfYmFsYW5jZV9vZrjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQLqYgABO2IAAVuRgICAUX+5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6hRiAAKvV1CAgFF/1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcUYgABhldQgIBRfyhhWzgmK00kF7owGlfTf0IXbL47tExEq9XJIHKPxqNpFGIAAZpXUICAUX9Ht7ynsZuaIy9z478aENZZGY9wCcRts3nwZxb5hn8ayBRiAAK7V1CAgFF/jAt2+/jT3WJAx/X8mmqIq5idH48B7FqmRC/tWic4jqcUYgACzldQgIBRf4mhpZa7jpXbFRcxn4DDPcxRnuulACBaOZ2fmal85p0PFGIAAiNXUIBRfyUk52A6qQ/AUHbqdi5s6si+bkOFHZWVHBXYWCmXOFkMFGIAAqZXUGABGVEAW2AAGVlgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tZWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2ADgVKBUpBWW2AgAVFRkFBZUICRUFCAMZBQkFZbYCABUYBRkGAgAVGRUFlQgIKSUJJQUGAAYABgAINZkIFSWWAgAZCBUmAgkAN/R7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsiBUmAAhlrxUICRUFBbM4GQkVBbMDFgAGAAYACFWWAgAZCBUmAgkANgAYFShWAAWvFQgYEDkFCRUFCQVltgIAFRgFGQYCABgFGQYCABUZJQWVCBgYSTUJNQk1BQYABgAGAAg1mQgVJZYCABkIFSYCCQA39Ht7ynsZuaIy9z478aENZZGY9wCcRts3nwZxb5hn8ayIFSYACHWvFQYABgAGAAhFlgIAGQgVJgIJADYAGBUoRgAFrxUIExklBQUJBWW1BZUFAwMZBWW1BQgpFQUGIAAWNWW2AgAVFRkFBZUICRUFBiAAH0VltgIAFRgFGQYCABUZFQWVCAgpJQklBQYgAB+laFMi4xLjCAAcAK+FOgNYx8viZGBiV3oOEGU/UGE8iI7mrpDHTyqMV3g4fL28/xoIWUTo2KvTwb8VD508whGM9kq36Mgp8fhoSGIfYMIL8LgICAgICAgICAgICAgICAAPhEoD9w0ow9ucwAKzMGn9HRLnY4BvBGHGcGmgI5Ixx8n3ak4iCgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD4lKCEeq/sWDToISyjF5mcLsr+tsdUO+10nsziJDkph8LaS/hxgICAgICAgICAoOtVWdUq0Wv+YU41YUUdTqktiDMcZUw5phNrJbwyCSOjgICgxE4zJ+TR+w/Xqby7X1eYJoZLU7SL63nBtRQsDLxlTlOAgKC5B5vn/FKjJuY0a3BJNH+i/lhxi2FLhhswZaMmX5xZRYD4dKCFlE6Nir08G/FQ+dPMIRjPZKt+jIKfH4aEhiH2DCC/C/hRoD9w0ow9ucwAKzMGn9HRLnY4BvBGHGcGmgI5Ixx8n3akoAh0DgZd1vSIXHZJmSQiayifodBvPmXiClGd1uaffzXsgICAgICAgICAgICAgICA+GWguQeb5/xSoybmNGtwSTR/ov5YcYthS4YbMGWjJl+cWUX4QqAagDE/AhqsSCeroOFrx4GAAgYo0cieZ2DJwnXRq4vRhaArEjtgwuisJzNVubaQYPUSfzqnx/3jQdF5FvUMOm7YUsDA4Vf3jQ=="
  },
  "tag": "poi",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: accounts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: contracts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: accounts, contracts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_found",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_found",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: accounts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: contracts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: accounts, contracts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_found",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_found",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAnHQYrA==",
    "code": "cb_+QP1RgKg/ukoFMi2RBUIDNHZ3pMMzHSrPs/uKkwO/vEf7cRnitr5Avv5ASqgaPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8WEbWFpbrjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QHLoLnJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqhGluaXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uMxiAABkYgAAhJGAgIBRf7nJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqFGIAAMBXUIBRf2jyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFFGIAAK9XUGABGVEAW2AAGVlgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tZWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2ADgVKBUpBWW2AgAVFRWVCAkVBQgJBQkFZbUFCCkVBQYgAAjFaFMi4xLjAhVoVW",
    "deposit": 10,
    "vm_version": 3
  },
  "tag": "new_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QTXOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FKfkEjrkEi/kEiIICPQGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EgwMAAbkD+PkD9UYCoP7pKBTItkQVCAzR2d6TDMx0qz7P7ipMDv7xH+3EZ4ra+QL7+QEqoGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFhG1haW64wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPkBy6C5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6oRpbml0uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+5AUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7jMYgAAZGIAAISRgICAUX+5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6hRiAADAV1CAUX9o8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxRRiAACvV1BgARlRAFtgABlZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbWVlgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgA4FSgVKQVltgIAFRUVlQgJFQUICQUJBWW1BQgpFQUGIAAIxWhTIuMS4wCrhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoMF2r8ykHEX6BSrwhjdvDqe7ffZz5go1h9zSUAt54Br+P3U6Ug==",
    "updates": [
      {
        "abi_version": 1,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAnHQYrA==",
        "code": "cb_+QP1RgKg/ukoFMi2RBUIDNHZ3pMMzHSrPs/uKkwO/vEf7cRnitr5Avv5ASqgaPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8WEbWFpbrjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QHLoLnJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqhGluaXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uMxiAABkYgAAhJGAgIBRf7nJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqFGIAAMBXUIBRf2jyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFFGIAAK9XUGABGVEAW2AAGVlgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tZWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2ADgVKBUpBWW2AgAVFRWVCAkVBQgJBQkFZbUFCCkVBQYgAAjFaFMi4xLjAhVoVW",
        "deposit": 10,
        "op": "OffChainNewContract",
        "owner": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "vm_version": 3
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
    "tx": "tx_+QUjCwH4QrhAtnEOkGCwtbIqX8UCPTTwh9JUeneasYvq8+I9QbSaxLCjZymH0a8qtEt5oI9WxYGUKXVCSzARlHt0eqHoQlbyDbkE2vkE1zkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSn5BI65BIv5BIiCAj0BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIMDAAG5A/j5A/VGAqD+6SgUyLZEFQgM0dnekwzMdKs+z+4qTA7+8R/txGeK2vkC+/kBKqBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxYRtYWluuMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AcuguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeqEaW5pdLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4zGIAAGRiAACEkYCAgFF/uclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoUYgAAwFdQgFF/aPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8UUYgAAr1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW1lZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYAOBUoFSkFZbYCABUVFZUICRUFCAkFCQVltQUIKRUFBiAACMVoUyLjEuMAq4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKDBdq/MpBxF+gUq8IY3bw6nu332c+YKNYfc0lALeeAa/vKkQPM="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QTXOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FKfkEjrkEi/kEiIICPQGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EgwMAAbkD+PkD9UYCoP7pKBTItkQVCAzR2d6TDMx0qz7P7ipMDv7xH+3EZ4ra+QL7+QEqoGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFhG1haW64wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPkBy6C5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6oRpbml0uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+5AUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7jMYgAAZGIAAISRgICAUX+5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6hRiAADAV1CAUX9o8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxRRiAACvV1BgARlRAFtgABlZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbWVlgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgA4FSgVKQVltgIAFRUVlQgJFQUICQUJBWW1BQgpFQUGIAAIxWhTIuMS4wCrhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoMF2r8ykHEX6BSrwhjdvDqe7ffZz5go1h9zSUAt54Br+P3U6Ug==",
    "updates": [
      {
        "abi_version": 1,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAnHQYrA==",
        "code": "cb_+QP1RgKg/ukoFMi2RBUIDNHZ3pMMzHSrPs/uKkwO/vEf7cRnitr5Avv5ASqgaPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8WEbWFpbrjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QHLoLnJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqhGluaXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uMxiAABkYgAAhJGAgIBRf7nJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqFGIAAMBXUIBRf2jyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFFGIAAK9XUGABGVEAW2AAGVlgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tZWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2ADgVKBUpBWW2AgAVFRWVCAkVBQgJBQkFZbUFCCkVBQYgAAjFaFMi4xLjAhVoVW",
        "deposit": 10,
        "op": "OffChainNewContract",
        "owner": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "vm_version": 3
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QUjCwH4QrhAUeNs7naoBx+mWy83ebaex4ICxtdfqFbVdjqTKYdYxYUS1NZHXEMHb/OxBw8cGuMKhJWIkGqO16IWtOS0fr9FDLkE2vkE1zkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSn5BI65BIv5BIiCAj0BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIMDAAG5A/j5A/VGAqD+6SgUyLZEFQgM0dnekwzMdKs+z+4qTA7+8R/txGeK2vkC+/kBKqBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxYRtYWluuMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AcuguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeqEaW5pdLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4zGIAAGRiAACEkYCAgFF/uclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoUYgAAwFdQgFF/aPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8UUYgAAr1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW1lZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYAOBUoFSkFZbYCABUVFZUICRUFCAkFCQVltQUIKRUFBiAACMVoUyLjEuMAq4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKDBdq/MpBxF+gUq8IY3bw6nu332c+YKNYfc0lALeeAa/tn1lWQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QVlCwH4hLhAUeNs7naoBx+mWy83ebaex4ICxtdfqFbVdjqTKYdYxYUS1NZHXEMHb/OxBw8cGuMKhJWIkGqO16IWtOS0fr9FDLhAtnEOkGCwtbIqX8UCPTTwh9JUeneasYvq8+I9QbSaxLCjZymH0a8qtEt5oI9WxYGUKXVCSzARlHt0eqHoQlbyDbkE2vkE1zkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSn5BI65BIv5BIiCAj0BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIMDAAG5A/j5A/VGAqD+6SgUyLZEFQgM0dnekwzMdKs+z+4qTA7+8R/txGeK2vkC+/kBKqBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxYRtYWluuMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AcuguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeqEaW5pdLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4zGIAAGRiAACEkYCAgFF/uclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoUYgAAwFdQgFF/aPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8UUYgAAr1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW1lZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYAOBUoFSkFZbYCABUVFZUICRUFCAkFCQVltQUIKRUFBiAACMVoUyLjEuMAq4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKDBdq/MpBxF+gUq8IY3bw6nu332c+YKNYfc0lALeeAa/iXQMSY="
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
    "state": "tx_+QVlCwH4hLhAUeNs7naoBx+mWy83ebaex4ICxtdfqFbVdjqTKYdYxYUS1NZHXEMHb/OxBw8cGuMKhJWIkGqO16IWtOS0fr9FDLhAtnEOkGCwtbIqX8UCPTTwh9JUeneasYvq8+I9QbSaxLCjZymH0a8qtEt5oI9WxYGUKXVCSzARlHt0eqHoQlbyDbkE2vkE1zkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSn5BI65BIv5BIiCAj0BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIMDAAG5A/j5A/VGAqD+6SgUyLZEFQgM0dnekwzMdKs+z+4qTA7+8R/txGeK2vkC+/kBKqBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxYRtYWluuMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AcuguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeqEaW5pdLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4zGIAAGRiAACEkYCAgFF/uclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoUYgAAwFdQgFF/aPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8UUYgAAr1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW1lZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYAOBUoFSkFZbYCABUVFZUICRUFCAkFCQVltQUIKRUFBiAACMVoUyLjEuMAq4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKDBdq/MpBxF+gUq8IY3bw6nu332c+YKNYfc0lALeeAa/iXQMSY="
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
        "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
        "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FKvjWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQW0/XR5UJq23Q1GIp5dK67tXcpg/SGeb7SvzZKKMxve9wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgaPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAqwKBZL7bWvUwYdHjRxax0Ap3XyuXatx55GnQk8yFbRuwlrIQtRKk=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhAHsPUVTR/GcthnfaLrdDkw5987Rc8rzHE/MyTsRAj2GZEPqXJdTWbr/D4qdvKCa+Tw2lvdYeBMMIGPLi+NjXyArkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSr41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEFtP10eVCatt0NRiKeXSuu7V3KYP0hnm+0r82SijMb3vcBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKsCgWS+21r1MGHR40cWsdAKd18rl2rceeRp0JPMhW0bsJawh091F"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FKvjWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQW0/XR5UJq23Q1GIp5dK67tXcpg/SGeb7SvzZKKMxve9wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgaPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAqwKBZL7bWvUwYdHjRxax0Ap3XyuXatx55GnQk8yFbRuwlrIQtRKk=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhAZN2mmxSFFrkGZZIu1U/qjunMzZyYPniDQdsHaj5QN9UWsEG6tF6E23xZoQNxYQDeb9cAKE9u2ox31WR9va12CLkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSr41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEFtP10eVCatt0NRiKeXSuu7V3KYP0hnm+0r82SijMb3vcBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKsCgWS+21r1MGHR40cWsdAKd18rl2rceeRp0JPMhW0bsJayGTDRP"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAHsPUVTR/GcthnfaLrdDkw5987Rc8rzHE/MyTsRAj2GZEPqXJdTWbr/D4qdvKCa+Tw2lvdYeBMMIGPLi+NjXyArhAZN2mmxSFFrkGZZIu1U/qjunMzZyYPniDQdsHaj5QN9UWsEG6tF6E23xZoQNxYQDeb9cAKE9u2ox31WR9va12CLkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSr41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEFtP10eVCatt0NRiKeXSuu7V3KYP0hnm+0r82SijMb3vcBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKsCgWS+21r1MGHR40cWsdAKd18rl2rceeRp0JPMhW0bsJaw7SJCV"
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
    "state": "tx_+QGsCwH4hLhAHsPUVTR/GcthnfaLrdDkw5987Rc8rzHE/MyTsRAj2GZEPqXJdTWbr/D4qdvKCa+Tw2lvdYeBMMIGPLi+NjXyArhAZN2mmxSFFrkGZZIu1U/qjunMzZyYPniDQdsHaj5QN9UWsEG6tF6E23xZoQNxYQDeb9cAKE9u2ox31WR9va12CLkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSr41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEFtP10eVCatt0NRiKeXSuu7V3KYP0hnm+0r82SijMb3vcBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKsCgWS+21r1MGHR40cWsdAKd18rl2rceeRp0JPMhW0bsJaw7SJCV"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "dry_run",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d"
  },
  "tag": "call_contract"
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
        "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "dry_run",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d"
  },
  "tag": "call_contract"
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
        "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "dry_run",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "dry_run",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 43,
    "contract_id": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
    "gas_price": 1,
    "gas_used": 192,
    "height": 43,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACr8s/aY"
  },
  "tag": "call_contract",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
    "round": 42
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 42,
    "contract_id": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
    "gas_price": 1,
    "gas_used": 192,
    "height": 42,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACr8s/aY"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
    "round": 42
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 42,
    "contract_id": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
    "gas_price": 1,
    "gas_used": 192,
    "height": 42,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACr8s/aY"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
    "round": 42
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 42,
    "contract_id": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
    "gas_price": 1,
    "gas_used": 192,
    "height": 42,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACr8s/aY"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
    "round": 42
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 42,
    "contract_id": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
    "gas_price": 1,
    "gas_used": 192,
    "height": 42,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACr8s/aY"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "clean_contract_calls"
}
```

#### responder <--- node
```javascript
{
  "action": "calls_pruned",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
    "round": 42
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "call_not_found",
    "request": {
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
        "round": 42
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
        "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
        "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FK/jWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQW0/XR5UJq23Q1GIp5dK67tXcpg/SGeb7SvzZKKMxve9wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgaPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAqwKDERIhatKy5dkKQatP6ZsIJrTvYyniDhsrSjWHMFxy5PEPaaQg=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhAbid+1+8Tvdrz0UYRP0QxhnsUC4+LRu0oH1CYstY27d0sNJx9sAVAiEqjP1amV/56lfvO6qZBGE9v/WEc0QzEBLkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSv41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEFtP10eVCatt0NRiKeXSuu7V3KYP0hnm+0r82SijMb3vcBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKsCgxESIWrSsuXZCkGrT+mbCCa072Mp4g4bK0o1hzBccuTzxOOwm"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FK/jWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQW0/XR5UJq23Q1GIp5dK67tXcpg/SGeb7SvzZKKMxve9wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgaPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8UAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAqwKDERIhatKy5dkKQatP6ZsIJrTvYyniDhsrSjWHMFxy5PEPaaQg=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhA8Kl6DkziMto54jjI6AZmqhck5D6l7DiNBpSq6CqhiTYRht5ipGk/8dO/9SWADw4jk9m4ipljIRBwVnlJw3CmCbkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSv41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEFtP10eVCatt0NRiKeXSuu7V3KYP0hnm+0r82SijMb3vcBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKsCgxESIWrSsuXZCkGrT+mbCCa072Mp4g4bK0o1hzBccuTwLxKH2"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAbid+1+8Tvdrz0UYRP0QxhnsUC4+LRu0oH1CYstY27d0sNJx9sAVAiEqjP1amV/56lfvO6qZBGE9v/WEc0QzEBLhA8Kl6DkziMto54jjI6AZmqhck5D6l7DiNBpSq6CqhiTYRht5ipGk/8dO/9SWADw4jk9m4ipljIRBwVnlJw3CmCbkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSv41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEFtP10eVCatt0NRiKeXSuu7V3KYP0hnm+0r82SijMb3vcBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKsCgxESIWrSsuXZCkGrT+mbCCa072Mp4g4bK0o1hzBccuTyJrcCY"
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
    "state": "tx_+QGsCwH4hLhAbid+1+8Tvdrz0UYRP0QxhnsUC4+LRu0oH1CYstY27d0sNJx9sAVAiEqjP1amV/56lfvO6qZBGE9v/WEc0QzEBLhA8Kl6DkziMto54jjI6AZmqhck5D6l7DiNBpSq6CqhiTYRht5ipGk/8dO/9SWADw4jk9m4ipljIRBwVnlJw3CmCbkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSv41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEFtP10eVCatt0NRiKeXSuu7V3KYP0hnm+0r82SijMb3vcBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIGjyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKsCgxESIWrSsuXZCkGrT+mbCCa072Mp4g4bK0o1hzBccuTyJrcCY"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "dry_run",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d"
  },
  "tag": "call_contract"
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
        "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "dry_run",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d"
  },
  "tag": "call_contract"
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
        "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "dry_run",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "dry_run",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 44,
    "contract_id": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
    "gas_price": 1,
    "gas_used": 192,
    "height": 44,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACr8s/aY"
  },
  "tag": "call_contract",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
    "round": 43
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 43,
    "contract_id": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
    "gas_price": 1,
    "gas_used": 192,
    "height": 43,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACr8s/aY"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
    "round": 43
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 43,
    "contract_id": "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d",
    "gas_price": 1,
    "gas_used": 192,
    "height": 43,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACr8s/aY"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
    ],
    "contracts": [
      "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d"
    ]
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "poi": "pi_+Qo2PAH5AmD5Al2gPNv/jRU7QpkVR/AC6yFkvjBUcNDeD+lZA+/fNJa+G1L5Ajn41KA82/+NFTtCmRVH8ALrIWS+MFRw0N4P6VkD7980lr4bUvixgICAgICAoMHi48sUi1/4LB+jrsdcySDXzBLyQ1Igxpd91OuROuhHgICgO6m3kt68QfyfIOAH8OXUHDKqCZ7oKML9lJL3gB86PueAoMoRn+9mFPzHyQSICRLBoWdZJIYp+38gjamAztCUiKfeoKbKODEGFrja/tYvqk5+obVO1/o1hWepkepH5PQmYYvFgICggvZJrcrkjSw9RBPpSJQ6AcUSqig/h19ZC0jyJy0cWDOA+E+glzmIfR0U7CH4WQRHbilxPDxZEDhfp3xt+a1FzoVo2hbtoCC1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmi8oKAQCGP6olIl/m+EmguxLq4g2NCBS0wGuZeExxICpTesdzHr8uScpnLhT7bp7noCD9dHlQmrbdDUYinl0rru1dymD9IZ5vtK/NkoozG973hcQKAQAK+E+gweLjyxSLX/gsH6Oux1zJINfMEvJDUiDGl33U65E66EftoDccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6Ei8oKAQCGJGE5yn/8+HSgyhGf72YU/MfJBIgJEsGhZ1kkhin7fyCNqYDO0JSIp974UYCglzmIfR0U7CH4WQRHbilxPDxZEDhfp3xt+a1FzoVo2haAgKC7EuriDY0IFLTAa5l4THEgKlN6x3Mevy5JymcuFPtunoCAgICAgICAgICAgOPioAy9bSFRQ28+Bi0XgG97E1tSLa6j7E6oYsprFohKey1UwMD5B6f5B6SgfiKWMMtz49kWjnNcrA3y8qNRtZvb4eI7MGhK+qpks3v5B4D5BIGgAJ1CqCpq56K3URPlfpefmisUenslyZYFdpKVFGfMggz5BF2AoCepMv5i2mPg+uG17O00eQSEcTtITmpHCpUh637u7D+/gICAgICAgICAgICAgIC5BCr5BCcoAaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSDAwABuQP4+QP1RgKg/ukoFMi2RBUIDNHZ3pMMzHSrPs/uKkwO/vEf7cRnitr5Avv5ASqgaPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8WEbWFpbrjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QHLoLnJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqhGluaXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uMxiAABkYgAAhJGAgIBRf7nJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqFGIAAMBXUIBRf2jyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFFGIAAK9XUGABGVEAW2AAGVlgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tZWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2ADgVKBUpBWW2AgAVFRWVCAkVBQgJBQkFZbUFCCkVBQYgAAjFaFMi4xLjCAAcAK+IagCHQOBl3W9IhcdkmZJCJrKJ+h0G8+ZeIKUZ3W5p9/Nez4YyC4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///////////////////////////////////////////hEoCepMv5i2mPg+uG17O00eQSEcTtITmpHCpUh637u7D+/4hCgNYx8viZGBiV3oOEGU/UGE8iI7mrpDHTyqMV3g4fL28/4U6A1jHy+JkYGJXeg4QZT9QYTyIjuaukMdPKoxXeDh8vbz/GghZROjYq9PBvxUPnTzCEYz2SrfoyCnx+GhIYh9gwgvwuAgICAgICAgICAgICAgIAA+ESgP3DSjD25zAArMwaf0dEudjgG8EYcZwaaAjkjHHyfdqTiIKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPhloGM6thOZLijYRlWhI1DtNsHSZiWEuuM2iB6J3yXGr9O4+EKgFP10eVCatt0NRiKeXSuu7V3KYP0hnm+0r82SijMb3vegAJ1CqCpq56K3URPlfpefmisUenslyZYFdpKVFGfMggz4tKB+IpYwy3Pj2RaOc1ysDfLyo1G1m9vh4jswaEr6qmSze/iRgICAgICAgICAoOtVWdUq0Wv+YU41YUUdTqktiDMcZUw5phNrJbwyCSOjgKBjOrYTmS4o2EZVoSNQ7TbB0mYlhLrjNogeid8lxq/TuKDETjMn5NH7D9epvLtfV5gmhktTtIvrecG1FCwMvGVOU4CAoLkHm+f8UqMm5jRrcEk0f6L+WHGLYUuGGzBloyZfnFlFgPh0oIWUTo2KvTwb8VD508whGM9kq36Mgp8fhoSGIfYMIL8L+FGgP3DSjD25zAArMwaf0dEudjgG8EYcZwaaAjkjHHyfdqSgCHQOBl3W9IhcdkmZJCJrKJ+h0G8+ZeIKUZ3W5p9/NeyAgICAgICAgICAgICAgIDAwKv+Uq4="
  },
  "tag": "poi",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
    ],
    "contracts": [
      "ct_2Ni9bJx3zsofVMsRWDXordUE967VtUQDUFRjJhcgmjFsr3QH1d"
    ]
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "poi": "pi_+Qo2PAH5AmD5Al2gPNv/jRU7QpkVR/AC6yFkvjBUcNDeD+lZA+/fNJa+G1L5Ajn41KA82/+NFTtCmRVH8ALrIWS+MFRw0N4P6VkD7980lr4bUvixgICAgICAoMHi48sUi1/4LB+jrsdcySDXzBLyQ1Igxpd91OuROuhHgICgO6m3kt68QfyfIOAH8OXUHDKqCZ7oKML9lJL3gB86PueAoMoRn+9mFPzHyQSICRLBoWdZJIYp+38gjamAztCUiKfeoKbKODEGFrja/tYvqk5+obVO1/o1hWepkepH5PQmYYvFgICggvZJrcrkjSw9RBPpSJQ6AcUSqig/h19ZC0jyJy0cWDOA+E+glzmIfR0U7CH4WQRHbilxPDxZEDhfp3xt+a1FzoVo2hbtoCC1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmi8oKAQCGP6olIl/m+EmguxLq4g2NCBS0wGuZeExxICpTesdzHr8uScpnLhT7bp7noCD9dHlQmrbdDUYinl0rru1dymD9IZ5vtK/NkoozG973hcQKAQAK+E+gweLjyxSLX/gsH6Oux1zJINfMEvJDUiDGl33U65E66EftoDccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6Ei8oKAQCGJGE5yn/8+HSgyhGf72YU/MfJBIgJEsGhZ1kkhin7fyCNqYDO0JSIp974UYCglzmIfR0U7CH4WQRHbilxPDxZEDhfp3xt+a1FzoVo2haAgKC7EuriDY0IFLTAa5l4THEgKlN6x3Mevy5JymcuFPtunoCAgICAgICAgICAgOPioAy9bSFRQ28+Bi0XgG97E1tSLa6j7E6oYsprFohKey1UwMD5B6f5B6SgfiKWMMtz49kWjnNcrA3y8qNRtZvb4eI7MGhK+qpks3v5B4D5BIGgAJ1CqCpq56K3URPlfpefmisUenslyZYFdpKVFGfMggz5BF2AoCepMv5i2mPg+uG17O00eQSEcTtITmpHCpUh637u7D+/gICAgICAgICAgICAgIC5BCr5BCcoAaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSDAwABuQP4+QP1RgKg/ukoFMi2RBUIDNHZ3pMMzHSrPs/uKkwO/vEf7cRnitr5Avv5ASqgaPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8WEbWFpbrjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QHLoLnJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqhGluaXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uMxiAABkYgAAhJGAgIBRf7nJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqFGIAAMBXUIBRf2jyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFFGIAAK9XUGABGVEAW2AAGVlgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tZWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2ADgVKBUpBWW2AgAVFRWVCAkVBQgJBQkFZbUFCCkVBQYgAAjFaFMi4xLjCAAcAK+IagCHQOBl3W9IhcdkmZJCJrKJ+h0G8+ZeIKUZ3W5p9/Nez4YyC4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///////////////////////////////////////////hEoCepMv5i2mPg+uG17O00eQSEcTtITmpHCpUh637u7D+/4hCgNYx8viZGBiV3oOEGU/UGE8iI7mrpDHTyqMV3g4fL28/4U6A1jHy+JkYGJXeg4QZT9QYTyIjuaukMdPKoxXeDh8vbz/GghZROjYq9PBvxUPnTzCEYz2SrfoyCnx+GhIYh9gwgvwuAgICAgICAgICAgICAgIAA+ESgP3DSjD25zAArMwaf0dEudjgG8EYcZwaaAjkjHHyfdqTiIKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPhloGM6thOZLijYRlWhI1DtNsHSZiWEuuM2iB6J3yXGr9O4+EKgFP10eVCatt0NRiKeXSuu7V3KYP0hnm+0r82SijMb3vegAJ1CqCpq56K3URPlfpefmisUenslyZYFdpKVFGfMggz4tKB+IpYwy3Pj2RaOc1ysDfLyo1G1m9vh4jswaEr6qmSze/iRgICAgICAgICAoOtVWdUq0Wv+YU41YUUdTqktiDMcZUw5phNrJbwyCSOjgKBjOrYTmS4o2EZVoSNQ7TbB0mYlhLrjNogeid8lxq/TuKDETjMn5NH7D9epvLtfV5gmhktTtIvrecG1FCwMvGVOU4CAoLkHm+f8UqMm5jRrcEk0f6L+WHGLYUuGGzBloyZfnFlFgPh0oIWUTo2KvTwb8VD508whGM9kq36Mgp8fhoSGIfYMIL8L+FGgP3DSjD25zAArMwaf0dEudjgG8EYcZwaaAjkjHHyfdqSgCHQOBl3W9IhcdkmZJCJrKJ+h0G8+ZeIKUZ3W5p9/NeyAgICAgICAgICAgICAgIDAwKv+Uq4="
  },
  "tag": "poi",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: accounts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: contracts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: accounts, contracts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_found",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_found",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: accounts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: contracts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: accounts, contracts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_found",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_found",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
    "code": "cb_+QW1RgKg2lZpnzaTbMnkiHSWtrDsi8S15f+OP6poqJ7cHBpu7OD5BEX4yaBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjqoLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2u4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////+QKLoOIjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEhGluaXS4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTIuMS4whY3lSg==",
    "deposit": 10,
    "vm_version": 3
  },
  "tag": "new_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+Qa3OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FLPkGbrkGa/kGaIICPQGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EgwMAAbkFuPkFtUYCoNpWaZ82k2zJ5Ih0lraw7IvEteX/jj+qaKie3Bwabuzg+QRF+MmgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD46qCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNruGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///////////////////////////////////////////kCi6DiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRIRpbml0uMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC5AaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoUyLjEuMAq4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAVoHnXp3XrAnOKS3I+pXAzGy6flXpj7c4t4HMPygcWN1zVX1nYPw==",
    "updates": [
      {
        "abi_version": 1,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
        "code": "cb_+QW1RgKg2lZpnzaTbMnkiHSWtrDsi8S15f+OP6poqJ7cHBpu7OD5BEX4yaBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjqoLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2u4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////+QKLoOIjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEhGluaXS4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTIuMS4whY3lSg==",
        "deposit": 10,
        "op": "OffChainNewContract",
        "owner": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "vm_version": 3
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
    "tx": "tx_+QcDCwH4QrhAQW6Of8vcnQNZ8hAaUrYHtQzQVfx2QW9ZOtXrPhlsjYJFKJLh91zmmkQT8D3F2276qUxcM4TFpcajbB9x4wYjBLkGuvkGtzkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSz5Bm65Bmv5BmiCAj0BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIMDAAG5Bbj5BbVGAqDaVmmfNpNsyeSIdJa2sOyLxLXl/44/qmiontwcGm7s4PkERfjJoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Oqgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGlja7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoug4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdLjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQGgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC5AUFiAACPYgAAwpGAgIBRf0nsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3FGIAATZXUICAUX/iIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRBRiAADRV1CAUX+zVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCThRiAAEbV1BgARlRAFtgABlZYCABkIFSYCCQA2AAWZCBUoFSWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW2AAUVGQVltgIAFRUZBQg5JQgJFQUIBZkIFSWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2AAWZCBUoFSWWAgAZCBUmAgkANgA4FSgVKQUJBWW1BZUFBgAFFgAWAAUVEBWZCBUpBQYABSWZBWW1BQWVBQYgAAylaFMi4xLjAKuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOIjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFaB516d16wJziktyPqVwMxsun5V6Y+3OLeBzD8oHFjdc1dewpyc="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+Qa3OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FLPkGbrkGa/kGaIICPQGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EgwMAAbkFuPkFtUYCoNpWaZ82k2zJ5Ih0lraw7IvEteX/jj+qaKie3Bwabuzg+QRF+MmgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD46qCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNruGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///////////////////////////////////////////kCi6DiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRIRpbml0uMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC5AaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoUyLjEuMAq4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAVoHnXp3XrAnOKS3I+pXAzGy6flXpj7c4t4HMPygcWN1zVX1nYPw==",
    "updates": [
      {
        "abi_version": 1,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
        "code": "cb_+QW1RgKg2lZpnzaTbMnkiHSWtrDsi8S15f+OP6poqJ7cHBpu7OD5BEX4yaBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjqoLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2u4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////+QKLoOIjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEhGluaXS4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTIuMS4whY3lSg==",
        "deposit": 10,
        "op": "OffChainNewContract",
        "owner": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "vm_version": 3
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QcDCwH4QrhAtVI0/BuzWlfD3ZrHRkj5i8pOlsqfv3FrpI+8UGjH7IV6S1xdbxqtoy++wSoheX2kIqggctumooNT0m1ZNZw/CrkGuvkGtzkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSz5Bm65Bmv5BmiCAj0BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIMDAAG5Bbj5BbVGAqDaVmmfNpNsyeSIdJa2sOyLxLXl/44/qmiontwcGm7s4PkERfjJoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Oqgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGlja7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoug4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdLjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQGgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC5AUFiAACPYgAAwpGAgIBRf0nsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3FGIAATZXUICAUX/iIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRBRiAADRV1CAUX+zVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCThRiAAEbV1BgARlRAFtgABlZYCABkIFSYCCQA2AAWZCBUoFSWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW2AAUVGQVltgIAFRUZBQg5JQgJFQUIBZkIFSWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2AAWZCBUoFSWWAgAZCBUmAgkANgA4FSgVKQUJBWW1BZUFBgAFFgAWAAUVEBWZCBUpBQYABSWZBWW1BQWVBQYgAAylaFMi4xLjAKuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOIjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFaB516d16wJziktyPqVwMxsun5V6Y+3OLeBzD8oHFjdc1Tj35b8="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QdFCwH4hLhAQW6Of8vcnQNZ8hAaUrYHtQzQVfx2QW9ZOtXrPhlsjYJFKJLh91zmmkQT8D3F2276qUxcM4TFpcajbB9x4wYjBLhAtVI0/BuzWlfD3ZrHRkj5i8pOlsqfv3FrpI+8UGjH7IV6S1xdbxqtoy++wSoheX2kIqggctumooNT0m1ZNZw/CrkGuvkGtzkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSz5Bm65Bmv5BmiCAj0BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIMDAAG5Bbj5BbVGAqDaVmmfNpNsyeSIdJa2sOyLxLXl/44/qmiontwcGm7s4PkERfjJoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Oqgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGlja7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoug4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdLjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQGgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC5AUFiAACPYgAAwpGAgIBRf0nsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3FGIAATZXUICAUX/iIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRBRiAADRV1CAUX+zVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCThRiAAEbV1BgARlRAFtgABlZYCABkIFSYCCQA2AAWZCBUoFSWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW2AAUVGQVltgIAFRUZBQg5JQgJFQUIBZkIFSWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2AAWZCBUoFSWWAgAZCBUmAgkANgA4FSgVKQUJBWW1BZUFBgAFFgAWAAUVEBWZCBUpBQYABSWZBWW1BQWVBQYgAAylaFMi4xLjAKuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOIjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFaB516d16wJziktyPqVwMxsun5V6Y+3OLeBzD8oHFjdc1eppjbg="
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
    "state": "tx_+QdFCwH4hLhAQW6Of8vcnQNZ8hAaUrYHtQzQVfx2QW9ZOtXrPhlsjYJFKJLh91zmmkQT8D3F2276qUxcM4TFpcajbB9x4wYjBLhAtVI0/BuzWlfD3ZrHRkj5i8pOlsqfv3FrpI+8UGjH7IV6S1xdbxqtoy++wSoheX2kIqggctumooNT0m1ZNZw/CrkGuvkGtzkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBSz5Bm65Bmv5BmiCAj0BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIMDAAG5Bbj5BbVGAqDaVmmfNpNsyeSIdJa2sOyLxLXl/44/qmiontwcGm7s4PkERfjJoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Oqgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGlja7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoug4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdLjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQGgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC5AUFiAACPYgAAwpGAgIBRf0nsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3FGIAATZXUICAUX/iIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRBRiAADRV1CAUX+zVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCThRiAAEbV1BgARlRAFtgABlZYCABkIFSYCCQA2AAWZCBUoFSWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW2AAUVGQVltgIAFRUZBQg5JQgJFQUIBZkIFSWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2AAWZCBUoFSWWAgAZCBUmAgkANgA4FSgVKQUJBWW1BZUFBgAFFgAWAAUVEBWZCBUpBQYABSWZBWW1BQWVBQYgAAylaFMi4xLjAKuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOIjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFaB516d16wJziktyPqVwMxsun5V6Y+3OLeBzD8oHFjdc1eppjbg="
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUt+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBfVfiomYdBNECEuLe9l3CA6FJvno1YC0QNaKKUi8Q2IeAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKDs2SPf8q1tQr9dv1m0HkPExF0oR57PSiQN1UldDFlC7Ht+rAM=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhA7odXNgcNGw+tGaXH64j5+GeWmVBIFw6qGfQ14oDhIhHoRW+7eXhhyqbGTOAvf6KezNqaXsOvnN+COGXcJGb2ArkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FLfi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg7Nkj3/KtbUK/Xb9ZtB5DxMRdKEeez0okDdVJXQxZQuxZtknr"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUt+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBfVfiomYdBNECEuLe9l3CA6FJvno1YC0QNaKKUi8Q2IeAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKDs2SPf8q1tQr9dv1m0HkPExF0oR57PSiQN1UldDFlC7Ht+rAM=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhA/GRiMS+lVc7FM5sfHQf+8NDKZzpkJFn43P+r7Q2C2yxWTYGfkNnptGIuezu9tHrcKUFNk0DcLpza0Qne9o46CrkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FLfi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg7Nkj3/KtbUK/Xb9ZtB5DxMRdKEeez0okDdVJXQxZQuyUuNJe"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhA7odXNgcNGw+tGaXH64j5+GeWmVBIFw6qGfQ14oDhIhHoRW+7eXhhyqbGTOAvf6KezNqaXsOvnN+COGXcJGb2ArhA/GRiMS+lVc7FM5sfHQf+8NDKZzpkJFn43P+r7Q2C2yxWTYGfkNnptGIuezu9tHrcKUFNk0DcLpza0Qne9o46CrkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FLfi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg7Nkj3/KtbUK/Xb9ZtB5DxMRdKEeez0okDdVJXQxZQuwYtMgm"
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
    "state": "tx_+QGLCwH4hLhA7odXNgcNGw+tGaXH64j5+GeWmVBIFw6qGfQ14oDhIhHoRW+7eXhhyqbGTOAvf6KezNqaXsOvnN+COGXcJGb2ArhA/GRiMS+lVc7FM5sfHQf+8NDKZzpkJFn43P+r7Q2C2yxWTYGfkNnptGIuezu9tHrcKUFNk0DcLpza0Qne9o46CrkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FLfi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg7Nkj3/KtbUK/Xb9ZtB5DxMRdKEeez0okDdVJXQxZQuwYtMgm"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "dry_run",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "dry_run",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "dry_run",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "dry_run",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 46,
    "contract_id": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "gas_price": 1,
    "gas_used": 220,
    "height": 46,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
  },
  "tag": "call_contract",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": 45
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 45,
    "contract_id": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "gas_price": 1,
    "gas_used": 220,
    "height": 45,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": 45
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 45,
    "contract_id": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "gas_price": 1,
    "gas_used": 220,
    "height": 45,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUu+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBfVfiomYdBNECEuLe9l3CA6FJvno1YC0QNaKKUi8Q2IeAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKBZH/70uWsEPR+br7u+55J18MFWmK8OMlSkohtT14Vg6vP8uGE=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhAUKKxFZPx0nxCYrISRBAESArTlE7bTeu+a7p8TgQMO0hkjaHZgrgIM80whV5lmChAbXC8Iw7L8Jv0c2YrczsECrkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FLvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgWR/+9LlrBD0fm6+7vueSdfDBVpivDjJUpKIbU9eFYOpD0nu2"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUu+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBfVfiomYdBNECEuLe9l3CA6FJvno1YC0QNaKKUi8Q2IeAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKBZH/70uWsEPR+br7u+55J18MFWmK8OMlSkohtT14Vg6vP8uGE=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhAX39JYSyi4hCIyKnQ10f59hUA0RrqbfJPvU9mDWjw/bnIELOM4E+3GzCsTxgTCMnMpbGUgv2v12aCYhj8Cs0JD7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FLvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgWR/+9LlrBD0fm6+7vueSdfDBVpivDjJUpKIbU9eFYOoWXfVv"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAUKKxFZPx0nxCYrISRBAESArTlE7bTeu+a7p8TgQMO0hkjaHZgrgIM80whV5lmChAbXC8Iw7L8Jv0c2YrczsECrhAX39JYSyi4hCIyKnQ10f59hUA0RrqbfJPvU9mDWjw/bnIELOM4E+3GzCsTxgTCMnMpbGUgv2v12aCYhj8Cs0JD7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FLvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgWR/+9LlrBD0fm6+7vueSdfDBVpivDjJUpKIbU9eFYOr66Scs"
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
    "state": "tx_+QGLCwH4hLhAUKKxFZPx0nxCYrISRBAESArTlE7bTeu+a7p8TgQMO0hkjaHZgrgIM80whV5lmChAbXC8Iw7L8Jv0c2YrczsECrhAX39JYSyi4hCIyKnQ10f59hUA0RrqbfJPvU9mDWjw/bnIELOM4E+3GzCsTxgTCMnMpbGUgv2v12aCYhj8Cs0JD7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FLvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgWR/+9LlrBD0fm6+7vueSdfDBVpivDjJUpKIbU9eFYOr66Scs"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUv+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBfVfiomYdBNECEuLe9l3CA6FJvno1YC0QNaKKUi8Q2IeAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKC3Sz4oydA1zW7ORAyYANO4KKAZG+AIPASlneNNfWdEjgBZdRo=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhA6d6x3q9IX9HvNf6uQjzsmPPzmjZNStgaRJX/zCOmKU+OmaKyLvYDxMKwWH9L8uca60ZD09hWUuRaTND0A22eBLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FL/i2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgt0s+KMnQNc1uzkQMmADTuCigGRvgCDwEpZ3jTX1nRI7MaseN"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUv+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBfVfiomYdBNECEuLe9l3CA6FJvno1YC0QNaKKUi8Q2IeAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKC3Sz4oydA1zW7ORAyYANO4KKAZG+AIPASlneNNfWdEjgBZdRo=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhAEElcxtJ2aNxUusRXhopHVbrfvtygGHc2TAS5SDABTn0WzPnDfIMw77wi3iKLHwKT2Fg5agQjwRbFYFDRv1PyBrkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FL/i2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgt0s+KMnQNc1uzkQMmADTuCigGRvgCDwEpZ3jTX1nRI7LJlms"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAEElcxtJ2aNxUusRXhopHVbrfvtygGHc2TAS5SDABTn0WzPnDfIMw77wi3iKLHwKT2Fg5agQjwRbFYFDRv1PyBrhA6d6x3q9IX9HvNf6uQjzsmPPzmjZNStgaRJX/zCOmKU+OmaKyLvYDxMKwWH9L8uca60ZD09hWUuRaTND0A22eBLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FL/i2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgt0s+KMnQNc1uzkQMmADTuCigGRvgCDwEpZ3jTX1nRI57ANm7"
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
    "state": "tx_+QGLCwH4hLhAEElcxtJ2aNxUusRXhopHVbrfvtygGHc2TAS5SDABTn0WzPnDfIMw77wi3iKLHwKT2Fg5agQjwRbFYFDRv1PyBrhA6d6x3q9IX9HvNf6uQjzsmPPzmjZNStgaRJX/zCOmKU+OmaKyLvYDxMKwWH9L8uca60ZD09hWUuRaTND0A22eBLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FL/i2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgt0s+KMnQNc1uzkQMmADTuCigGRvgCDwEpZ3jTX1nRI57ANm7"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUw+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBfVfiomYdBNECEuLe9l3CA6FJvno1YC0QNaKKUi8Q2IeAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKDfnXDV88gvqZIj/eWNThqxAA6JFK46TM+x3bNFRekogG4EdQk=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhA8bhloNycmWUpD1YOielV1Wm5+UAwg3Ls4cZFVHj793Y6xYVvZsM0oBJMgd1itRB6IlUM9tc20ZCsXVkYaE7LAbkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FMPi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg351w1fPIL6mSI/3ljU4asQAOiRSuOkzPsd2zRUXpKICJsHv3"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUw+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBfVfiomYdBNECEuLe9l3CA6FJvno1YC0QNaKKUi8Q2IeAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKDfnXDV88gvqZIj/eWNThqxAA6JFK46TM+x3bNFRekogG4EdQk=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhAgjWG6p4OK5XE992n118EsQkBFxO7HFoAy+b59gWFClEJlyQkqRtnx4HJPaunjOqIHzJRhW0vsEvCNtH7SOr/ArkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FMPi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg351w1fPIL6mSI/3ljU4asQAOiRSuOkzPsd2zRUXpKICqWuL2"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": 47
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAgjWG6p4OK5XE992n118EsQkBFxO7HFoAy+b59gWFClEJlyQkqRtnx4HJPaunjOqIHzJRhW0vsEvCNtH7SOr/ArhA8bhloNycmWUpD1YOielV1Wm5+UAwg3Ls4cZFVHj793Y6xYVvZsM0oBJMgd1itRB6IlUM9tc20ZCsXVkYaE7LAbkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FMPi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg351w1fPIL6mSI/3ljU4asQAOiRSuOkzPsd2zRUXpKIBcE8A7"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 47,
    "contract_id": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "gas_price": 1,
    "gas_used": 220,
    "height": 47,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAgjWG6p4OK5XE992n118EsQkBFxO7HFoAy+b59gWFClEJlyQkqRtnx4HJPaunjOqIHzJRhW0vsEvCNtH7SOr/ArhA8bhloNycmWUpD1YOielV1Wm5+UAwg3Ls4cZFVHj793Y6xYVvZsM0oBJMgd1itRB6IlUM9tc20ZCsXVkYaE7LAbkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FMPi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg351w1fPIL6mSI/3ljU4asQAOiRSuOkzPsd2zRUXpKIBcE8A7"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": 47
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 47,
    "contract_id": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "gas_price": 1,
    "gas_used": 220,
    "height": 47,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": 48
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 48,
    "contract_id": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "gas_price": 1,
    "gas_used": 220,
    "height": 48,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": 48
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 48,
    "contract_id": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "gas_price": 1,
    "gas_used": 220,
    "height": 48,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": 45
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 45,
    "contract_id": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "gas_price": 1,
    "gas_used": 220,
    "height": 45,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": 45
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 45,
    "contract_id": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "gas_price": 1,
    "gas_used": 220,
    "height": 45,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "clean_contract_calls"
}
```

#### responder <--- node
```javascript
{
  "action": "calls_pruned",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": 45
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "call_not_found",
    "request": {
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "round": 45
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUx+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBfVfiomYdBNECEuLe9l3CA6FJvno1YC0QNaKKUi8Q2IeAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKAub45W1c+pZ/aHG+2AmMJJrHRMxfAsLzRBpLD4TZ06Q30EP68=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhAP13Bg1INTDA5XjtwAA9CqGdkcMrRQBiyXt+RVLARIRcYF1t6VAJBmJLdFl8nRJui8LLBz7+QHtzK3KZDWhBwBLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FMfi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgLm+OVtXPqWf2hxvtgJjCSax0TMXwLC80QaSw+E2dOkMxVxIx"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUx+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBfVfiomYdBNECEuLe9l3CA6FJvno1YC0QNaKKUi8Q2IeAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKAub45W1c+pZ/aHG+2AmMJJrHRMxfAsLzRBpLD4TZ06Q30EP68=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhABUAq3vPiu1GU00YewF8Cqhq3+tFsx2LJ1yuJYJvbX8aMw1r69Z0vBSKpWY1jdMOKzr4FZvbmq52Alqal1f38A7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FMfi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgLm+OVtXPqWf2hxvtgJjCSax0TMXwLC80QaSw+E2dOkNGjwq4"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhABUAq3vPiu1GU00YewF8Cqhq3+tFsx2LJ1yuJYJvbX8aMw1r69Z0vBSKpWY1jdMOKzr4FZvbmq52Alqal1f38A7hAP13Bg1INTDA5XjtwAA9CqGdkcMrRQBiyXt+RVLARIRcYF1t6VAJBmJLdFl8nRJui8LLBz7+QHtzK3KZDWhBwBLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FMfi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgLm+OVtXPqWf2hxvtgJjCSax0TMXwLC80QaSw+E2dOkOSEKSl"
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
    "state": "tx_+QGLCwH4hLhABUAq3vPiu1GU00YewF8Cqhq3+tFsx2LJ1yuJYJvbX8aMw1r69Z0vBSKpWY1jdMOKzr4FZvbmq52Alqal1f38A7hAP13Bg1INTDA5XjtwAA9CqGdkcMrRQBiyXt+RVLARIRcYF1t6VAJBmJLdFl8nRJui8LLBz7+QHtzK3KZDWhBwBLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FMfi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgLm+OVtXPqWf2hxvtgJjCSax0TMXwLC80QaSw+E2dOkOSEKSl"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "dry_run",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "dry_run",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "dry_run",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "dry_run",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 50,
    "contract_id": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "gas_price": 1,
    "gas_used": 220,
    "height": 50,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
  },
  "tag": "call_contract",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": 49
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 49,
    "contract_id": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "gas_price": 1,
    "gas_used": 220,
    "height": 49,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": 49
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 49,
    "contract_id": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "gas_price": 1,
    "gas_used": 220,
    "height": 49,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUy+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBfVfiomYdBNECEuLe9l3CA6FJvno1YC0QNaKKUi8Q2IeAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKCrzzFKPj42p7mhdNDtmcd+7/TsHyCi2BLHY46XVmT76F56X5s=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhAaRgomFuTXKgmxzu1xPmG47M1fIyu/CBohZIxiTKiqYA94O4cVd/OCwqUiuUNYR04xDcXgCx4qOXmN32y2pZuC7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FMvi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgq88xSj4+Nqe5oXTQ7ZnHfu/07B8gotgSx2OOl1Zk++jG9Y9Z"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUy+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBfVfiomYdBNECEuLe9l3CA6FJvno1YC0QNaKKUi8Q2IeAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKCrzzFKPj42p7mhdNDtmcd+7/TsHyCi2BLHY46XVmT76F56X5s=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhAeURmtCEmg7f/DwcI4uPiMT4OPAiVabYC663SNfTyyRoEIka7wNG37TIeZv0Bc9+IOrPEVqk7coHoRBj88JmvCLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FMvi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgq88xSj4+Nqe5oXTQ7ZnHfu/07B8gotgSx2OOl1Zk++jBi4ih"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAaRgomFuTXKgmxzu1xPmG47M1fIyu/CBohZIxiTKiqYA94O4cVd/OCwqUiuUNYR04xDcXgCx4qOXmN32y2pZuC7hAeURmtCEmg7f/DwcI4uPiMT4OPAiVabYC663SNfTyyRoEIka7wNG37TIeZv0Bc9+IOrPEVqk7coHoRBj88JmvCLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FMvi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgq88xSj4+Nqe5oXTQ7ZnHfu/07B8gotgSx2OOl1Zk++jSVefN"
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
    "state": "tx_+QGLCwH4hLhAaRgomFuTXKgmxzu1xPmG47M1fIyu/CBohZIxiTKiqYA94O4cVd/OCwqUiuUNYR04xDcXgCx4qOXmN32y2pZuC7hAeURmtCEmg7f/DwcI4uPiMT4OPAiVabYC663SNfTyyRoEIka7wNG37TIeZv0Bc9+IOrPEVqk7coHoRBj88JmvCLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FMvi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgq88xSj4+Nqe5oXTQ7ZnHfu/07B8gotgSx2OOl1Zk++jSVefN"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUz+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBfVfiomYdBNECEuLe9l3CA6FJvno1YC0QNaKKUi8Q2IeAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKDyi77eyJLW5ZC10WHmwuXxLR4y0bRGSCqBvOqPuqKFQtmS/+k=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhAoNOoA6M5ZVg8+q6SNOBSCgTaf8xfyDAJx+WC3/9ev9Qhp+uJEyYvvUXCrwNnMo+hoSriHpAgwte7qoznITsRCbkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FM/i2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg8ou+3siS1uWQtdFh5sLl8S0eMtG0Rkgqgbzqj7qihULkil7d"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgUz+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBfVfiomYdBNECEuLe9l3CA6FJvno1YC0QNaKKUi8Q2IeAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKDyi77eyJLW5ZC10WHmwuXxLR4y0bRGSCqBvOqPuqKFQtmS/+k=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhABxb8XqpevFyV46JR1vVhGnoi1D+Ah12HtbfIM0gOZhHeauO+U2tPD0ufGI5/nQvPXQ9UGn6m3h8jGAHBl/25ArkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FM/i2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg8ou+3siS1uWQtdFh5sLl8S0eMtG0Rkgqgbzqj7qihUJT6wrl"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhABxb8XqpevFyV46JR1vVhGnoi1D+Ah12HtbfIM0gOZhHeauO+U2tPD0ufGI5/nQvPXQ9UGn6m3h8jGAHBl/25ArhAoNOoA6M5ZVg8+q6SNOBSCgTaf8xfyDAJx+WC3/9ev9Qhp+uJEyYvvUXCrwNnMo+hoSriHpAgwte7qoznITsRCbkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FM/i2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg8ou+3siS1uWQtdFh5sLl8S0eMtG0Rkgqgbzqj7qihULatiod"
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
    "state": "tx_+QGLCwH4hLhABxb8XqpevFyV46JR1vVhGnoi1D+Ah12HtbfIM0gOZhHeauO+U2tPD0ufGI5/nQvPXQ9UGn6m3h8jGAHBl/25ArhAoNOoA6M5ZVg8+q6SNOBSCgTaf8xfyDAJx+WC3/9ev9Qhp+uJEyYvvUXCrwNnMo+hoSriHpAgwte7qoznITsRCbkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FM/i2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg8ou+3siS1uWQtdFh5sLl8S0eMtG0Rkgqgbzqj7qihULatiod"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgU0+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBfVfiomYdBNECEuLe9l3CA6FJvno1YC0QNaKKUi8Q2IeAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKBkDJcB1oeZ1k158MWueaKgG6YBO4FpSgAVlT+sOww13d6o3/w=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhAHOBDS8f0MAjPEsm4M6ruJqXHfqvITkKpdHFJu5Tkt/FRi7dVBc1kDBaBOkQ8XK2bwhlICMKQ5b0L/JMjNhmDArkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FNPi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgZAyXAdaHmdZNefDFrnmioBumATuBaUoAFZU/rDsMNd30l2Ae"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgU0+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBfVfiomYdBNECEuLe9l3CA6FJvno1YC0QNaKKUi8Q2IeAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKBkDJcB1oeZ1k158MWueaKgG6YBO4FpSgAVlT+sOww13d6o3/w=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhAXuNrnXtMT8oWFAxO/KbTdDaMF9LHXTwZQwSR3FWWYg/0Je6pcNT7irhgCgXdqzfedUnneMHU+tiGgWOempnlDLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FNPi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgZAyXAdaHmdZNefDFrnmioBumATuBaUoAFZU/rDsMNd3494KQ"
  }
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": 51
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAHOBDS8f0MAjPEsm4M6ruJqXHfqvITkKpdHFJu5Tkt/FRi7dVBc1kDBaBOkQ8XK2bwhlICMKQ5b0L/JMjNhmDArhAXuNrnXtMT8oWFAxO/KbTdDaMF9LHXTwZQwSR3FWWYg/0Je6pcNT7irhgCgXdqzfedUnneMHU+tiGgWOempnlDLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FNPi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgZAyXAdaHmdZNefDFrnmioBumATuBaUoAFZU/rDsMNd3mFdBh"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 51,
    "contract_id": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "gas_price": 1,
    "gas_used": 220,
    "height": 51,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": 51
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAHOBDS8f0MAjPEsm4M6ruJqXHfqvITkKpdHFJu5Tkt/FRi7dVBc1kDBaBOkQ8XK2bwhlICMKQ5b0L/JMjNhmDArhAXuNrnXtMT8oWFAxO/KbTdDaMF9LHXTwZQwSR3FWWYg/0Je6pcNT7irhgCgXdqzfedUnneMHU+tiGgWOempnlDLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FNPi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX1X4qJmHQTRAhLi3vZdwgOhSb56NWAtEDWiilIvENiHgEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgZAyXAdaHmdZNefDFrnmioBumATuBaUoAFZU/rDsMNd3mFdBh"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 51,
    "contract_id": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "gas_price": 1,
    "gas_used": 220,
    "height": 51,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": 52
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 52,
    "contract_id": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "gas_price": 1,
    "gas_used": 220,
    "height": 52,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "round": 52
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 52,
    "contract_id": "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD",
    "gas_price": 1,
    "gas_used": 220,
    "height": 52,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
    ],
    "contracts": [
      "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
    ]
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "poi": "pi_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////////////////////////////////+QKLoOIjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEhGluaXS4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTIuMS4wgAHACvjmoMMN5omVEejhhfhAqs9cOijYD5ArIrSxrLGPPIGxA0Z3+MMguMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD4U6DNpoitZLgFQ639Ks3Yk7qiD+s/hNmS96KJ0HTDHyCd6fGgSBEeVwu8cW7q/gUKtI9BT7SQXY1Hq9ywIfX9gYKO8UWAgICAgICAgICAgICAgIAA+HSg6Np8INAl7xUhh/f9Z2sUmSll4pCLp9m/t8f7B8T2lOL4UYCAgICAoEujI+gxCXvkukn7jGamYQCUpcfH+Qf/tuT/mZFj5yQFgICAgKB/E88D35DavlOERrYjdrTcsh3dmKFqoi+e34QJ7o7/VYCAgICAgPi0oPuj4LnUFdZiktkWvtHf6FmxXwKJh29KNXI0UDbWOfLN+JGAgICAgICAgICg61VZ1SrRa/5hTjVhRR1OqS2IMxxlTDmmE2slvDIJI6OAoGM6thOZLijYRlWhI1DtNsHSZiWEuuM2iB6J3yXGr9O4oMROMyfk0fsP16m8u19XmCaGS1O0i+t5wbUULAy8ZU5TgICg6Np8INAl7xUhh/f9Z2sUmSll4pCLp9m/t8f7B8T2lOKAwMDqr76t"
  },
  "tag": "poi",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
    ],
    "contracts": [
      "ct_2s4jJFBMJYFMBv1mdTtBB9WYTKr4bKzpfvo4UVauy6DdRSqzcD"
    ]
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "poi": "pi_+Q1kPAH5Atb5AtOgzCHi4DGvUhfQA0kxcosamxiqM0hDrN32ef3G1b4QhMX5Aq/4SaBGRQz1M2ueBzAqFsUjzIP6Rvz1YasQZUe7+X60yT/1H+egIF+KiZh0E0QIS4t72XcIDoUm+ejVgLRA1oopSLxDYh6FxAoBAAr4T6CAiHNqg4ZVqicfI3Qu9MEXLVnpbH7LTbVLWy23yNIV6u2gNxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKf/L4T6CXOYh9HRTsIfhZBEduKXE8PFkQOF+nfG35rUXOhWjaFu2gILV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aLygoBAIY/qiUiX+b4dKCuXv9F7cAwbIrdqPli89O8XNsF4pktMqE38lYJJkXLcvhRgICAgICgRkUM9TNrngcwKhbFI8yD+kb89WGrEGVHu/l+tMk/9R+AgICAoN+ZN2893FICpEUSqIVRnSeJ1C3J4Lo6vMr6MGRbdQrhgICAgICA+HSgyhGf72YU/MfJBIgJEsGhZ1kkhin7fyCNqYDO0JSIp974UYCglzmIfR0U7CH4WQRHbilxPDxZEDhfp3xt+a1FzoVo2haAgKC7EuriDY0IFLTAa5l4THEgKlN6x3Mevy5JymcuFPtunoCAgICAgICAgICAgPjUoMwh4uAxr1IX0ANJMXKLGpsYqjNIQ6zd9nn9xtW+EITF+LGAgICAgICggIhzaoOGVaonHyN0LvTBFy1Z6Wx+y021S1stt8jSFeqAgKA7qbeS3rxB/J8g4Afw5dQcMqoJnugowv2UkveAHzo+54CgyhGf72YU/MfJBIgJEsGhZ1kkhin7fyCNqYDO0JSIp96gpso4MQYWuNr+1i+qTn6htU7X+jWFZ6mR6kfk9CZhi8WAgKCuXv9F7cAwbIrdqPli89O8XNsF4pktMqE38lYJJkXLcoDj4qBUOUykZzg2/WuVaFvphDP5pkxqCLvy7B4oyi4wbYz+KcDA+Qpf+QpcoPuj4LnUFdZiktkWvtHf6FmxXwKJh29KNXI0UDbWOfLN+Qo4+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+HSgSBEeVwu8cW7q/gUKtI9BT7SQXY1Hq9ywIfX9gYKO8UX4UaAVaiNPbxb1nROfE0C66bQnbZgclArLhJIVIS1S0xfBX6DDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd4CAgICAgICAgICAgICAgPhloEujI+gxCXvkukn7jGamYQCUpcfH+Qf/tuT/mZFj5yQF+EKgAF+KiZh0E0QIS4t72XcIDoUm+ejVgLRA1oopSLxDYh6gjyj9QATjpJb1kbkTzTuTrdAkKSJkNAlu54PesVgelxP5BkGgjyj9QATjpJb1kbkTzTuTrdAkKSJkNAlu54PesVgelxP5Bh2AoB3cqLle1ryvDXI00L62hGL8UKTN2Cnd3VxpFOi9gdiMgICAgICAgICAgICAgIC5Ber5BecoAaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSDAwABuQW4+QW1RgKg2lZpnzaTbMnkiHSWtrDsi8S15f+OP6poqJ7cHBpu7OD5BEX4yaBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjqoLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2u4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////+QKLoOIjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEhGluaXS4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTIuMS4wgAHACvjmoMMN5omVEejhhfhAqs9cOijYD5ArIrSxrLGPPIGxA0Z3+MMguMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD4U6DNpoitZLgFQ639Ks3Yk7qiD+s/hNmS96KJ0HTDHyCd6fGgSBEeVwu8cW7q/gUKtI9BT7SQXY1Hq9ywIfX9gYKO8UWAgICAgICAgICAgICAgIAA+HSg6Np8INAl7xUhh/f9Z2sUmSll4pCLp9m/t8f7B8T2lOL4UYCAgICAoEujI+gxCXvkukn7jGamYQCUpcfH+Qf/tuT/mZFj5yQFgICAgKB/E88D35DavlOERrYjdrTcsh3dmKFqoi+e34QJ7o7/VYCAgICAgPi0oPuj4LnUFdZiktkWvtHf6FmxXwKJh29KNXI0UDbWOfLN+JGAgICAgICAgICg61VZ1SrRa/5hTjVhRR1OqS2IMxxlTDmmE2slvDIJI6OAoGM6thOZLijYRlWhI1DtNsHSZiWEuuM2iB6J3yXGr9O4oMROMyfk0fsP16m8u19XmCaGS1O0i+t5wbUULAy8ZU5TgICg6Np8INAl7xUhh/f9Z2sUmSll4pCLp9m/t8f7B8T2lOKAwMDqr76t"
  },
  "tag": "poi",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: accounts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: contracts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: accounts, contracts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_found",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_found",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: accounts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: contracts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: accounts, contracts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_found",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_found",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAnHQYrA==",
    "code": "cb_+Q08RgKgnah8HG5i8Hcxgqfpf/YViaWsF9xn5gugEO9fcFC8+zj5CiP40aAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDItnZXRfYmFsYW5jZbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QGUoChhWzgmK00kF7owGlfTf0IXbL47tExEq9XJIHKPxqNpjXdpdGhkcmF3X2Zyb225ASAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AS6gR7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsiId2l0aGRyYXe4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPkB8aCJoaWWu46V2xUXMZ+Awz3MUZ7rpQAgWjmdn5mpfOadD4pzcGVuZF9mcm9tuQGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QGMoIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nhXNwZW5kuQEgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QHLoLnJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqhGluaXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////+QE0oNa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13jmdldF9iYWxhbmNlX29muMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC5AupiAAE7YgABW5GAgIBRf7nJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqFGIAAq9XUICAUX/Wv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdxRiAAGGV1CAgFF/KGFbOCYrTSQXujAaV9N/Qhdsvju0TESr1ckgco/Go2kUYgABmldQgIBRf0e3vKexm5ojL3PjvxoQ1lkZj3AJxG2zefBnFvmGfxrIFGIAArtXUICAUX+MC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpxRiAALOV1CAgFF/iaGllruOldsVFzGfgMM9zFGe66UAIFo5nZ+ZqXzmnQ8UYgACI1dQgFF/JSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwUYgACpldQYAEZUQBbYAAZWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW1lZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYAOBUoFSkFZbYCABUVGQUFlQgJFQUIAxkFCQVltgIAFRgFGQYCABUZFQWVCAgpJQklBQYABgAGAAg1mQgVJZYCABkIFSYCCQA39Ht7ynsZuaIy9z478aENZZGY9wCcRts3nwZxb5hn8ayIFSYACGWvFQgJFQUFszgZCRUFswMWAAYABgAIVZYCABkIFSYCCQA2ABgVKFYABa8VCBgQOQUJFQUJBWW2AgAVGAUZBgIAGAUZBgIAFRklBZUIGBhJNQk1CTUFBgAGAAYACDWZCBUllgIAGQgVJgIJADf0e3vKexm5ojL3PjvxoQ1lkZj3AJxG2zefBnFvmGfxrIgVJgAIda8VBgAGAAYACEWWAgAZCBUmAgkANgAYFShGAAWvFQgTGSUFBQkFZbUFlQUDAxkFZbUFCCkVBQYgABY1ZbYCABUVGQUFlQgJFQUGIAAfRWW2AgAVGAUZBgIAFRkVBZUICCklCSUFBiAAH6VoUyLjEuMFpia+4=",
    "deposit": 10,
    "vm_version": 3
  },
  "tag": "new_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_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AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPkBy6C5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6oRpbml0uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+5AUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///////////////////////////////////////////kBNKDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtd45nZXRfYmFsYW5jZV9vZrjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQLqYgABO2IAAVuRgICAUX+5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6hRiAAKvV1CAgFF/1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcUYgABhldQgIBRfyhhWzgmK00kF7owGlfTf0IXbL47tExEq9XJIHKPxqNpFGIAAZpXUICAUX9Ht7ynsZuaIy9z478aENZZGY9wCcRts3nwZxb5hn8ayBRiAAK7V1CAgFF/jAt2+/jT3WJAx/X8mmqIq5idH48B7FqmRC/tWic4jqcUYgACzldQgIBRf4mhpZa7jpXbFRcxn4DDPcxRnuulACBaOZ2fmal85p0PFGIAAiNXUIBRfyUk52A6qQ/AUHbqdi5s6si+bkOFHZWVHBXYWCmXOFkMFGIAAqZXUGABGVEAW2AAGVlgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tZWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2ADgVKBUpBWW2AgAVFRkFBZUICRUFCAMZBQkFZbYCABUYBRkGAgAVGRUFlQgIKSUJJQUGAAYABgAINZkIFSWWAgAZCBUmAgkAN/R7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsiBUmAAhlrxUICRUFBbM4GQkVBbMDFgAGAAYACFWWAgAZCBUmAgkANgAYFShWAAWvFQgYEDkFCRUFCQVltgIAFRgFGQYCABgFGQYCABUZJQWVCBgYSTUJNQk1BQYABgAGAAg1mQgVJZYCABkIFSYCCQA39Ht7ynsZuaIy9z478aENZZGY9wCcRts3nwZxb5hn8ayIFSYACHWvFQYABgAGAAhFlgIAGQgVJgIJADYAGBUoRgAFrxUIExklBQUJBWW1BZUFAwMZBWW1BQgpFQUGIAAWNWW2AgAVFRkFBZUICRUFBiAAH0VltgIAFRgFGQYCABUZFQWVCAgpJQklBQYgAB+laFMi4xLjAKuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILnJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgoZ3qzCeYnxPYfxqz6YpjAX7E+caqeSgD169OqyYqlz2ekFoi",
    "updates": [
      {
        "abi_version": 1,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAnHQYrA==",
        "code": "cb_+Q08RgKgnah8HG5i8Hcxgqfpf/YViaWsF9xn5gugEO9fcFC8+zj5CiP40aAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDItnZXRfYmFsYW5jZbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QGUoChhWzgmK00kF7owGlfTf0IXbL47tExEq9XJIHKPxqNpjXdpdGhkcmF3X2Zyb225ASAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AS6gR7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsiId2l0aGRyYXe4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPkB8aCJoaWWu46V2xUXMZ+Awz3MUZ7rpQAgWjmdn5mpfOadD4pzcGVuZF9mcm9tuQGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QGMoIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nhXNwZW5kuQEgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QHLoLnJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqhGluaXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////+QE0oNa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13jmdldF9iYWxhbmNlX29muMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC5AupiAAE7YgABW5GAgIBRf7nJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqFGIAAq9XUICAUX/Wv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdxRiAAGGV1CAgFF/KGFbOCYrTSQXujAaV9N/Qhdsvju0TESr1ckgco/Go2kUYgABmldQgIBRf0e3vKexm5ojL3PjvxoQ1lkZj3AJxG2zefBnFvmGfxrIFGIAArtXUICAUX+MC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpxRiAALOV1CAgFF/iaGllruOldsVFzGfgMM9zFGe66UAIFo5nZ+ZqXzmnQ8UYgACI1dQgFF/JSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwUYgACpldQYAEZUQBbYAAZWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW1lZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYAOBUoFSkFZbYCABUVGQUFlQgJFQUIAxkFCQVltgIAFRgFGQYCABUZFQWVCAgpJQklBQYABgAGAAg1mQgVJZYCABkIFSYCCQA39Ht7ynsZuaIy9z478aENZZGY9wCcRts3nwZxb5hn8ayIFSYACGWvFQgJFQUFszgZCRUFswMWAAYABgAIVZYCABkIFSYCCQA2ABgVKFYABa8VCBgQOQUJFQUJBWW2AgAVGAUZBgIAGAUZBgIAFRklBZUIGBhJNQk1CTUFBgAGAAYACDWZCBUllgIAGQgVJgIJADf0e3vKexm5ojL3PjvxoQ1lkZj3AJxG2zefBnFvmGfxrIgVJgAIda8VBgAGAAYACEWWAgAZCBUmAgkANgAYFShGAAWvFQgTGSUFBQkFZbUFlQUDAxkFZbUFCCkVBQYgABY1ZbYCABUVGQUFlQgJFQUGIAAfRWW2AgAVGAUZBgIAFRkVBZUICCklCSUFBiAAH6VoUyLjEuMFpia+4=",
        "deposit": 10,
        "op": "OffChainNewContract",
        "owner": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "vm_version": 3
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
    "tx": "tx_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AAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AcuguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeqEaW5pdLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5ATSg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXeOZ2V0X2JhbGFuY2Vfb2a4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkC6mIAATtiAAFbkYCAgFF/uclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoUYgACr1dQgIBRf9a/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13FGIAAYZXUICAUX8oYVs4JitNJBe6MBpX039CF2y+O7RMRKvVySByj8ajaRRiAAGaV1CAgFF/R7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsgUYgACu1dQgIBRf4wLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nFGIAAs5XUICAUX+JoaWWu46V2xUXMZ+Awz3MUZ7rpQAgWjmdn5mpfOadDxRiAAIjV1CAUX8lJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDBRiAAKmV1BgARlRAFtgABlZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbWVlgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgA4FSgVKQVltgIAFRUZBQWVCAkVBQgDGQUJBWW2AgAVGAUZBgIAFRkVBZUICCklCSUFBgAGAAYACDWZCBUllgIAGQgVJgIJADf0e3vKexm5ojL3PjvxoQ1lkZj3AJxG2zefBnFvmGfxrIgVJgAIZa8VCAkVBQWzOBkJFQWzAxYABgAGAAhVlgIAGQgVJgIJADYAGBUoVgAFrxUIGBA5BQkVBQkFZbYCABUYBRkGAgAYBRkGAgAVGSUFlQgYGEk1CTUJNQUGAAYABgAINZkIFSWWAgAZCBUmAgkAN/R7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsiBUmAAh1rxUGAAYABgAIRZYCABkIFSYCCQA2ABgVKEYABa8VCBMZJQUFCQVltQWVBQMDGQVltQUIKRUFBiAAFjVltgIAFRUZBQWVCAkVBQYgAB9FZbYCABUYBRkGAgAVGRUFlQgIKSUJJQUGIAAfpWhTIuMS4wCrhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoKGd6swnmJ8T2H8as+mKYwF+xPnGqnkoA9evTqsmKpc9IVh87g=="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_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AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPkBy6C5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6oRpbml0uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+5AUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///////////////////////////////////////////kBNKDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtd45nZXRfYmFsYW5jZV9vZrjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQLqYgABO2IAAVuRgICAUX+5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6hRiAAKvV1CAgFF/1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcUYgABhldQgIBRfyhhWzgmK00kF7owGlfTf0IXbL47tExEq9XJIHKPxqNpFGIAAZpXUICAUX9Ht7ynsZuaIy9z478aENZZGY9wCcRts3nwZxb5hn8ayBRiAAK7V1CAgFF/jAt2+/jT3WJAx/X8mmqIq5idH48B7FqmRC/tWic4jqcUYgACzldQgIBRf4mhpZa7jpXbFRcxn4DDPcxRnuulACBaOZ2fmal85p0PFGIAAiNXUIBRfyUk52A6qQ/AUHbqdi5s6si+bkOFHZWVHBXYWCmXOFkMFGIAAqZXUGABGVEAW2AAGVlgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tZWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2ADgVKBUpBWW2AgAVFRkFBZUICRUFCAMZBQkFZbYCABUYBRkGAgAVGRUFlQgIKSUJJQUGAAYABgAINZkIFSWWAgAZCBUmAgkAN/R7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsiBUmAAhlrxUICRUFBbM4GQkVBbMDFgAGAAYACFWWAgAZCBUmAgkANgAYFShWAAWvFQgYEDkFCRUFCQVltgIAFRgFGQYCABgFGQYCABUZJQWVCBgYSTUJNQk1BQYABgAGAAg1mQgVJZYCABkIFSYCCQA39Ht7ynsZuaIy9z478aENZZGY9wCcRts3nwZxb5hn8ayIFSYACHWvFQYABgAGAAhFlgIAGQgVJgIJADYAGBUoRgAFrxUIExklBQUJBWW1BZUFAwMZBWW1BQgpFQUGIAAWNWW2AgAVFRkFBZUICRUFBiAAH0VltgIAFRgFGQYCABUZFQWVCAgpJQklBQYgAB+laFMi4xLjAKuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAILnJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgoZ3qzCeYnxPYfxqz6YpjAX7E+caqeSgD169OqyYqlz2ekFoi",
    "updates": [
      {
        "abi_version": 1,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAnHQYrA==",
        "code": "cb_+Q08RgKgnah8HG5i8Hcxgqfpf/YViaWsF9xn5gugEO9fcFC8+zj5CiP40aAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDItnZXRfYmFsYW5jZbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QGUoChhWzgmK00kF7owGlfTf0IXbL47tExEq9XJIHKPxqNpjXdpdGhkcmF3X2Zyb225ASAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AS6gR7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsiId2l0aGRyYXe4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPkB8aCJoaWWu46V2xUXMZ+Awz3MUZ7rpQAgWjmdn5mpfOadD4pzcGVuZF9mcm9tuQGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QGMoIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nhXNwZW5kuQEgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QHLoLnJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqhGluaXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////+QE0oNa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13jmdldF9iYWxhbmNlX29muMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC5AupiAAE7YgABW5GAgIBRf7nJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqFGIAAq9XUICAUX/Wv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdxRiAAGGV1CAgFF/KGFbOCYrTSQXujAaV9N/Qhdsvju0TESr1ckgco/Go2kUYgABmldQgIBRf0e3vKexm5ojL3PjvxoQ1lkZj3AJxG2zefBnFvmGfxrIFGIAArtXUICAUX+MC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpxRiAALOV1CAgFF/iaGllruOldsVFzGfgMM9zFGe66UAIFo5nZ+ZqXzmnQ8UYgACI1dQgFF/JSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwUYgACpldQYAEZUQBbYAAZWWAgAZCBUmAgkANgA4FSkFlgAFFZUmAAUmAA81tgAIBSYADzW1lZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYAOBUoFSkFZbYCABUVGQUFlQgJFQUIAxkFCQVltgIAFRgFGQYCABUZFQWVCAgpJQklBQYABgAGAAg1mQgVJZYCABkIFSYCCQA39Ht7ynsZuaIy9z478aENZZGY9wCcRts3nwZxb5hn8ayIFSYACGWvFQgJFQUFszgZCRUFswMWAAYABgAIVZYCABkIFSYCCQA2ABgVKFYABa8VCBgQOQUJFQUJBWW2AgAVGAUZBgIAGAUZBgIAFRklBZUIGBhJNQk1CTUFBgAGAAYACDWZCBUllgIAGQgVJgIJADf0e3vKexm5ojL3PjvxoQ1lkZj3AJxG2zefBnFvmGfxrIgVJgAIda8VBgAGAAYACEWWAgAZCBUmAgkANgAYFShGAAWvFQgTGSUFBQkFZbUFlQUDAxkFZbUFCCkVBQYgABY1ZbYCABUVGQUFlQgJFQUGIAAfRWW2AgAVGAUZBgIAFRkVBZUICCklCSUFBiAAH6VoUyLjEuMFpia+4=",
        "deposit": 10,
        "op": "OffChainNewContract",
        "owner": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "vm_version": 3
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_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AAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AcuguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeqEaW5pdLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5ATSg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXeOZ2V0X2JhbGFuY2Vfb2a4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkC6mIAATtiAAFbkYCAgFF/uclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoUYgACr1dQgIBRf9a/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13FGIAAYZXUICAUX8oYVs4JitNJBe6MBpX039CF2y+O7RMRKvVySByj8ajaRRiAAGaV1CAgFF/R7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsgUYgACu1dQgIBRf4wLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nFGIAAs5XUICAUX+JoaWWu46V2xUXMZ+Awz3MUZ7rpQAgWjmdn5mpfOadDxRiAAIjV1CAUX8lJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDBRiAAKmV1BgARlRAFtgABlZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbWVlgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgA4FSgVKQVltgIAFRUZBQWVCAkVBQgDGQUJBWW2AgAVGAUZBgIAFRkVBZUICCklCSUFBgAGAAYACDWZCBUllgIAGQgVJgIJADf0e3vKexm5ojL3PjvxoQ1lkZj3AJxG2zefBnFvmGfxrIgVJgAIZa8VCAkVBQWzOBkJFQWzAxYABgAGAAhVlgIAGQgVJgIJADYAGBUoVgAFrxUIGBA5BQkVBQkFZbYCABUYBRkGAgAYBRkGAgAVGSUFlQgYGEk1CTUJNQUGAAYABgAINZkIFSWWAgAZCBUmAgkAN/R7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsiBUmAAh1rxUGAAYABgAIRZYCABkIFSYCCQA2ABgVKEYABa8VCBMZJQUFCQVltQWVBQMDGQVltQUIKRUFBiAAFjVltgIAFRUZBQWVCAkVBQYgAB9FZbYCABUYBRkGAgAVGRUFlQgIKSUJJQUGIAAfpWhTIuMS4wCrhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoKGd6swnmJ8T2H8as+mKYwF+xPnGqnkoA9evTqsmKpc9uw8NBw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_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AAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AcuguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeqEaW5pdLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5ATSg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXeOZ2V0X2JhbGFuY2Vfb2a4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkC6mIAATtiAAFbkYCAgFF/uclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoUYgACr1dQgIBRf9a/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13FGIAAYZXUICAUX8oYVs4JitNJBe6MBpX039CF2y+O7RMRKvVySByj8ajaRRiAAGaV1CAgFF/R7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsgUYgACu1dQgIBRf4wLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nFGIAAs5XUICAUX+JoaWWu46V2xUXMZ+Awz3MUZ7rpQAgWjmdn5mpfOadDxRiAAIjV1CAUX8lJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDBRiAAKmV1BgARlRAFtgABlZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbWVlgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgA4FSgVKQVltgIAFRUZBQWVCAkVBQgDGQUJBWW2AgAVGAUZBgIAFRkVBZUICCklCSUFBgAGAAYACDWZCBUllgIAGQgVJgIJADf0e3vKexm5ojL3PjvxoQ1lkZj3AJxG2zefBnFvmGfxrIgVJgAIZa8VCAkVBQWzOBkJFQWzAxYABgAGAAhVlgIAGQgVJgIJADYAGBUoVgAFrxUIGBA5BQkVBQkFZbYCABUYBRkGAgAYBRkGAgAVGSUFlQgYGEk1CTUJNQUGAAYABgAINZkIFSWWAgAZCBUmAgkAN/R7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsiBUmAAh1rxUGAAYABgAIRZYCABkIFSYCCQA2ABgVKEYABa8VCBMZJQUFCQVltQWVBQMDGQVltQUIKRUFBiAAFjVltgIAFRUZBQWVCAkVBQYgAB9FZbYCABUYBRkGAgAVGRUFlQgIKSUJJQUGIAAfpWhTIuMS4wCrhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoKGd6swnmJ8T2H8as+mKYwF+xPnGqnkoA9evTqsmKpc9+dnvjw=="
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
    "state": "tx_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AAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD5AcuguclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeqEaW5pdLhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5ATSg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXeOZ2V0X2JhbGFuY2Vfb2a4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkC6mIAATtiAAFbkYCAgFF/uclW8osxSan1mHqlBfPaGyIJzFc5I0AGK7bBvZ+fmeoUYgACr1dQgIBRf9a/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13FGIAAYZXUICAUX8oYVs4JitNJBe6MBpX039CF2y+O7RMRKvVySByj8ajaRRiAAGaV1CAgFF/R7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsgUYgACu1dQgIBRf4wLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nFGIAAs5XUICAUX+JoaWWu46V2xUXMZ+Awz3MUZ7rpQAgWjmdn5mpfOadDxRiAAIjV1CAUX8lJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDBRiAAKmV1BgARlRAFtgABlZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbWVlgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgA4FSgVKQVltgIAFRUZBQWVCAkVBQgDGQUJBWW2AgAVGAUZBgIAFRkVBZUICCklCSUFBgAGAAYACDWZCBUllgIAGQgVJgIJADf0e3vKexm5ojL3PjvxoQ1lkZj3AJxG2zefBnFvmGfxrIgVJgAIZa8VCAkVBQWzOBkJFQWzAxYABgAGAAhVlgIAGQgVJgIJADYAGBUoVgAFrxUIGBA5BQkVBQkFZbYCABUYBRkGAgAYBRkGAgAVGSUFlQgYGEk1CTUJNQUGAAYABgAINZkIFSWWAgAZCBUmAgkAN/R7e8p7GbmiMvc+O/GhDWWRmPcAnEbbN58GcW+YZ/GsiBUmAAh1rxUGAAYABgAIRZYCABkIFSYCCQA2ABgVKEYABa8VCBMZJQUFCQVltQWVBQMDGQVltQUIKRUFBiAAFjVltgIAFRUZBQWVCAkVBQYgAB9FZbYCABUYBRkGAgAVGRUFlQgIKSUJJQUGIAAfpWhTIuMS4wCrhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoKGd6swnmJ8T2H8as+mKYwF+xPnGqnkoA9evTqsmKpc9+dnvjw=="
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgU2+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBfbp/yPHi8nqF5JlHY3gMf4+TUukk841j5dpZAlBnErrAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKCtqd+zZYsRGmdaArT3U98g6jMIULFlWFPsOe/tnrpnLkF8yP4=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhAz6JiQVdTTCN42Yk/Xk+L2jAUtb4dCCQUHdTOREDybjc5ajqMYE8TjNP83Nq50WqPpjt2Ety1W3NMUtg8WQpQDbkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FNvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgranfs2WLERpnWgK091PfIOozCFCxZVhT7Dnv7Z66Zy4xq577"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgU2+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBfbp/yPHi8nqF5JlHY3gMf4+TUukk841j5dpZAlBnErrAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKCtqd+zZYsRGmdaArT3U98g6jMIULFlWFPsOe/tnrpnLkF8yP4=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhAfYZ5wxDtV6NQIpIBsmHUJQmpsSKc7X/JTRGkskuoOTHJer+tTPfxAeFmG2pVdpZErTdToA/RL5rL2mhjKjgTC7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FNvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgranfs2WLERpnWgK091PfIOozCFCxZVhT7Dnv7Z66Zy50+xFq"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 54
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAfYZ5wxDtV6NQIpIBsmHUJQmpsSKc7X/JTRGkskuoOTHJer+tTPfxAeFmG2pVdpZErTdToA/RL5rL2mhjKjgTC7hAz6JiQVdTTCN42Yk/Xk+L2jAUtb4dCCQUHdTOREDybjc5ajqMYE8TjNP83Nq50WqPpjt2Ety1W3NMUtg8WQpQDbkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FNvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgranfs2WLERpnWgK091PfIOozCFCxZVhT7Dnv7Z66Zy7TpOiM"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 54,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 718,
    "height": 54,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAqAOOdZ"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAfYZ5wxDtV6NQIpIBsmHUJQmpsSKc7X/JTRGkskuoOTHJer+tTPfxAeFmG2pVdpZErTdToA/RL5rL2mhjKjgTC7hAz6JiQVdTTCN42Yk/Xk+L2jAUtb4dCCQUHdTOREDybjc5ajqMYE8TjNP83Nq50WqPpjt2Ety1W3NMUtg8WQpQDbkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FNvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgranfs2WLERpnWgK091PfIOozCFCxZVhT7Dnv7Z66Zy7TpOiM"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 54
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 54,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 718,
    "height": 54,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAqAOOdZ"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FN/jWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EwKDKBSmN/yp48jR1cSGGPJpQk0qciwTlwbI4AH0zkOTnJ/eBweo=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhAA4RJkIdLYLKLjAwp68S5YvaW0il5hyKxMm4x2+kqK9qyShfjrt/lSc6rGOBVdhLOzVc2RLagGAhnMMi14RKkCrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBTf41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgygUpjf8qePI0dXEhhjyaUJNKnIsE5cGyOAB9M5Dk5ydHx8GZ"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FN/jWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EwKDKBSmN/yp48jR1cSGGPJpQk0qciwTlwbI4AH0zkOTnJ/eBweo=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhAyw9rIjApeeqoNIUzQVqNcl1lh2zvIO4PkX0KuyeC/GfSG1m9+hEDQ6vwOAchMbjQvaxtG1ZFcvK/+AChYg4SCbkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBTf41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgygUpjf8qePI0dXEhhjyaUJNKnIsE5cGyOAB9M5Dk5yexEUxS"
  }
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 55
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAA4RJkIdLYLKLjAwp68S5YvaW0il5hyKxMm4x2+kqK9qyShfjrt/lSc6rGOBVdhLOzVc2RLagGAhnMMi14RKkCrhAyw9rIjApeeqoNIUzQVqNcl1lh2zvIO4PkX0KuyeC/GfSG1m9+hEDQ6vwOAchMbjQvaxtG1ZFcvK/+AChYg4SCbkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBTf41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgygUpjf8qePI0dXEhhjyaUJNKnIsE5cGyOAB9M5Dk5yczMu18"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 55,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 600,
    "height": 55,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkYTnKf+gTmzlA"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 55
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAA4RJkIdLYLKLjAwp68S5YvaW0il5hyKxMm4x2+kqK9qyShfjrt/lSc6rGOBVdhLOzVc2RLagGAhnMMi14RKkCrhAyw9rIjApeeqoNIUzQVqNcl1lh2zvIO4PkX0KuyeC/GfSG1m9+hEDQ6vwOAchMbjQvaxtG1ZFcvK/+AChYg4SCbkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBTf41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgygUpjf8qePI0dXEhhjyaUJNKnIsE5cGyOAB9M5Dk5yczMu18"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 55,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 600,
    "height": 55,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkYTnKf+gTmzlA"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FOPjWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmwKB3syTDJcbyxKB4TNUzLuva/JeUMMXnO02jtmjBAaJy0a66sbg=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhA8CWEHrgpDlT3nowb7Zfi4cm0buxRsr2I+oKmf44D7iuBKcNfXPiSvNul5sNMOxQnkgqp2emPQlU2VQUVV6KNA7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBTj41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgd7MkwyXG8sSgeEzVMy7r2vyXlDDF5ztNo7ZowQGictHPWn3a"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FOPjWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmwKB3syTDJcbyxKB4TNUzLuva/JeUMMXnO02jtmjBAaJy0a66sbg=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhAqEc5aT8NaX4EMjIdWtMHFqjFf0Y1XeX5O2jH5nbNNKr3HVoreRymPwayPqwIKqeJfstIKutDw/uQ0U0tLB19D7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBTj41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgd7MkwyXG8sSgeEzVMy7r2vyXlDDF5ztNo7ZowQGictE/ZzOz"
  }
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 56
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAqEc5aT8NaX4EMjIdWtMHFqjFf0Y1XeX5O2jH5nbNNKr3HVoreRymPwayPqwIKqeJfstIKutDw/uQ0U0tLB19D7hA8CWEHrgpDlT3nowb7Zfi4cm0buxRsr2I+oKmf44D7iuBKcNfXPiSvNul5sNMOxQnkgqp2emPQlU2VQUVV6KNA7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBTj41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgd7MkwyXG8sSgeEzVMy7r2vyXlDDF5ztNo7ZowQGictE9xhPD"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 56,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 600,
    "height": 56,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/qiUiX+ZkmnBe"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 56
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAqEc5aT8NaX4EMjIdWtMHFqjFf0Y1XeX5O2jH5nbNNKr3HVoreRymPwayPqwIKqeJfstIKutDw/uQ0U0tLB19D7hA8CWEHrgpDlT3nowb7Zfi4cm0buxRsr2I+oKmf44D7iuBKcNfXPiSvNul5sNMOxQnkgqp2emPQlU2VQUVV6KNA7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBTj41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgd7MkwyXG8sSgeEzVMy7r2vyXlDDF5ztNo7ZowQGictE9xhPD"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 56,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 600,
    "height": 56,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/qiUiX+ZkmnBe"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1K4BjA=",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1K4BjA=",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1K4BjA=",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1K4BjA=",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1K4BjA=",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QE+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FOfj2uPT48oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgjAt2+/jT3WJAx/X8mmqIq5idH48B7FqmRC/tWic4jqcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPAoGLe+8hVqHZ5KN3l9k7Q0zUEeWqT2dCkUTd988Q9rz14WphxIw==",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1K4BjA=",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QGKCwH4QrhA2FZqAqBVrBc07wLqKul2+OSY6mreSRTenj55FVPFQ7M/H9gKPe42zmk6Xuh+VS8eyovV6UkM/yL/xod73/FfBrkBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBTn49rj0+PKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwKBi3vvIVah2eSjd5fZO0NM1BHlqk9nQpFE3ffPEPa89eHb5SAM="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QE+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FOfj2uPT48oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgjAt2+/jT3WJAx/X8mmqIq5idH48B7FqmRC/tWic4jqcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPAoGLe+8hVqHZ5KN3l9k7Q0zUEeWqT2dCkUTd988Q9rz14WphxIw==",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1K4BjA=",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QGKCwH4QrhAQ+q6T4Sx1b4RdUsVIcwubmJpQC973loXTefh3HFdDP6QpgbrxSKrP2S7+2KrObLnHemep6dqedz54BVsQc6MC7kBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBTn49rj0+PKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwKBi3vvIVah2eSjd5fZO0NM1BHlqk9nQpFE3ffPEPa89eP94LRw="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QHMCwH4hLhAQ+q6T4Sx1b4RdUsVIcwubmJpQC973loXTefh3HFdDP6QpgbrxSKrP2S7+2KrObLnHemep6dqedz54BVsQc6MC7hA2FZqAqBVrBc07wLqKul2+OSY6mreSRTenj55FVPFQ7M/H9gKPe42zmk6Xuh+VS8eyovV6UkM/yL/xod73/FfBrkBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBTn49rj0+PKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwKBi3vvIVah2eSjd5fZO0NM1BHlqk9nQpFE3ffPEPa89eOzjRuw="
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
    "state": "tx_+QHMCwH4hLhAQ+q6T4Sx1b4RdUsVIcwubmJpQC973loXTefh3HFdDP6QpgbrxSKrP2S7+2KrObLnHemep6dqedz54BVsQc6MC7hA2FZqAqBVrBc07wLqKul2+OSY6mreSRTenj55FVPFQ7M/H9gKPe42zmk6Xuh+VS8eyovV6UkM/yL/xod73/FfBrkBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBTn49rj0+PKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwKBi3vvIVah2eSjd5fZO0NM1BHlqk9nQpFE3ffPEPa89eOzjRuw="
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgU6+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBfbp/yPHi8nqF5JlHY3gMf4+TUukk841j5dpZAlBnErrAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKBP9vskS09JEjT/LXv/9Aall5Q2Pkw89YcHsosWMr9lI4BcFuQ=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhAqJFe7ui5MdT9MSvyEgcn252WNVKdJyqVqS8ImOcqsgES83O0PC/qn7iTrZS0qEtfyCrr1EN6wIyZJpLVlhFSALkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FOvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgT/b7JEtPSRI0/y17//QGpZeUNj5MPPWHB7KLFjK/ZSNz7dFE"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgU6+La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBfbp/yPHi8nqF5JlHY3gMf4+TUukk841j5dpZAlBnErrAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKBP9vskS09JEjT/LXv/9Aall5Q2Pkw89YcHsosWMr9lI4BcFuQ=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhA3LkVS6EhcMF8MGrfU8Js/PjTvtLFBxbmXhz3xdcIEE8/gJ42dTXUvAKaJvsq1JECcRHjYVonzdBFnIJ5yTO8DLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FOvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgT/b7JEtPSRI0/y17//QGpZeUNj5MPPWHB7KLFjK/ZSMPSZN2"
  }
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 58
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAqJFe7ui5MdT9MSvyEgcn252WNVKdJyqVqS8ImOcqsgES83O0PC/qn7iTrZS0qEtfyCrr1EN6wIyZJpLVlhFSALhA3LkVS6EhcMF8MGrfU8Js/PjTvtLFBxbmXhz3xdcIEE8/gJ42dTXUvAKaJvsq1JECcRHjYVonzdBFnIJ5yTO8DLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FOvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgT/b7JEtPSRI0/y17//QGpZeUNj5MPPWHB7KLFjK/ZSM4JI3g"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 58,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 718,
    "height": 58,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAfn8n3G"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
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
    "state": "tx_+QGLCwH4hLhAqJFe7ui5MdT9MSvyEgcn252WNVKdJyqVqS8ImOcqsgES83O0PC/qn7iTrZS0qEtfyCrr1EN6wIyZJpLVlhFSALhA3LkVS6EhcMF8MGrfU8Js/PjTvtLFBxbmXhz3xdcIEE8/gJ42dTXUvAKaJvsq1JECcRHjYVonzdBFnIJ5yTO8DLkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FOvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgT/b7JEtPSRI0/y17//QGpZeUNj5MPPWHB7KLFjK/ZSM4JI3g"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 58
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 58,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 718,
    "height": 58,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAfn8n3G"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FO/jWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EwKBQHZYiCm0xv1KnpRtvwZu1R1srOAmlY8YTkksFJkmw7tqmvBM=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhAVHKMwflbtxWJyCzmXpLVcvKu1D9XM9nxDyWbJSjZVrwbPJtSuX8BpYj3k+rE6yAjLExtZcdcqoAimVHElassB7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBTv41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgUB2WIgptMb9Sp6Ubb8GbtUdbKzgJpWPGE5JLBSZJsO6n+CjE"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FO/jWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EwKBQHZYiCm0xv1KnpRtvwZu1R1srOAmlY8YTkksFJkmw7tqmvBM=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhASB7Qh/1xmUwu1S2uGAO1Es+3a8bh4HURzaXRvpDlitQpbzfc3CR3Ai1Pue/RPyzTHEfygqTbj0UyB6sePl0QBLkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBTv41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgUB2WIgptMb9Sp6Ubb8GbtUdbKzgJpWPGE5JLBSZJsO5h0zVe"
  }
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 59
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhASB7Qh/1xmUwu1S2uGAO1Es+3a8bh4HURzaXRvpDlitQpbzfc3CR3Ai1Pue/RPyzTHEfygqTbj0UyB6sePl0QBLhAVHKMwflbtxWJyCzmXpLVcvKu1D9XM9nxDyWbJSjZVrwbPJtSuX8BpYj3k+rE6yAjLExtZcdcqoAimVHElassB7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBTv41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgUB2WIgptMb9Sp6Ubb8GbtUdbKzgJpWPGE5JLBSZJsO6WL3IT"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 59,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 600,
    "height": 59,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkYTnKf+u+B7q9"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhASB7Qh/1xmUwu1S2uGAO1Es+3a8bh4HURzaXRvpDlitQpbzfc3CR3Ai1Pue/RPyzTHEfygqTbj0UyB6sePl0QBLhAVHKMwflbtxWJyCzmXpLVcvKu1D9XM9nxDyWbJSjZVrwbPJtSuX8BpYj3k+rE6yAjLExtZcdcqoAimVHElassB7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBTv41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgUB2WIgptMb9Sp6Ubb8GbtUdbKzgJpWPGE5JLBSZJsO6WL3IT"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 59
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 59,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 600,
    "height": 59,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkYTnKf+u+B7q9"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FPPjWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmwKDfpEQZVMI20MEeXygxC2cFe0ckKmFcDNhi73qfpCsQw1q3nas=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhAVVvt2j+Pg9bdEPNzY0cVNkPcUivot7IZoGG20zXMOK3zN04XiMh7uItTASNKS/cwEMDUJYSmLYoZnDOopndsC7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBTz41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCg36REGVTCNtDBHl8oMQtnBXtHJCphXAzYYu96n6QrEMPVIga7"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FPPjWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmwKDfpEQZVMI20MEeXygxC2cFe0ckKmFcDNhi73qfpCsQw1q3nas=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhA9lzLN3LlWuCUxzQbxINTczmeN6WZZ3fiV8NSqSfLYCOgfuoHHwYKGRewYC7+J0V9MxZyGZUJnGJScvhOsuLwBrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBTz41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCg36REGVTCNtDBHl8oMQtnBXtHJCphXAzYYu96n6QrEMNonJn3"
  }
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 60
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAVVvt2j+Pg9bdEPNzY0cVNkPcUivot7IZoGG20zXMOK3zN04XiMh7uItTASNKS/cwEMDUJYSmLYoZnDOopndsC7hA9lzLN3LlWuCUxzQbxINTczmeN6WZZ3fiV8NSqSfLYCOgfuoHHwYKGRewYC7+J0V9MxZyGZUJnGJScvhOsuLwBrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBTz41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCg36REGVTCNtDBHl8oMQtnBXtHJCphXAzYYu96n6QrEMOPbEXW"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 60,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 600,
    "height": 60,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/qiUiX+ZkmnBe"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAVVvt2j+Pg9bdEPNzY0cVNkPcUivot7IZoGG20zXMOK3zN04XiMh7uItTASNKS/cwEMDUJYSmLYoZnDOopndsC7hA9lzLN3LlWuCUxzQbxINTczmeN6WZZ3fiV8NSqSfLYCOgfuoHHwYKGRewYC7+J0V9MxZyGZUJnGJScvhOsuLwBrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBTz41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCg36REGVTCNtDBHl8oMQtnBXtHJCphXAzYYu96n6QrEMOPbEXW"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 60
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 60,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 600,
    "height": 60,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/qiUiX+ZkmnBe"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAmoF82g=",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAmoF82g=",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAmoF82g=",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAmoF82g=",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAmoF82g=",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QE+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FPfj2uPT48oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgjAt2+/jT3WJAx/X8mmqIq5idH48B7FqmRC/tWic4jqcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALAoOPFg9f+AAU8YukxnSLijvKyHl0HZms0NwO7XLgubUokbIMsRw==",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAmoF82g=",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QGKCwH4QrhAZum15gAYxk6wh/CVDktBcyFpt+iiQLUQ8nPeAr+e+HB/WieHieTu3ebRFwtsRj4F3n8BMAmzY2bCvaVr3gCQBLkBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBT349rj0+PKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwKDjxYPX/gAFPGLpMZ0i4o7ysh5dB2ZrNDcDu1y4Lm1KJEk2mLY="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QE+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FPfj2uPT48oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgjAt2+/jT3WJAx/X8mmqIq5idH48B7FqmRC/tWic4jqcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALAoOPFg9f+AAU8YukxnSLijvKyHl0HZms0NwO7XLgubUokbIMsRw==",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAmoF82g=",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QGKCwH4QrhALOjcDKUSVXMJ95JaVu8JtvwE2E8YtMRieLw2jFaE2uFO19Ho8j+6f4eHdKGHF+5lp+fJ+NZmeTBSeEqTdDwUCLkBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBT349rj0+PKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwKDjxYPX/gAFPGLpMZ0i4o7ysh5dB2ZrNDcDu1y4Lm1KJEOZfCs="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QHMCwH4hLhALOjcDKUSVXMJ95JaVu8JtvwE2E8YtMRieLw2jFaE2uFO19Ho8j+6f4eHdKGHF+5lp+fJ+NZmeTBSeEqTdDwUCLhAZum15gAYxk6wh/CVDktBcyFpt+iiQLUQ8nPeAr+e+HB/WieHieTu3ebRFwtsRj4F3n8BMAmzY2bCvaVr3gCQBLkBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBT349rj0+PKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwKDjxYPX/gAFPGLpMZ0i4o7ysh5dB2ZrNDcDu1y4Lm1KJDEYKQ4="
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
    "state": "tx_+QHMCwH4hLhALOjcDKUSVXMJ95JaVu8JtvwE2E8YtMRieLw2jFaE2uFO19Ho8j+6f4eHdKGHF+5lp+fJ+NZmeTBSeEqTdDwUCLhAZum15gAYxk6wh/CVDktBcyFpt+iiQLUQ8nPeAr+e+HB/WieHieTu3ebRFwtsRj4F3n8BMAmzY2bCvaVr3gCQBLkBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBT349rj0+PKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwKDjxYPX/gAFPGLpMZ0i4o7ysh5dB2ZrNDcDu1y4Lm1KJDEYKQ4="
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgU++La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBfbp/yPHi8nqF5JlHY3gMf4+TUukk841j5dpZAlBnErrAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKByleP3xmVpb7P9Hp8K6kJDKZ6UYtizmd7ADX2tcWKNvPfpWOo=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhAAhuDDGSKGGOfllX5l/wxHbkpxqWMrL6kc/qFE9R//UMugywHoBBljSsrKluFX6y06kvqz1WJ3WcGocLRJ4UJCrkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FPvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgcpXj98ZlaW+z/R6fCupCQymelGLYs5newA19rXFijbyvlADl"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgU++La4tPiyggI+AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShBfbp/yPHi8nqF5JlHY3gMf4+TUukk841j5dpZAlBnErrAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKByleP3xmVpb7P9Hp8K6kJDKZ6UYtizmd7ADX2tcWKNvPfpWOo=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhAhljyVmrqsy8HIUM4wXg7dic1pXwRtiJGuaBE+DFBJB15yyB5u7/pZyDTxoZT2C35j4pVhbW+fu5xIJ0bwEo+D7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FPvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgcpXj98ZlaW+z/R6fCupCQymelGLYs5newA19rXFijbyttO/H"
  }
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 62
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAAhuDDGSKGGOfllX5l/wxHbkpxqWMrL6kc/qFE9R//UMugywHoBBljSsrKluFX6y06kvqz1WJ3WcGocLRJ4UJCrhAhljyVmrqsy8HIUM4wXg7dic1pXwRtiJGuaBE+DFBJB15yyB5u7/pZyDTxoZT2C35j4pVhbW+fu5xIJ0bwEo+D7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FPvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgcpXj98ZlaW+z/R6fCupCQymelGLYs5newA19rXFijbwFuDBt"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 62,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 718,
    "height": 62,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUTF3JV"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAAhuDDGSKGGOfllX5l/wxHbkpxqWMrL6kc/qFE9R//UMugywHoBBljSsrKluFX6y06kvqz1WJ3WcGocLRJ4UJCrhAhljyVmrqsy8HIUM4wXg7dic1pXwRtiJGuaBE+DFBJB15yyB5u7/pZyDTxoZT2C35j4pVhbW+fu5xIJ0bwEo+D7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FPvi2uLT4soICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgcpXj98ZlaW+z/R6fCupCQymelGLYs5newA19rXFijbwFuDBt"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 62
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 62,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 718,
    "height": 62,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUTF3JV"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FP/jWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EwKBNWJ99A7OxJVsb8DrovSBKeBdUtZfp/ybp71a57dtAwW+Kkq8=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhAYBxp72jpHU4W/daYImZZa/7kaC6M4dE4ZZo8JWM+Pxa5OgnqVzu3dwFVI+GPtxY++9RbxtewOlEgfdaJeJcUBLkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBT/41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgTViffQOzsSVbG/A66L0gSngXVLWX6f8m6e9Wue3bQMFNwNZY"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FP/jWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EwKBNWJ99A7OxJVsb8DrovSBKeBdUtZfp/ybp71a57dtAwW+Kkq8=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhAatWh7zV/rxi5xdZRxYbi1xH2RLDPsu2uPdSAQxOSF9gEWVq6fJxytHLoSdNxMw1QglZXfIDQAfjXlaHiVyPDCrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBT/41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgTViffQOzsSVbG/A66L0gSngXVLWX6f8m6e9Wue3bQMFGx5gP"
  }
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 63
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAYBxp72jpHU4W/daYImZZa/7kaC6M4dE4ZZo8JWM+Pxa5OgnqVzu3dwFVI+GPtxY++9RbxtewOlEgfdaJeJcUBLhAatWh7zV/rxi5xdZRxYbi1xH2RLDPsu2uPdSAQxOSF9gEWVq6fJxytHLoSdNxMw1QglZXfIDQAfjXlaHiVyPDCrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBT/41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgTViffQOzsSVbG/A66L0gSngXVLWX6f8m6e9Wue3bQMEh+SeM"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 63,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 600,
    "height": 63,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkYTnKf+u+B7q9"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAYBxp72jpHU4W/daYImZZa/7kaC6M4dE4ZZo8JWM+Pxa5OgnqVzu3dwFVI+GPtxY++9RbxtewOlEgfdaJeJcUBLhAatWh7zV/rxi5xdZRxYbi1xH2RLDPsu2uPdSAQxOSF9gEWVq6fJxytHLoSdNxMw1QglZXfIDQAfjXlaHiVyPDCrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBT/41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgTViffQOzsSVbG/A66L0gSngXVLWX6f8m6e9Wue3bQMEh+SeM"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 63
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 63,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 600,
    "height": 63,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkYTnKf+u+B7q9"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FQPjWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmwKBK215vhYOJf5ljAvFwFvcLztuKnAn+8H9kGHPnEeVpK9YF75k=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhAcRl7od5Ou4NTLZZSdA/qqFdKclQVBTc3Ff+tXecuIOhmq6GtBAGMGbFdN6gPTi0gx5tx5K0xw5Ge+pSib3NBCLkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUD41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgStteb4WDiX+ZYwLxcBb3C87bipwJ/vB/ZBhz5xHlaSuJ35Tm"
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FQPjWuNT40oICPgGhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmwKBK215vhYOJf5ljAvFwFvcLztuKnAn+8H9kGHPnEeVpK9YF75k=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "call_stack": [],
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhA9wPWOuQbP9+MzoYXlT7/uOrZ0iB7BescFobkck9oGrwANN6VwpPsr40lulaRSmcgvWerJ5QzD+ETbLAVb7YqALkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUD41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgStteb4WDiX+ZYwLxcBb3C87bipwJ/vB/ZBhz5xHlaStNFuTQ"
  }
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 64
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAcRl7od5Ou4NTLZZSdA/qqFdKclQVBTc3Ff+tXecuIOhmq6GtBAGMGbFdN6gPTi0gx5tx5K0xw5Ge+pSib3NBCLhA9wPWOuQbP9+MzoYXlT7/uOrZ0iB7BescFobkck9oGrwANN6VwpPsr40lulaRSmcgvWerJ5QzD+ETbLAVb7YqALkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUD41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgStteb4WDiX+ZYwLxcBb3C87bipwJ/vB/ZBhz5xHlaSt1mmFE"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 64,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 600,
    "height": 64,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/qiUiX+gwgMWl"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAcRl7od5Ou4NTLZZSdA/qqFdKclQVBTc3Ff+tXecuIOhmq6GtBAGMGbFdN6gPTi0gx5tx5K0xw5Ge+pSib3NBCLhA9wPWOuQbP9+MzoYXlT7/uOrZ0iB7BescFobkck9oGrwANN6VwpPsr40lulaRSmcgvWerJ5QzD+ETbLAVb7YqALkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUD41rjU+NKCAj4BoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgStteb4WDiX+ZYwLxcBb3C87bipwJ/vB/ZBhz5xHlaSt1mmFE"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 64
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 64,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 600,
    "height": 64,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/qiUiX+gwgMWl"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 61
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 61,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 22521,
    "height": 61,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUTF3JV"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 61
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "caller_nonce": 61,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 22521,
    "height": 61,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUTF3JV"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "clean_contract_calls"
}
```

#### responder <--- node
```javascript
{
  "action": "calls_pruned",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 61
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "call_not_found",
    "request": {
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": 61
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgVB+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBfbp/yPHi8nqF5JlHY3gMf4+TUukk841j5dpZAlBnErrAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKCOc/eklhtNewGzYfSqKXRPB75i0CoQGBHsQvDqUeuiwinck/M=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhA+AcrrsDq/DQ6fWLiAzOTQdwU4ap4lX1dAYDKXQHVtSm73bLYNWwecgMQY1+d9f1kR5oiwjuAVb19rHFe/zrvA7kBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FQfi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgjnP3pJYbTXsBs2H0qil0Twe+YtAqEBgR7ELw6lHrosJH4hFC"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgVB+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBfbp/yPHi8nqF5JlHY3gMf4+TUukk841j5dpZAlBnErrAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKCOc/eklhtNewGzYfSqKXRPB75i0CoQGBHsQvDqUeuiwinck/M=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhA/O/KkZDT7OOgs9HRQUEGXjksZR899CnwDv5+r+QmzMf9S0oOBFai8W7RCUEUHO2KW5PZjf/m9Trxka+ENTX/BrkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FQfi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgjnP3pJYbTXsBs2H0qil0Twe+YtAqEBgR7ELw6lHrosJ9RdbW"
  }
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 65
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhA+AcrrsDq/DQ6fWLiAzOTQdwU4ap4lX1dAYDKXQHVtSm73bLYNWwecgMQY1+d9f1kR5oiwjuAVb19rHFe/zrvA7hA/O/KkZDT7OOgs9HRQUEGXjksZR899CnwDv5+r+QmzMf9S0oOBFai8W7RCUEUHO2KW5PZjf/m9Trxka+ENTX/BrkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FQfi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgjnP3pJYbTXsBs2H0qil0Twe+YtAqEBgR7ELw6lHrosIVsZQ6"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 65,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 718,
    "height": 65,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUTF3JV"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhA+AcrrsDq/DQ6fWLiAzOTQdwU4ap4lX1dAYDKXQHVtSm73bLYNWwecgMQY1+d9f1kR5oiwjuAVb19rHFe/zrvA7hA/O/KkZDT7OOgs9HRQUEGXjksZR899CnwDv5+r+QmzMf9S0oOBFai8W7RCUEUHO2KW5PZjf/m9Trxka+ENTX/BrkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FQfi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgjnP3pJYbTXsBs2H0qil0Twe+YtAqEBgR7ELw6lHrosIVsZQ6"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 65
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 65,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 718,
    "height": 65,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUTF3JV"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FQvjWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmwKDAgdK/N2qEgMDlHpAMeToFq9RN0a6o+R4dDX+QZaMt1B4N3RE=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhA+qshON7TvlT5qV+FiHQkdhtglapkr7Iej7rHnILxm7qy+hIfqoa165IuCaIx5ZDWU7NnL5ydLWE+7wypJwqUDbkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUL41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgwIHSvzdqhIDA5R6QDHk6BavUTdGuqPkeHQ1/kGWjLdQYHkQ9"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FQvjWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmwKDAgdK/N2qEgMDlHpAMeToFq9RN0a6o+R4dDX+QZaMt1B4N3RE=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhAW8Fe9Ajn6+MCHyJvy4OclOsyAictitrmxqHHf7veCvlcUwPeHkDGPd4B8BxbwzrDgJ6c3Bg2+OSqMptNqioMArkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUL41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgwIHSvzdqhIDA5R6QDHk6BavUTdGuqPkeHQ1/kGWjLdTceOhD"
  }
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 66
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAW8Fe9Ajn6+MCHyJvy4OclOsyAictitrmxqHHf7veCvlcUwPeHkDGPd4B8BxbwzrDgJ6c3Bg2+OSqMptNqioMArhA+qshON7TvlT5qV+FiHQkdhtglapkr7Iej7rHnILxm7qy+hIfqoa165IuCaIx5ZDWU7NnL5ydLWE+7wypJwqUDbkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUL41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgwIHSvzdqhIDA5R6QDHk6BavUTdGuqPkeHQ1/kGWjLdQ0ssev"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 66,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 600,
    "height": 66,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/qiUiX+gwgMWl"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAW8Fe9Ajn6+MCHyJvy4OclOsyAictitrmxqHHf7veCvlcUwPeHkDGPd4B8BxbwzrDgJ6c3Bg2+OSqMptNqioMArhA+qshON7TvlT5qV+FiHQkdhtglapkr7Iej7rHnILxm7qy+hIfqoa165IuCaIx5ZDWU7NnL5ydLWE+7wypJwqUDbkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUL41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgwIHSvzdqhIDA5R6QDHk6BavUTdGuqPkeHQ1/kGWjLdQ0ssev"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 66
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 66,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 600,
    "height": 66,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/qiUiX+gwgMWl"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FQ/jWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EwKCu+ex70VQdQ/zp6knsoD5VWGFxW+1WxxSqjLVbSvuYzW0VloQ=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhAAcX0zX/BWi8nqXZLFKF5+ioezWgaf6ec9N0jWCBwRMAI0dDEcrf4WZ1GcpSJQ0rxRncPnAMCWVifWq1bjXtxBrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUP41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgrvnse9FUHUP86epJ7KA+VVhhcVvtVscUqoy1W0r7mM299q+Z"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FQ/jWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EwKCu+ex70VQdQ/zp6knsoD5VWGFxW+1WxxSqjLVbSvuYzW0VloQ=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 67
  },
  "tag": "contract_call"
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhArLkL6BGYIdSgnEoDJCt27RE4HfQVtTNzKXWuUlQs6iJ+wEu1zJk/o5cQBGfopJQj5ifTagqcg7yipJAJcaGxArkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUP41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgrvnse9FUHUP86epJ7KA+VVhhcVvtVscUqoy1W0r7mM1BgLuy"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAAcX0zX/BWi8nqXZLFKF5+ioezWgaf6ec9N0jWCBwRMAI0dDEcrf4WZ1GcpSJQ0rxRncPnAMCWVifWq1bjXtxBrhArLkL6BGYIdSgnEoDJCt27RE4HfQVtTNzKXWuUlQs6iJ+wEu1zJk/o5cQBGfopJQj5ifTagqcg7yipJAJcaGxArkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUP41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgrvnse9FUHUP86epJ7KA+VVhhcVvtVscUqoy1W0r7mM17q+yN"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 67,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 600,
    "height": 67,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkYTnKf+u+B7q9"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAAcX0zX/BWi8nqXZLFKF5+ioezWgaf6ec9N0jWCBwRMAI0dDEcrf4WZ1GcpSJQ0rxRncPnAMCWVifWq1bjXtxBrhArLkL6BGYIdSgnEoDJCt27RE4HfQVtTNzKXWuUlQs6iJ+wEu1zJk/o5cQBGfopJQj5ifTagqcg7yipJAJcaGxArkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUP41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgrvnse9FUHUP86epJ7KA+VVhhcVvtVscUqoy1W0r7mM17q+yN"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 67
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 67,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 600,
    "height": 67,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkYTnKf+u+B7q9"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5ceuTo=",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5ceuTo=",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5ceuTo=",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5ceuTo=",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5ceuTo=",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QE+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FRPj2uPT48oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgjAt2+/jT3WJAx/X8mmqIq5idH48B7FqmRC/tWic4jqcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPAoIELPS9hvo2cOzmoG7+nwJJYs45TKS0drNWxEwUOT9CMXX7ZOw==",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5ceuTo=",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QGKCwH4QrhACaiZybMPEIQnWZ8Fv61NGRvfqfVddRjaUTuZxPXiYevBMjPI5Zow+BKX6ZL66LAiP1UEAe7BSXsUolYSfT/tB7kBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUT49rj0+PKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwKCBCz0vYb6NnDs5qBu/p8CSWLOOUyktHazVsRMFDk/QjLpfd/U="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QE+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FRPj2uPT48oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgjAt2+/jT3WJAx/X8mmqIq5idH48B7FqmRC/tWic4jqcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPAoIELPS9hvo2cOzmoG7+nwJJYs45TKS0drNWxEwUOT9CMXX7ZOw==",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5ceuTo=",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QGKCwH4QrhAPMsbSD2M5Z/rok0FhvJn1SKKBEGoRHB4WnL8V/yq+4OZWQxvPLek6fRe/jTTHkCny6AQHIYHt+1gjK0RhdwcCbkBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUT49rj0+PKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwKCBCz0vYb6NnDs5qBu/p8CSWLOOUyktHazVsRMFDk/QjHraCuY="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QHMCwH4hLhACaiZybMPEIQnWZ8Fv61NGRvfqfVddRjaUTuZxPXiYevBMjPI5Zow+BKX6ZL66LAiP1UEAe7BSXsUolYSfT/tB7hAPMsbSD2M5Z/rok0FhvJn1SKKBEGoRHB4WnL8V/yq+4OZWQxvPLek6fRe/jTTHkCny6AQHIYHt+1gjK0RhdwcCbkBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUT49rj0+PKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwKCBCz0vYb6NnDs5qBu/p8CSWLOOUyktHazVsRMFDk/QjJc1yZA="
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
    "state": "tx_+QHMCwH4hLhACaiZybMPEIQnWZ8Fv61NGRvfqfVddRjaUTuZxPXiYevBMjPI5Zow+BKX6ZL66LAiP1UEAe7BSXsUolYSfT/tB7hAPMsbSD2M5Z/rok0FhvJn1SKKBEGoRHB4WnL8V/yq+4OZWQxvPLek6fRe/jTTHkCny6AQHIYHt+1gjK0RhdwcCbkBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUT49rj0+PKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADwKCBCz0vYb6NnDs5qBu/p8CSWLOOUyktHazVsRMFDk/QjJc1yZA="
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgVF+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBfbp/yPHi8nqF5JlHY3gMf4+TUukk841j5dpZAlBnErrAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKD+z8s5PdRTXCUQZpaETo774YXN9VuIR3x8EZ6KqKX8j0XOb90=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhAWQPPTd+hqZuOTiKjo/D/dQC6m8nhBYhHN4AvLtxEpwvs7cmesPI0mNix1jc2eP68iI+PBAw4gbyO0NkTE08fBbkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FRfi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg/s/LOT3UU1wlEGaWhE6O++GFzfVbiEd8fBGeiqil/I9wC3i1"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgVF+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBfbp/yPHi8nqF5JlHY3gMf4+TUukk841j5dpZAlBnErrAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKD+z8s5PdRTXCUQZpaETo774YXN9VuIR3x8EZ6KqKX8j0XOb90=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhALPFokEj60yx4tJWAzO2/7b7Ga+U+0Udvnx65U8srpTvddJz2vmANyWTo0tY3mUk4hDkYG+8XGMlA8Q/qQ7jjBrkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FRfi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg/s/LOT3UU1wlEGaWhE6O++GFzfVbiEd8fBGeiqil/I8dyrtQ"
  }
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 69
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhALPFokEj60yx4tJWAzO2/7b7Ga+U+0Udvnx65U8srpTvddJz2vmANyWTo0tY3mUk4hDkYG+8XGMlA8Q/qQ7jjBrhAWQPPTd+hqZuOTiKjo/D/dQC6m8nhBYhHN4AvLtxEpwvs7cmesPI0mNix1jc2eP68iI+PBAw4gbyO0NkTE08fBbkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FRfi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg/s/LOT3UU1wlEGaWhE6O++GFzfVbiEd8fBGeiqil/I+zpEgI"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 69,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 718,
    "height": 69,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKTmJT3"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhALPFokEj60yx4tJWAzO2/7b7Ga+U+0Udvnx65U8srpTvddJz2vmANyWTo0tY3mUk4hDkYG+8XGMlA8Q/qQ7jjBrhAWQPPTd+hqZuOTiKjo/D/dQC6m8nhBYhHN4AvLtxEpwvs7cmesPI0mNix1jc2eP68iI+PBAw4gbyO0NkTE08fBbkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FRfi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg/s/LOT3UU1wlEGaWhE6O++GFzfVbiEd8fBGeiqil/I+zpEgI"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 69
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 69,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 718,
    "height": 69,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKTmJT3"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FRvjWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmwKAw0Qw5Hg+Y8Y83l2Qs1yKSiMdTCjLAgg+U+YpusWhe2y81rlg=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhAQJ2i2agPfLWzmn+6UG2V7GoElibyn0phLyzaKSxQdKqETI78dt0lQCfZ69joU6QUPBe4GAIb0XL/iyJqjUFYArkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUb41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgMNEMOR4PmPGPN5dkLNcikojHUwoywIIPlPmKbrFoXts2VslS"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FRvjWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmwKAw0Qw5Hg+Y8Y83l2Qs1yKSiMdTCjLAgg+U+YpusWhe2y81rlg=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhA/L2pzlkjasJxOCX/RhroqwajO08mvBpHNtdVS1P4a9AoFpGFNiLwK8ISuKA1/cMM0h6rHeDP0PzidwHOqJZlBLkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUb41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgMNEMOR4PmPGPN5dkLNcikojHUwoywIIPlPmKbrFoXttL5IIt"
  }
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 70
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAQJ2i2agPfLWzmn+6UG2V7GoElibyn0phLyzaKSxQdKqETI78dt0lQCfZ69joU6QUPBe4GAIb0XL/iyJqjUFYArhA/L2pzlkjasJxOCX/RhroqwajO08mvBpHNtdVS1P4a9AoFpGFNiLwK8ISuKA1/cMM0h6rHeDP0PzidwHOqJZlBLkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUb41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgMNEMOR4PmPGPN5dkLNcikojHUwoywIIPlPmKbrFoXtslQbtA"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 70,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 600,
    "height": 70,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/qiUiX+sti1Wp"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAQJ2i2agPfLWzmn+6UG2V7GoElibyn0phLyzaKSxQdKqETI78dt0lQCfZ69joU6QUPBe4GAIb0XL/iyJqjUFYArhA/L2pzlkjasJxOCX/RhroqwajO08mvBpHNtdVS1P4a9AoFpGFNiLwK8ISuKA1/cMM0h6rHeDP0PzidwHOqJZlBLkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUb41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgMNEMOR4PmPGPN5dkLNcikojHUwoywIIPlPmKbrFoXtslQbtA"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 70
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 70,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 600,
    "height": 70,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/qiUiX+sti1Wp"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FR/jWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EwKB6W8ZRDEH3krZihlvSOmU3sbGcixpfmbd26L9CydNisv4Uy4I=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhAlKcNsHR7IxmA8mO4hEarHbJOHubo4Ek9fOgSkshSb9sMRfMKPbrY4/PAQn1mJz57hoTqkqvcDaIMltecslemALkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUf41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgelvGUQxB95K2YoZb0jplN7GxnIsaX5m3dui/QsnTYrLjkSxD"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FR/jWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EwKB6W8ZRDEH3krZihlvSOmU3sbGcixpfmbd26L9CydNisv4Uy4I=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhAuKzwqHsfk7o2Gk1yBT30KUAoNNmbWJFCXic3Sh1MrBWu0ilsCiAmDmp5McPEXthV16dOeOJPGHanBdYPRtlhD7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUf41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgelvGUQxB95K2YoZb0jplN7GxnIsaX5m3dui/QsnTYrKQZlRT"
  }
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 71
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAlKcNsHR7IxmA8mO4hEarHbJOHubo4Ek9fOgSkshSb9sMRfMKPbrY4/PAQn1mJz57hoTqkqvcDaIMltecslemALhAuKzwqHsfk7o2Gk1yBT30KUAoNNmbWJFCXic3Sh1MrBWu0ilsCiAmDmp5McPEXthV16dOeOJPGHanBdYPRtlhD7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUf41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgelvGUQxB95K2YoZb0jplN7GxnIsaX5m3dui/QsnTYrJML034"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 71,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 600,
    "height": 71,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkYTnKf+u+B7q9"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAlKcNsHR7IxmA8mO4hEarHbJOHubo4Ek9fOgSkshSb9sMRfMKPbrY4/PAQn1mJz57hoTqkqvcDaIMltecslemALhAuKzwqHsfk7o2Gk1yBT30KUAoNNmbWJFCXic3Sh1MrBWu0ilsCiAmDmp5McPEXthV16dOeOJPGHanBdYPRtlhD7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUf41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCgelvGUQxB95K2YoZb0jplN7GxnIsaX5m3dui/QsnTYrJML034"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 71
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 71,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 600,
    "height": 71,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkYTnKf+u+B7q9"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv71OkQ=",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv71OkQ=",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv71OkQ=",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv71OkQ=",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv71OkQ=",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QE+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FSPj2uPT48oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgjAt2+/jT3WJAx/X8mmqIq5idH48B7FqmRC/tWic4jqcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALAoPsF4HwjvEq5+Ha8/jeuhTtHwh/+gYsb+znMPw2RUp6VjZDfiw==",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv71OkQ=",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QGKCwH4QrhAZalW6NlSxjh9EjItIEd/G+mKOjlSCHzXyYhF8L83hJ4c4EqxxBAsz/n9612TV0yCNuLMdzveANFkQJzURiJBCLkBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUj49rj0+PKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwKD7BeB8I7xKufh2vP43roU7R8If/oGLG/s5zD8NkVKelVzt9Gs="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QE+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FSPj2uPT48oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgjAt2+/jT3WJAx/X8mmqIq5idH48B7FqmRC/tWic4jqcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALAoPsF4HwjvEq5+Ha8/jeuhTtHwh/+gYsb+znMPw2RUp6VjZDfiw==",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCMC3b7+NPdYkDH9fyaaoirmJ0fjwHsWqZEL+1aJziOpwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAv71OkQ=",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QGKCwH4QrhAKq1u8CtkzbWmHC6w4wUFOB7vtsz7t0QcoRTrFOxzSkGSL+UAuU12Il05vPxOFunlNaFXJePRmmp+3hDcAUhkCbkBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUj49rj0+PKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwKD7BeB8I7xKufh2vP43roU7R8If/oGLG/s5zD8NkVKeldCbNCM="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QHMCwH4hLhAKq1u8CtkzbWmHC6w4wUFOB7vtsz7t0QcoRTrFOxzSkGSL+UAuU12Il05vPxOFunlNaFXJePRmmp+3hDcAUhkCbhAZalW6NlSxjh9EjItIEd/G+mKOjlSCHzXyYhF8L83hJ4c4EqxxBAsz/n9612TV0yCNuLMdzveANFkQJzURiJBCLkBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUj49rj0+PKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwKD7BeB8I7xKufh2vP43roU7R8If/oGLG/s5zD8NkVKelVuXIos="
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
    "state": "tx_+QHMCwH4hLhAKq1u8CtkzbWmHC6w4wUFOB7vtsz7t0QcoRTrFOxzSkGSL+UAuU12Il05vPxOFunlNaFXJePRmmp+3hDcAUhkCbhAZalW6NlSxjh9EjItIEd/G+mKOjlSCHzXyYhF8L83hJ4c4EqxxBAsz/n9612TV0yCNuLMdzveANFkQJzURiJBCLkBQfkBPjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUj49rj0+PKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIIwLdvv4091iQMf1/JpqiKuYnR+PAexapkQv7VonOI6nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACwKD7BeB8I7xKufh2vP43roU7R8If/oGLG/s5zD8NkVKelVuXIos="
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgVJ+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBfbp/yPHi8nqF5JlHY3gMf4+TUukk841j5dpZAlBnErrAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKBgUW15/KeAR3l78JcTSUkvpUc+r46yiGRPo9z9HV5Gi3QacDA=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFJCwH4QrhArQBp7aJsYvlezGf5PGViz/Nq3QXPPCCnGBu15VePieyMBuOrYYlxhNTwtTe1i0Us8SP4abSVm1Cr67zQMQfQBbkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FSfi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgYFFtefyngEd5e/CXE0lJL6VHPq+OsohkT6Pc/R1eRov9QDuw"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+P45AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgVJ+La4tPiyggI+AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahBfbp/yPHi8nqF5JlHY3gMf4+TUukk841j5dpZAlBnErrAQCDD0JAAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwKBgUW15/KeAR3l78JcTSUkvpUc+r46yiGRPo9z9HV5Gi3QacDA=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAlJOdgOqkPwFB26nYubOrIvm5DhR2VlRwV2FgplzhZDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAtAttlg==",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFJCwH4QrhAaHiC5XOzBdpOZtcNIH7a9dlIsbXH5UvDQrG8i5SGQZGmu1ulAYIayhKpd+8ZTygB1qdhN33hshaax5dKSOSMBbkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FSfi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgYFFtefyngEd5e/CXE0lJL6VHPq+OsohkT6Pc/R1eRosTpd0O"
  }
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 73
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAaHiC5XOzBdpOZtcNIH7a9dlIsbXH5UvDQrG8i5SGQZGmu1ulAYIayhKpd+8ZTygB1qdhN33hshaax5dKSOSMBbhArQBp7aJsYvlezGf5PGViz/Nq3QXPPCCnGBu15VePieyMBuOrYYlxhNTwtTe1i0Us8SP4abSVm1Cr67zQMQfQBbkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FSfi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgYFFtefyngEd5e/CXE0lJL6VHPq+OsohkT6Pc/R1eRovvPoTI"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 73,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 718,
    "height": 73,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAArMtts"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGLCwH4hLhAaHiC5XOzBdpOZtcNIH7a9dlIsbXH5UvDQrG8i5SGQZGmu1ulAYIayhKpd+8ZTygB1qdhN33hshaax5dKSOSMBbhArQBp7aJsYvlezGf5PGViz/Nq3QXPPCCnGBu15VePieyMBuOrYYlxhNTwtTe1i0Us8SP4abSVm1Cr67zQMQfQBbkBAPj+OQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FSfi2uLT4soICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgJSTnYDqpD8BQdup2LmzqyL5uQ4UdlZUcFdhYKZc4WQwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgYFFtefyngEd5e/CXE0lJL6VHPq+OsohkT6Pc/R1eRovvPoTI"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 73
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 73,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 718,
    "height": 73,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAArMtts"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FSvjWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmwKDNoEaa2yiL1+5O+TpJQEIdkYI0VP//9Xb5B18BMY+8TPvd6C4=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhAE2PPqFKT6r64CCy87qivPxEqMADxOtejusJ2wZMCixrxxZxnNX8KqGWdHk/AZXiZ3+4wxPSrIp4SqnYbM9wABbkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUr41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgzaBGmtsoi9fuTvk6SUBCHZGCNFT///V2+QdfATGPvEx392YS"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FSvjWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYLG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmwKDNoEaa2yiL1+5O+TpJQEIdkYI0VP//9Xb5B18BMY+8TPvd6C4=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aHTUoC",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhAxSaJo+iip1VWgic4ywphyoVKGkAKGvonGVbXVhoLnjVolXjBY0Yz6F84uQtk5LjRRmdRODtklx7y3G8K7SaMDLkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUr41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgzaBGmtsoi9fuTvk6SUBCHZGCNFT///V2+QdfATGPvEx3xTpZ"
  }
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 74
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAE2PPqFKT6r64CCy87qivPxEqMADxOtejusJ2wZMCixrxxZxnNX8KqGWdHk/AZXiZ3+4wxPSrIp4SqnYbM9wABbhAxSaJo+iip1VWgic4ywphyoVKGkAKGvonGVbXVhoLnjVolXjBY0Yz6F84uQtk5LjRRmdRODtklx7y3G8K7SaMDLkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUr41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgzaBGmtsoi9fuTvk6SUBCHZGCNFT///V2+QdfATGPvEwPGJ07"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 74,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 600,
    "height": 74,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/qiUiX+sti1Wp"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhAE2PPqFKT6r64CCy87qivPxEqMADxOtejusJ2wZMCixrxxZxnNX8KqGWdHk/AZXiZ3+4wxPSrIp4SqnYbM9wABbhAxSaJo+iip1VWgic4ywphyoVKGkAKGvonGVbXVhoLnjVolXjBY0Yz6F84uQtk5LjRRmdRODtklx7y3G8K7SaMDLkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUr41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZsCgzaBGmtsoi9fuTvk6SUBCHZGCNFT///V2+QdfATGPvEwPGJ07"
  },
  "version": 1
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 74
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 74,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 600,
    "height": 74,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/qiUiX+sti1Wp"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
  },
  "tag": "call_contract"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FS/jWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EwKDvQLN7kFxct1a2oNcrsOVQA2MfS61w64ElWBm3SASWwCZWnok=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
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
    "tx": "tx_+QFqCwH4QrhACS2MSXUWP5JN43mFmMKxVG0PeK4JBN51ob+JV4TBn78wsgg9+g2+N/kHtoH61wi3CdYZrw6PpLj1LtaZ9uNlB7kBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUv41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCg70Cze5BcXLdWtqDXK7DlUANjH0utcOuBJVgZt0gElsB+Fowb"
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "event": "update"
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
    "tx": "tx_+QEeOQGhBoKHxseeenUyEqm0v3trQqdUTgoKKLYqDOBR73bgh24FS/jWuNT40oICPgGhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmoQX26f8jx4vJ6heSZR2N4DH+Pk1LpJPONY+XaWQJQZxK6wEAgw9CQAG4gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAg1r+0+BwtopVDDcRbykW41BvmfSZj/w7DbcFsLUYCbXcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYGccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EwKDvQLN7kFxct1a2oNcrsOVQA2MfS61w64ElWBm3SASWwCZWnok=",
    "updates": [
      {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtdwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSSEuue",
        "call_stack": [],
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "gas": 1000000,
        "gas_price": 1,
        "op": "OffChainCallContract"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+QFqCwH4QrhArtbrd05TpSBE792v33V1oxQs9knbB0cL+zOnC+gFYTPXmle31skLo/K32H4atsWbZbwqHIFLMjM2MCeRjxn9DrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUv41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCg70Cze5BcXLdWtqDXK7DlUANjH0utcOuBJVgZt0gElsA7T17R"
  }
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 75
  },
  "tag": "contract_call"
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhACS2MSXUWP5JN43mFmMKxVG0PeK4JBN51ob+JV4TBn78wsgg9+g2+N/kHtoH61wi3CdYZrw6PpLj1LtaZ9uNlB7hArtbrd05TpSBE792v33V1oxQs9knbB0cL+zOnC+gFYTPXmle31skLo/K32H4atsWbZbwqHIFLMjM2MCeRjxn9DrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUv41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCg70Cze5BcXLdWtqDXK7DlUANjH0utcOuBJVgZt0gElsCKHfM4"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 75,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 600,
    "height": 75,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkYTnKf+2wRpHk"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": "2"
  },
  "tag": "contract_call"
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
      "method": "channels.get.contract_call",
      "params": {
        "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
        "round": "2"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "caller": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "contract": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "round": 75
  },
  "tag": "contract_call"
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QGsCwH4hLhACS2MSXUWP5JN43mFmMKxVG0PeK4JBN51ob+JV4TBn78wsgg9+g2+N/kHtoH61wi3CdYZrw6PpLj1LtaZ9uNlB7hArtbrd05TpSBE792v33V1oxQs9knbB0cL+zOnC+gFYTPXmle31skLo/K32H4atsWbZbwqHIFLMjM2MCeRjxn9DrkBIfkBHjkBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBUv41rjU+NKCAj4BoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEF9un/I8eLyeoXkmUdjeAx/j5NS6STzjWPl2lkCUGcSusBAIMPQkABuIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAINa/tPgcLaKVQw3EW8pFuNQb5n0mY/8Ow23BbC1GAm13AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGBnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhMCg70Cze5BcXLdWtqDXK7DlUANjH0utcOuBJVgZt0gElsCKHfM4"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "caller_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "caller_nonce": 75,
    "contract_id": "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7",
    "gas_price": 1,
    "gas_used": 600,
    "height": 75,
    "log": [],
    "return_type": "ok",
    "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAkYTnKf+2wRpHk"
  },
  "tag": "contract_call",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
    ],
    "contracts": [
      "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
    ]
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "poi": "pi_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AAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPkBy6C5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6oRpbml0uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+5AUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///////////////////////////////////////////kBNKDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtd45nZXRfYmFsYW5jZV9vZrjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAA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"
  },
  "tag": "poi",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
    ],
    "contracts": [
      "ct_2sk672NvzjmUyv3cj7kLp4k8KQL6H8U9c7nR1oLJ8Bh7GCJWg7"
    ]
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "poi": "pi_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AAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPkBy6C5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6oRpbml0uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+5AUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///////////////////////////////////////////kBNKDWv7T4HC2ilUMNxFvKRbjUG+Z9JmP/DsNtwWwtRgJtd45nZXRfYmFsYW5jZV9vZrjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAA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"
  },
  "tag": "poi",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: accounts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: contracts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: accounts, contracts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_found",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  },
  "tag": "poi"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_found",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: accounts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: contracts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "broken_encoding: accounts, contracts",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_found",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  },
  "tag": "poi"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "reason": "not_found",
    "request": {
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
      }
    }
  },
  "version": 1
}
```
