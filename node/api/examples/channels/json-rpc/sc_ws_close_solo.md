
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_close_solo_%2F3111%5Binitiator%5D
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
      "fsm_id": "ba_qvumWoEx+iG/7VCu4bC1O1e9gu87cnLMNBEXcfEhEYMOnL7z"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_close_solo_%2F3111%5Binitiator%5D
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
      "fsm_id": "ba_+fIIGEgmuP1EFPedYq2+K/I+KU+IZ2JpW/dyz6dBh63GGdnN"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYMaaiPxQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423301,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAgYTcBu/crWrckugV++9/UQc1+1BlPwnAMpjKi5ONbC6FjPbMduBmKoSSQbK8/DgGuAlD1pxkwWDCu0OvsRpQDuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2DEE5j0U="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423301,
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
    "channel_id": null,
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
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+MsLAfhCuEAgYTcBu/crWrckugV++9/UQc1+1BlPwnAMpjKi5ONbC6FjPbMduBmKoSSQbK8/DgGuAlD1pxkwWDCu0OvsRpQDuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2DEE5j0U=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423300,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAIGE3Abv3K1q3JLoFfvvf1EHNftQZT8JwDKYyouTjWwuhYz2zHbgZiqEkkGyvPw4BrgJQ9acZMFgwrtDr7EaUA7hA66k87NTcuysIv8WOE9zmbmHilVZGmNzByAOxwfYJkq7mMq5lH/5PU0IYS1aXLEYkKohX2NcjgV9vpWFk748KCriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgz/uKKO"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423300,
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
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAIGE3Abv3K1q3JLoFfvvf1EHNftQZT8JwDKYyouTjWwuhYz2zHbgZiqEkkGyvPw4BrgJQ9acZMFgwrtDr7EaUA7hA66k87NTcuysIv8WOE9zmbmHilVZGmNzByAOxwfYJkq7mMq5lH/5PU0IYS1aXLEYkKohX2NcjgV9vpWFk748KCriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgz/uKKO",
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
    "channel_id": null,
    "data": {
      "event": "funding_signed"
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
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAIGE3Abv3K1q3JLoFfvvf1EHNftQZT8JwDKYyouTjWwuhYz2zHbgZiqEkkGyvPw4BrgJQ9acZMFgwrtDr7EaUA7hA66k87NTcuysIv8WOE9zmbmHilVZGmNzByAOxwfYJkq7mMq5lH/5PU0IYS1aXLEYkKohX2NcjgV9vpWFk748KCriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgz/uKKO",
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
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAIGE3Abv3K1q3JLoFfvvf1EHNftQZT8JwDKYyouTjWwuhYz2zHbgZiqEkkGyvPw4BrgJQ9acZMFgwrtDr7EaUA7hA66k87NTcuysIv8WOE9zmbmHilVZGmNzByAOxwfYJkq7mMq5lH/5PU0IYS1aXLEYkKohX2NcjgV9vpWFk748KCriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgz/uKKO",
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
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAIGE3Abv3K1q3JLoFfvvf1EHNftQZT8JwDKYyouTjWwuhYz2zHbgZiqEkkGyvPw4BrgJQ9acZMFgwrtDr7EaUA7hA66k87NTcuysIv8WOE9zmbmHilVZGmNzByAOxwfYJkq7mMq5lH/5PU0IYS1aXLEYkKohX2NcjgV9vpWFk748KCriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgz/uKKO",
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
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
    "data": {
      "message": {
        "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
        "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
        "info": "Hello",
        "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
    "data": {
      "message": {
        "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
        "info": "Hello back",
        "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423299,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
  "id": -576460752303423299,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "balance": 69999999999999
    },
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Channel is `open` and ready to use

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
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
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
    "data": {
      "state": "tx_+QENCwH4hLhAIGE3Abv3K1q3JLoFfvvf1EHNftQZT8JwDKYyouTjWwuhYz2zHbgZiqEkkGyvPw4BrgJQ9acZMFgwrtDr7EaUA7hA66k87NTcuysIv8WOE9zmbmHilVZGmNzByAOxwfYJkq7mMq5lH/5PU0IYS1aXLEYkKohX2NcjgV9vpWFk748KCriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgz/uKKO"
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
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
    "data": {
      "state": "tx_+QENCwH4hLhAIGE3Abv3K1q3JLoFfvvf1EHNftQZT8JwDKYyouTjWwuhYz2zHbgZiqEkkGyvPw4BrgJQ9acZMFgwrtDr7EaUA7hA66k87NTcuysIv8WOE9zmbmHilVZGmNzByAOxwfYJkq7mMq5lH/5PU0IYS1aXLEYkKohX2NcjgV9vpWFk748KCriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgz/uKKO"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBoNtMulnkG3mS43NqsOS5J1NN2hRe24hjJFHFSH1B6/KoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYC5AUz5AUk8AfkBP/kBPKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvkBGPh0oCiW0e4qVvD/C94E6/En+1vvEgzoctloLayg1hD1Tl5u+FGAgICAgICg46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVuAgICAoKcJtie4oQxB6+5JVy+F3eNaNF7V7TgRPXFlQNJ4W/wIgICAgID4T6CnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CO2gP/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWLygoBAIY/qiUiX//4T6DjooHlLkRUA0QFUOns+/GhHcvejx4IPZN7Jd7GGFRtW+2gNllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAHAwMDAwACGFT7sgIAADUIjS9w=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo_sign",
  "params": {
    "signed_tx": "tx_+QHrCwH4QrhA1wae1hdCb6krvmWKwc170/xafe4zVLoiB/9+qnuf0njpyM2xWanMQZBshxJTNcq/0+6ns76HrsoOup5oHOiuDLkBovkBnzYBoQaDbTLpZ5Bt5kuNzarDkuSdTTdoUXtuIYyRRxUh9QevyqEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWAuQFM+QFJPAH5AT/5ATygKJbR7ipW8P8L3gTr8Sf7W+8SDOhy2WgtrKDWEPVOXm75ARj4dKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvhRgICAgICAoOOigeUuRFQDRAVQ6ez78aEdy96PHgg9k3sl3sYYVG1bgICAgKCnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CICAgICA+E+gpwm2J7ihDEHr7klXL4Xd41o0XtXtOBE9cWVA0nhb/AjtoD/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVi8oKAQCGP6olIl//+E+g46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVvtoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAA2Qtsbq"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhA1wae1hdCb6krvmWKwc170/xafe4zVLoiB/9+qnuf0njpyM2xWanMQZBshxJTNcq/0+6ns76HrsoOup5oHOiuDLkBovkBnzYBoQaDbTLpZ5Bt5kuNzarDkuSdTTdoUXtuIYyRRxUh9QevyqEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWAuQFM+QFJPAH5AT/5ATygKJbR7ipW8P8L3gTr8Sf7W+8SDOhy2WgtrKDWEPVOXm75ARj4dKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvhRgICAgICAoOOigeUuRFQDRAVQ6ez78aEdy96PHgg9k3sl3sYYVG1bgICAgKCnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CICAgICA+E+gpwm2J7ihDEHr7klXL4Xd41o0XtXtOBE9cWVA0nhb/AjtoD/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVi8oKAQCGP6olIl//+E+g46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVvtoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAA2Qtsbq",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
    "data": {
      "event": "closing"
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
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhA1wae1hdCb6krvmWKwc170/xafe4zVLoiB/9+qnuf0njpyM2xWanMQZBshxJTNcq/0+6ns76HrsoOup5oHOiuDLkBovkBnzYBoQaDbTLpZ5Bt5kuNzarDkuSdTTdoUXtuIYyRRxUh9QevyqEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWAuQFM+QFJPAH5AT/5ATygKJbR7ipW8P8L3gTr8Sf7W+8SDOhy2WgtrKDWEPVOXm75ARj4dKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvhRgICAgICAoOOigeUuRFQDRAVQ6ez78aEdy96PHgg9k3sl3sYYVG1bgICAgKCnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CICAgICA+E+gpwm2J7ihDEHr7klXL4Xd41o0XtXtOBE9cWVA0nhb/AjtoD/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVi8oKAQCGP6olIl//+E+g46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVvtoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAA2Qtsbq",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
    "data": {
      "event": "closing"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBoNtMulnkG3mS43NqsOS5J1NN2hRe24hjJFHFSH1B6/KoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4Y/qiUiX/+GJGE5yoABAIYPXtZ/KAAEFSyS5w==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEALFFLSNDWP8CrXUND/EdgrEWfvYDKdO+2/+XfQgmjjiqS7KTVpYS+LvOCdPJgSNOXKS6nRvLKI6x2yDsWsE70PuF/4XTgBoQaDbTLpZ5Bt5kuNzarDkuSdTTdoUXtuIYyRRxUh9QevyqEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GP6olIl//hiRhOcqAAQCGD17WfygABGOzBdY="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEALFFLSNDWP8CrXUND/EdgrEWfvYDKdO+2/+XfQgmjjiqS7KTVpYS+LvOCdPJgSNOXKS6nRvLKI6x2yDsWsE70PuF/4XTgBoQaDbTLpZ5Bt5kuNzarDkuSdTTdoUXtuIYyRRxUh9QevyqEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GP6olIl//hiRhOcqAAQCGD17WfygABGOzBdY=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEALFFLSNDWP8CrXUND/EdgrEWfvYDKdO+2/+XfQgmjjiqS7KTVpYS+LvOCdPJgSNOXKS6nRvLKI6x2yDsWsE70PuF/4XTgBoQaDbTLpZ5Bt5kuNzarDkuSdTTdoUXtuIYyRRxUh9QevyqEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GP6olIl//hiRhOcqAAQCGD17WfygABGOzBdY=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
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
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
    "data": {
      "event": "died"
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
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
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
    "channel_id": "ch_zt7fySKq2seFgiL5MoqKBKUqHe3Rf3NJXGipQ3HsRwrbeJ399",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection
```

```

#### initiator closes WebSocket connection
```

```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_close_solo_%2F3111%5Bresponder%5D
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
      "fsm_id": "ba_au9v8fEgd4gWld8iPf+yUrxKZXzrvtiRes493w+waCh6H8W8"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_close_solo_%2F3111%5Bresponder%5D
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
      "fsm_id": "ba_+glBCP+FEczYuWUgPrOW0SOzm6UZYhld8m0Ls/XLHjNYiUVm"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYOEsndlg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423298,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAWxVg/PAxzJbU3woXdWgr0Nszos91kdJCfHq0N6EsyhHlDAEXRu4ORb4SBVh6fhIzGdcZQYvX779V0OEXhuSAAuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2DrIAmVY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423298,
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
    "channel_id": null,
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
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+MsLAfhCuEAWxVg/PAxzJbU3woXdWgr0Nszos91kdJCfHq0N6EsyhHlDAEXRu4ORb4SBVh6fhIzGdcZQYvX779V0OEXhuSAAuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2DrIAmVY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423297,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAFsVYPzwMcyW1N8KF3VoK9DbM6LPdZHSQnx6tDehLMoR5QwBF0buDkW+EgVYen4SMxnXGUGL1++/VdDhF4bkgALhAUDsmmJ3xW7+1fkBbltNRRoJyYjkQktGhZkhMPkkBso/HmDRkhAspq231AVUyHYLd+U6yQcyo4eQiCAez0fYCAbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdg6OvbB/"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423297,
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
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAFsVYPzwMcyW1N8KF3VoK9DbM6LPdZHSQnx6tDehLMoR5QwBF0buDkW+EgVYen4SMxnXGUGL1++/VdDhF4bkgALhAUDsmmJ3xW7+1fkBbltNRRoJyYjkQktGhZkhMPkkBso/HmDRkhAspq231AVUyHYLd+U6yQcyo4eQiCAez0fYCAbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdg6OvbB/",
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
    "channel_id": null,
    "data": {
      "event": "funding_signed"
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
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAFsVYPzwMcyW1N8KF3VoK9DbM6LPdZHSQnx6tDehLMoR5QwBF0buDkW+EgVYen4SMxnXGUGL1++/VdDhF4bkgALhAUDsmmJ3xW7+1fkBbltNRRoJyYjkQktGhZkhMPkkBso/HmDRkhAspq231AVUyHYLd+U6yQcyo4eQiCAez0fYCAbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdg6OvbB/",
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
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAFsVYPzwMcyW1N8KF3VoK9DbM6LPdZHSQnx6tDehLMoR5QwBF0buDkW+EgVYen4SMxnXGUGL1++/VdDhF4bkgALhAUDsmmJ3xW7+1fkBbltNRRoJyYjkQktGhZkhMPkkBso/HmDRkhAspq231AVUyHYLd+U6yQcyo4eQiCAez0fYCAbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdg6OvbB/",
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
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAFsVYPzwMcyW1N8KF3VoK9DbM6LPdZHSQnx6tDehLMoR5QwBF0buDkW+EgVYen4SMxnXGUGL1++/VdDhF4bkgALhAUDsmmJ3xW7+1fkBbltNRRoJyYjkQktGhZkhMPkkBso/HmDRkhAspq231AVUyHYLd+U6yQcyo4eQiCAez0fYCAbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdg6OvbB/",
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
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
    "data": {
      "message": {
        "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
        "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
        "info": "Hello",
        "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
    "data": {
      "message": {
        "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
        "info": "Hello back",
        "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423296,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
  "id": -576460752303423296,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "balance": 69999999999999
    },
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
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
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
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
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
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
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
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
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Channel is `open` and ready to use

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder info
> Channel is `open` and ready to use

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
    "data": {
      "state": "tx_+QENCwH4hLhAFsVYPzwMcyW1N8KF3VoK9DbM6LPdZHSQnx6tDehLMoR5QwBF0buDkW+EgVYen4SMxnXGUGL1++/VdDhF4bkgALhAUDsmmJ3xW7+1fkBbltNRRoJyYjkQktGhZkhMPkkBso/HmDRkhAspq231AVUyHYLd+U6yQcyo4eQiCAez0fYCAbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdg6OvbB/"
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
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
    "data": {
      "state": "tx_+QENCwH4hLhAFsVYPzwMcyW1N8KF3VoK9DbM6LPdZHSQnx6tDehLMoR5QwBF0buDkW+EgVYen4SMxnXGUGL1++/VdDhF4bkgALhAUDsmmJ3xW7+1fkBbltNRRoJyYjkQktGhZkhMPkkBso/HmDRkhAspq231AVUyHYLd+U6yQcyo4eQiCAez0fYCAbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdg6OvbB/"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhButxU/BthuZt400xe1G8pfH6Yol1T7BU8FPc59WRzSegoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4C5AUz5AUk8AfkBP/kBPKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvkBGPh0oCiW0e4qVvD/C94E6/En+1vvEgzoctloLayg1hD1Tl5u+FGAgICAgICg46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVuAgICAoKcJtie4oQxB6+5JVy+F3eNaNF7V7TgRPXFlQNJ4W/wIgICAgID4T6CnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CO2gP/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWLygoBAIY/qiUiX//4T6DjooHlLkRUA0QFUOns+/GhHcvejx4IPZN7Jd7GGFRtW+2gNllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAHAwMDAwACGFT7sgIAABSpsyoM=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo_sign",
  "params": {
    "signed_tx": "tx_+QHrCwH4QrhAYYygX1xKO1dqY2usG1HXxl3vikpjk0y0LPxf69irZfVV8p0dklXf+HQzlkcV0twjrjg4RXJRIgEMCmBulrdrBbkBovkBnzYBoQbrcVPwbYbmbeNNMXtRvKXx+mKJdU+wVPBT3OfVkc0noKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+AuQFM+QFJPAH5AT/5ATygKJbR7ipW8P8L3gTr8Sf7W+8SDOhy2WgtrKDWEPVOXm75ARj4dKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvhRgICAgICAoOOigeUuRFQDRAVQ6ez78aEdy96PHgg9k3sl3sYYVG1bgICAgKCnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CICAgICA+E+gpwm2J7ihDEHr7klXL4Xd41o0XtXtOBE9cWVA0nhb/AjtoD/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVi8oKAQCGP6olIl//+E+g46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVvtoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAAUWgpKC"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAYYygX1xKO1dqY2usG1HXxl3vikpjk0y0LPxf69irZfVV8p0dklXf+HQzlkcV0twjrjg4RXJRIgEMCmBulrdrBbkBovkBnzYBoQbrcVPwbYbmbeNNMXtRvKXx+mKJdU+wVPBT3OfVkc0noKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+AuQFM+QFJPAH5AT/5ATygKJbR7ipW8P8L3gTr8Sf7W+8SDOhy2WgtrKDWEPVOXm75ARj4dKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvhRgICAgICAoOOigeUuRFQDRAVQ6ez78aEdy96PHgg9k3sl3sYYVG1bgICAgKCnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CICAgICA+E+gpwm2J7ihDEHr7klXL4Xd41o0XtXtOBE9cWVA0nhb/AjtoD/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVi8oKAQCGP6olIl//+E+g46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVvtoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAAUWgpKC",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
    "data": {
      "event": "closing"
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
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAYYygX1xKO1dqY2usG1HXxl3vikpjk0y0LPxf69irZfVV8p0dklXf+HQzlkcV0twjrjg4RXJRIgEMCmBulrdrBbkBovkBnzYBoQbrcVPwbYbmbeNNMXtRvKXx+mKJdU+wVPBT3OfVkc0noKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+AuQFM+QFJPAH5AT/5ATygKJbR7ipW8P8L3gTr8Sf7W+8SDOhy2WgtrKDWEPVOXm75ARj4dKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvhRgICAgICAoOOigeUuRFQDRAVQ6ez78aEdy96PHgg9k3sl3sYYVG1bgICAgKCnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CICAgICA+E+gpwm2J7ihDEHr7klXL4Xd41o0XtXtOBE9cWVA0nhb/AjtoD/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVi8oKAQCGP6olIl//+E+g46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVvtoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAAUWgpKC",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
    "data": {
      "event": "closing"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhButxU/BthuZt400xe1G8pfH6Yol1T7BU8FPc59WRzSegoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiX/+GJGE5yoABAIYPXtZ/KAAP782OPA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEB1dIbw7SS3hsvltRuFGpeU0OzkZ5wBv8co2wvH/BG0bBe8HhGU8T22Vbg0hNTmfCfgunGik1V7L4MGgx9HjxAGuF/4XTgBoQbrcVPwbYbmbeNNMXtRvKXx+mKJdU+wVPBT3OfVkc0noKEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olIl//hiRhOcqAAQCGD17WfygAD0Yd/7A="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEB1dIbw7SS3hsvltRuFGpeU0OzkZ5wBv8co2wvH/BG0bBe8HhGU8T22Vbg0hNTmfCfgunGik1V7L4MGgx9HjxAGuF/4XTgBoQbrcVPwbYbmbeNNMXtRvKXx+mKJdU+wVPBT3OfVkc0noKEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olIl//hiRhOcqAAQCGD17WfygAD0Yd/7A=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEB1dIbw7SS3hsvltRuFGpeU0OzkZ5wBv8co2wvH/BG0bBe8HhGU8T22Vbg0hNTmfCfgunGik1V7L4MGgx9HjxAGuF/4XTgBoQbrcVPwbYbmbeNNMXtRvKXx+mKJdU+wVPBT3OfVkc0noKEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olIl//hiRhOcqAAQCGD17WfygAD0Yd/7A=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
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
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
    "data": {
      "event": "died"
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
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
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
    "channel_id": "ch_2nh4ut2TQXWfTwcd58uf7tCpZQ4nHoNt9jsCPbPzX9NoVWpzsv",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection
```

```

#### initiator closes WebSocket connection
```

```
