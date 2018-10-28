# Æternity epoch

This is a description of epoch, the reference implementation
of the Æternity protocol. Epoch is written in Erlang/OTP.

### P2P network

Peer:

```
uri
blocked
last_seen
last_pings
ping_tref
```

### Mempool

- transactions with invalid signatures will be dropped

### [API](./epoch/api/README.md)
