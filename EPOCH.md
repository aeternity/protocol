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
The secret key gets left padded with 0's to a length of 32bytes, since erlang's crypto library does not return it padded.
The public key currently gets padded to 128 bytes (***TODO: why not just pad it to 80 bytes which is the next 128bit multiple***)


```
enc_sk = AES_ECB_ENC(lpad(sk_bin), SHA256(password))
enc_pk = AES_ECB_ENC(rpad(pk_bin), SHA256(password))
sk = AES_ECB_DEC(enc_sk, SHA256(password))
sk = AES_ECB_DEC(enc_sk, SHA256(password))
```

### Mempool

- transactions with invalid signatures will be dropped
-

### [API](./epoch/api/README.md)
