
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm&keep_running=false&lock_period=10&port=14035&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr&role=initiator
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_40FZWip6Uwfd4PV3np3mDtvgFjNp/+5dF4+30nh+DxH/Bxf7"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm&keep_running=false&lock_period=10&port=14035&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr&role=responder
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_ApMmQo5SGRHN5ZEw1peUKC6qO+BhQJ/CpSuxg8DQIEYJqOeh"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "channel_open"
    }
  },
  "version": 1
}
```

#### responder info
> Received an WebSocket opening request

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "channel_accept"
    }
  },
  "version": 1
}
```

#### initiator info
> Received an WebSocket connection accepted

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAYFyX20tJ3kJWZba8QX1zQgAqZ+Fvto7b6xDt9XcJ52mhj+qJSJgAKEBY7BAnZQdwHCfa8IWz8sy3BIvv194bbM9K7ToL6Ya5sOGJGE5yoAAAgoAhhAGeddIAMCg7HrkhJzrXwFy5IKtmxhbJuaCbjSV3VFmmnRgb+Tsdg8E+11/Iw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422684,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEA4PS+DlHDD24g9Y8D6uaKdXWZmtxLxoyBDuPHfrCp0XpLcigZ1L57u7iXdWpOpdJLdpfkvgW4XLXbuqUlWvEkDuIP4gTIBoQGBcl9tLSd5CVmW2vEF9c0IAKmfhb7aO2+sQ7fV3CedpoY/qiUiYAChAWOwQJ2UHcBwn2vCFs/LMtwSL79feG2zPSu06C+mGubDhiRhOcqAAAIKAIYQBnnXSADAoOx65ISc618BcuSCrZsYWybmgm40ld1RZpp0YG/k7HYPBJhxhIs="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422684,
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
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "event": "funding_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "fsm_id": "ba_ApMmQo5SGRHN5ZEw1peUKC6qO+BhQJ/CpSuxg8DQIEYJqOeh",
      "signed_tx": "tx_+MsLAfhCuEA4PS+DlHDD24g9Y8D6uaKdXWZmtxLxoyBDuPHfrCp0XpLcigZ1L57u7iXdWpOpdJLdpfkvgW4XLXbuqUlWvEkDuIP4gTIBoQGBcl9tLSd5CVmW2vEF9c0IAKmfhb7aO2+sQ7fV3CedpoY/qiUiYAChAWOwQJ2UHcBwn2vCFs/LMtwSL79feG2zPSu06C+mGubDhiRhOcqAAAIKAIYQBnnXSADAoOx65ISc618BcuSCrZsYWybmgm40ld1RZpp0YG/k7HYPBJhxhIs=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422683,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAOD0vg5Rww9uIPWPA+rminV1mZrcS8aMgQ7jx36wqdF6S3IoGdS+e7u4l3VqTqXSS3aX5L4FuFy127qlJVrxJA7hA2a7IMcYD5JnzzUsMAi+WFVaG4d5ooICbEBeo/etT+lJwDQ/UKZt81h0QY/mKEusf0ka5IPdNpC9sII/g1JKcC7iD+IEyAaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGP6olImAAoQFjsECdlB3AcJ9rwhbPyzLcEi+/X3htsz0rtOgvphrmw4YkYTnKgAACCgCGEAZ510gAwKDseuSEnOtfAXLkgq2bGFsm5oJuNJXdUWaadGBv5Ox2DwR9UBIW"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
  "id": -576460752303422683,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAOD0vg5Rww9uIPWPA+rminV1mZrcS8aMgQ7jx36wqdF6S3IoGdS+e7u4l3VqTqXSS3aX5L4FuFy127qlJVrxJA7hA2a7IMcYD5JnzzUsMAi+WFVaG4d5ooICbEBeo/etT+lJwDQ/UKZt81h0QY/mKEusf0ka5IPdNpC9sII/g1JKcC7iD+IEyAaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGP6olImAAoQFjsECdlB3AcJ9rwhbPyzLcEi+/X3htsz0rtOgvphrmw4YkYTnKgAACCgCGEAZ510gAwKDseuSEnOtfAXLkgq2bGFsm5oJuNJXdUWaadGBv5Ox2DwR9UBIW",
      "type": "channel_create_tx"
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
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_40FZWip6Uwfd4PV3np3mDtvgFjNp/+5dF4+30nh+DxH/Bxf7"
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
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAOD0vg5Rww9uIPWPA+rminV1mZrcS8aMgQ7jx36wqdF6S3IoGdS+e7u4l3VqTqXSS3aX5L4FuFy127qlJVrxJA7hA2a7IMcYD5JnzzUsMAi+WFVaG4d5ooICbEBeo/etT+lJwDQ/UKZt81h0QY/mKEusf0ka5IPdNpC9sII/g1JKcC7iD+IEyAaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGP6olImAAoQFjsECdlB3AcJ9rwhbPyzLcEi+/X3htsz0rtOgvphrmw4YkYTnKgAACCgCGEAZ510gAwKDseuSEnOtfAXLkgq2bGFsm5oJuNJXdUWaadGBv5Ox2DwR9UBIW",
      "type": "channel_create_tx"
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
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAOD0vg5Rww9uIPWPA+rminV1mZrcS8aMgQ7jx36wqdF6S3IoGdS+e7u4l3VqTqXSS3aX5L4FuFy127qlJVrxJA7hA2a7IMcYD5JnzzUsMAi+WFVaG4d5ooICbEBeo/etT+lJwDQ/UKZt81h0QY/mKEusf0ka5IPdNpC9sII/g1JKcC7iD+IEyAaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGP6olImAAoQFjsECdlB3AcJ9rwhbPyzLcEi+/X3htsz0rtOgvphrmw4YkYTnKgAACCgCGEAZ510gAwKDseuSEnOtfAXLkgq2bGFsm5oJuNJXdUWaadGBv5Ox2DwR9UBIW",
      "type": "channel_create_tx"
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
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAOD0vg5Rww9uIPWPA+rminV1mZrcS8aMgQ7jx36wqdF6S3IoGdS+e7u4l3VqTqXSS3aX5L4FuFy127qlJVrxJA7hA2a7IMcYD5JnzzUsMAi+WFVaG4d5ooICbEBeo/etT+lJwDQ/UKZt81h0QY/mKEusf0ka5IPdNpC9sII/g1JKcC7iD+IEyAaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGP6olImAAoQFjsECdlB3AcJ9rwhbPyzLcEi+/X3htsz0rtOgvphrmw4YkYTnKgAACCgCGEAZ510gAwKDseuSEnOtfAXLkgq2bGFsm5oJuNJXdUWaadGBv5Ox2DwR9UBIW",
      "type": "channel_create_tx"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello",
    "to": "ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "message": {
        "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
        "from": "ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm",
        "info": "Hello",
        "to": "ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
    "to": "ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "message": {
        "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
        "from": "ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr",
        "info": "Hello back",
        "to": "ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422682,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm",
      "ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
  "id": -576460752303422682,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm",
      "balance": 69999999999999
    },
    {
      "account": "ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder info
> Channel is `open` and ready to use

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "state": "tx_+QENCwH4hLhAOD0vg5Rww9uIPWPA+rminV1mZrcS8aMgQ7jx36wqdF6S3IoGdS+e7u4l3VqTqXSS3aX5L4FuFy127qlJVrxJA7hA2a7IMcYD5JnzzUsMAi+WFVaG4d5ooICbEBeo/etT+lJwDQ/UKZt81h0QY/mKEusf0ka5IPdNpC9sII/g1JKcC7iD+IEyAaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGP6olImAAoQFjsECdlB3AcJ9rwhbPyzLcEi+/X3htsz0rtOgvphrmw4YkYTnKgAACCgCGEAZ510gAwKDseuSEnOtfAXLkgq2bGFsm5oJuNJXdUWaadGBv5Ox2DwR9UBIW"
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
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Channel is `open` and ready to use

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "state": "tx_+QENCwH4hLhAOD0vg5Rww9uIPWPA+rminV1mZrcS8aMgQ7jx36wqdF6S3IoGdS+e7u4l3VqTqXSS3aX5L4FuFy127qlJVrxJA7hA2a7IMcYD5JnzzUsMAi+WFVaG4d5ooICbEBeo/etT+lJwDQ/UKZt81h0QY/mKEusf0ka5IPdNpC9sII/g1JKcC7iD+IEyAaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGP6olImAAoQFjsECdlB3AcJ9rwhbPyzLcEi+/X3htsz0rtOgvphrmw4YkYTnKgAACCgCGEAZ510gAwKDseuSEnOtfAXLkgq2bGFsm5oJuNJXdUWaadGBv5Ox2DwR9UBIW"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr",
    "to": "ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuuVxL8kZKX3ZlgYKQ8cuWYBuPAZ25slM4M6hicAFld5AqBRKdAo9Ra0kJxynZwYowrhRLTvz49zVGnqVpE47qEsW/EUGOk=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr",
          "op": "OffChainTransfer",
          "to": "ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm"
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
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECWAm0lcXHOepfw1/kRLpP592hYESdLCOw4stBkRPcoY5Pgr+HKS/6g0qH3HMXJglbl4sN8MQvc8Zs7c4amonYOuEj4RjkCoQbrlcS/JGSl92ZYGCkPHLlmAbjwGdubJTODOoYnABZXeQKgUSnQKPUWtJCccp2cGKMK4US078+Pc1Rp6laROO6hLFtOMrzF"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 1
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr",
    "to": "ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuuVxL8kZKX3ZlgYKQ8cuWYBuPAZ25slM4M6hicAFld5AqBRKdAo9Ra0kJxynZwYowrhRLTvz49zVGnqVpE47qEsW/EUGOk=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr",
          "op": "OffChainTransfer",
          "to": "ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm"
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
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAMrkIPl/QK1tM/f3apILsWwAfY7ASBdqaLriLtE2JtwZqxxOksW38iofD56c3ooxZEE5lvvMwc+MX9rk7JBeIGuECWAm0lcXHOepfw1/kRLpP592hYESdLCOw4stBkRPcoY5Pgr+HKS/6g0qH3HMXJglbl4sN8MQvc8Zs7c4amonYOuEj4RjkCoQbrlcS/JGSl92ZYGCkPHLlmAbjwGdubJTODOoYnABZXeQKgUSnQKPUWtJCccp2cGKMK4US078+Pc1Rp6laROO6hLFtw/r11"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "state": "tx_+NILAfiEuEAMrkIPl/QK1tM/f3apILsWwAfY7ASBdqaLriLtE2JtwZqxxOksW38iofD56c3ooxZEE5lvvMwc+MX9rk7JBeIGuECWAm0lcXHOepfw1/kRLpP592hYESdLCOw4stBkRPcoY5Pgr+HKS/6g0qH3HMXJglbl4sN8MQvc8Zs7c4amonYOuEj4RjkCoQbrlcS/JGSl92ZYGCkPHLlmAbjwGdubJTODOoYnABZXeQKgUSnQKPUWtJCccp2cGKMK4US078+Pc1Rp6laROO6hLFtw/r11"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH&host=localhost&offchain_tx=tx_%2BNILAfiEuEAMrkIPl%2FQK1tM%2Ff3apILsWwAfY7ASBdqaLriLtE2JtwZqxxOksW38iofD56c3ooxZEE5lvvMwc%2BMX9rk7JBeIGuECWAm0lcXHOepfw1%2FkRLpP592hYESdLCOw4stBkRPcoY5Pgr%2BHKS%2F6g0qH3HMXJglbl4sN8MQvc8Zs7c4amonYOuEj4RjkCoQbrlcS%2FJGSl92ZYGCkPHLlmAbjwGdubJTODOoYnABZXeQKgUSnQKPUWtJCccp2cGKMK4US078%2BPc1Rp6laROO6hLFtw%2Fr11&port=14035&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 2000,
        "message": "Missing field: existing_fsm_id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH&existing_fsm_id=Invalid&host=localhost&offchain_tx=tx_%2BNILAfiEuEAMrkIPl%2FQK1tM%2Ff3apILsWwAfY7ASBdqaLriLtE2JtwZqxxOksW38iofD56c3ooxZEE5lvvMwc%2BMX9rk7JBeIGuECWAm0lcXHOepfw1%2FkRLpP592hYESdLCOw4stBkRPcoY5Pgr%2BHKS%2F6g0qH3HMXJglbl4sN8MQvc8Zs7c4amonYOuEj4RjkCoQbrlcS%2FJGSl92ZYGCkPHLlmAbjwGdubJTODOoYnABZXeQKgUSnQKPUWtJCccp2cGKMK4US078%2BPc1Rp6laROO6hLFtw%2Fr11&port=14035&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH&existing_fsm_id=ba_JuLtGmqUw7RuuEdO&host=localhost&offchain_tx=tx_%2BNILAfiEuEAMrkIPl%2FQK1tM%2Ff3apILsWwAfY7ASBdqaLriLtE2JtwZqxxOksW38iofD56c3ooxZEE5lvvMwc%2BMX9rk7JBeIGuECWAm0lcXHOepfw1%2FkRLpP592hYESdLCOw4stBkRPcoY5Pgr%2BHKS%2F6g0qH3HMXJglbl4sN8MQvc8Zs7c4amonYOuEj4RjkCoQbrlcS%2FJGSl92ZYGCkPHLlmAbjwGdubJTODOoYnABZXeQKgUSnQKPUWtJCccp2cGKMK4US078%2BPc1Rp6laROO6hLFtw%2Fr11&port=14035&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH&existing_fsm_id=ba_TlRWABDIo%2BQRHBo1gjzglbxRVwPFIlM%2FsvK30rXLSvx4tdW%2B&host=localhost&offchain_tx=tx_%2BNILAfiEuEAMrkIPl%2FQK1tM%2Ff3apILsWwAfY7ASBdqaLriLtE2JtwZqxxOksW38iofD56c3ooxZEE5lvvMwc%2BMX9rk7JBeIGuECWAm0lcXHOepfw1%2FkRLpP592hYESdLCOw4stBkRPcoY5Pgr%2BHKS%2F6g0qH3HMXJglbl4sN8MQvc8Zs7c4amonYOuEj4RjkCoQbrlcS%2FJGSl92ZYGCkPHLlmAbjwGdubJTODOoYnABZXeQKgUSnQKPUWtJCccp2cGKMK4US078%2BPc1Rp6laROO6hLFtw%2Fr11&port=14035&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH&existing_fsm_id=ba_40FZWip6Uwfd4PV3np3mDtvgFjNp%2F%2B5dF4%2B30nh%2BDxH%2FBxf7&host=localhost&offchain_tx=tx_%2BNILAfiEuEAMrkIPl%2FQK1tM%2Ff3apILsWwAfY7ASBdqaLriLtE2JtwZqxxOksW38iofD56c3ooxZEE5lvvMwc%2BMX9rk7JBeIGuECWAm0lcXHOepfw1%2FkRLpP592hYESdLCOw4stBkRPcoY5Pgr%2BHKS%2F6g0qH3HMXJglbl4sN8MQvc8Zs7c4amonYOuEj4RjkCoQbrlcS%2FJGSl92ZYGCkPHLlmAbjwGdubJTODOoYnABZXeQKgUSnQKPUWtJCccp2cGKMK4US078%2BPc1Rp6laROO6hLFtw%2Fr11&port=14035&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_40FZWip6Uwfd4PV3np3mDtvgFjNp/+5dF4+30nh+DxH/Bxf7"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBuuVxL8kZKX3ZlgYKQ8cuWYBuPAZ25slM4M6hicAFld5oQGBcl9tLSd5CVmW2vEF9c0IAKmfhb7aO2+sQ7fV3CedpoY3+rnizACGHLHOiuwAAIYPXtZ/KAAFnJZnKg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422681,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuECHaISA5fIKRcFM2VVQp0vy/s4hx9qCoM9YK+WegZmn5zjkBPOWle5R91wQHUvR7wUXbSuy145aOnTUJcXdPIwFuF/4XTUBoQbrlcS/JGSl92ZYGCkPHLlmAbjwGdubJTODOoYnABZXeaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGN/q54swAhhyxzorsAACGD17WfygABRHzM94="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
  "id": -576460752303422681,
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
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "event": "shutdown"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "signed_tx": "tx_+KcLAfhCuECHaISA5fIKRcFM2VVQp0vy/s4hx9qCoM9YK+WegZmn5zjkBPOWle5R91wQHUvR7wUXbSuy145aOnTUJcXdPIwFuF/4XTUBoQbrlcS/JGSl92ZYGCkPHLlmAbjwGdubJTODOoYnABZXeaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGN/q54swAhhyxzorsAACGD17WfygABRHzM94=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422680,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuECHaISA5fIKRcFM2VVQp0vy/s4hx9qCoM9YK+WegZmn5zjkBPOWle5R91wQHUvR7wUXbSuy145aOnTUJcXdPIwFuECMDYze3J/o/5XTB9xXqan7ppBEMzqSWN9/FmeHSkUldSEN1Rttp01ye0a36xuqhRXRlO3/YrUKyZckQSBUka0PuF/4XTUBoQbrlcS/JGSl92ZYGCkPHLlmAbjwGdubJTODOoYnABZXeaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGN/q54swAhhyxzorsAACGD17WfygABdGJgW4="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
  "id": -576460752303422680,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuECHaISA5fIKRcFM2VVQp0vy/s4hx9qCoM9YK+WegZmn5zjkBPOWle5R91wQHUvR7wUXbSuy145aOnTUJcXdPIwFuECMDYze3J/o/5XTB9xXqan7ppBEMzqSWN9/FmeHSkUldSEN1Rttp01ye0a36xuqhRXRlO3/YrUKyZckQSBUka0PuF/4XTUBoQbrlcS/JGSl92ZYGCkPHLlmAbjwGdubJTODOoYnABZXeaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGN/q54swAhhyxzorsAACGD17WfygABdGJgW4=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "event": "closing"
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
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuECHaISA5fIKRcFM2VVQp0vy/s4hx9qCoM9YK+WegZmn5zjkBPOWle5R91wQHUvR7wUXbSuy145aOnTUJcXdPIwFuECMDYze3J/o/5XTB9xXqan7ppBEMzqSWN9/FmeHSkUldSEN1Rttp01ye0a36xuqhRXRlO3/YrUKyZckQSBUka0PuF/4XTUBoQbrlcS/JGSl92ZYGCkPHLlmAbjwGdubJTODOoYnABZXeaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGN/q54swAhhyxzorsAACGD17WfygABdGJgW4=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "event": "closing"
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
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuECHaISA5fIKRcFM2VVQp0vy/s4hx9qCoM9YK+WegZmn5zjkBPOWle5R91wQHUvR7wUXbSuy145aOnTUJcXdPIwFuECMDYze3J/o/5XTB9xXqan7ppBEMzqSWN9/FmeHSkUldSEN1Rttp01ye0a36xuqhRXRlO3/YrUKyZckQSBUka0PuF/4XTUBoQbrlcS/JGSl92ZYGCkPHLlmAbjwGdubJTODOoYnABZXeaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGN/q54swAhhyxzorsAACGD17WfygABdGJgW4=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuECHaISA5fIKRcFM2VVQp0vy/s4hx9qCoM9YK+WegZmn5zjkBPOWle5R91wQHUvR7wUXbSuy145aOnTUJcXdPIwFuECMDYze3J/o/5XTB9xXqan7ppBEMzqSWN9/FmeHSkUldSEN1Rttp01ye0a36xuqhRXRlO3/YrUKyZckQSBUka0PuF/4XTUBoQbrlcS/JGSl92ZYGCkPHLlmAbjwGdubJTODOoYnABZXeaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGN/q54swAhhyxzorsAACGD17WfygABdGJgW4=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "event": "closed_confirmed"
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
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "event": "died"
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
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "event": "closed_confirmed"
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
    "channel_id": "ch_2nkhoY6qQKYX47akKfmjAUDtZaG49hN4ADAe2BtUg51m4urPxH",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
