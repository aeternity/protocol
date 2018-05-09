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

### Key storage

Both the public key and private key are encrypted with AES in ECB mode when stored on disk.

```
enc_sk = AES_ECB_ENC(sk_bin, SHA256(password))
enc_pk = AES_ECB_ENC(pk_bin, SHA256(password))
sk = AES_ECB_DEC(enc_sk, SHA256(password))
sk = AES_ECB_DEC(enc_sk, SHA256(password))
```

### Mempool

- transactions with invalid signatures will be dropped
-

### [API](./epoch/api/README.md)
