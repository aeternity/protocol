# Æternity epoch

This is a description of epoch, the reference implementation
of the Æternity protocol. Epoch is written in Erlang/OTP.

### Base58Check encoding


The motivation for base58check can be found on the bitcoin wiki
[https://en.bitcoin.it/wiki/Base58Check_encoding](https://en.bitcoin.it/wiki/Base58Check_encoding)

```
    // Why base-58 instead of standard base-64 encoding?
    // - Don't want 0OIl characters that look the same in some fonts and
    //      could be used to create visually identical looking account numbers.
    // - A string with non-alphanumeric characters is not as easily accepted as an account number.
    // - E-mail usually won't line-break if there's no punctuation to break at.
    // - Doubleclicking selects the whole number as one word if it's all alphanumeric.
```


#### Prefixes

All binary strings that could possibly used by humans to identify entities or
retrieve information should get a prefix after being base58check encoded. This
prefix should give users a quick idea what the string represents, e.g. if it
is a public key or the hash of a block.
This prefix is only relevant for users and maybe client applications such as
chain explorers, which might vary their logic based on a supplied prefix but
should definitely not depend on it.


```
bh    - block hash
bx    - block tx hash (transaction merkle root hash)
bs    - block state hash (state merkle root hash)
tx    - transaction
ok    - oracle pk
oq    - oracle query id
ak    - account pk
k1sig - signature (secp255k1)
k1sk  - secret key (secp255k1)
edsk  - secret key (ed25519)
edsig - signature (ed25519)
```


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
The secret key gets left padded with 0's to a length of 32bytes, since erlang's crypto library
does not return it padded. The public key currently gets padded to 128 bytes.


```
enc_sk = AES_ECB_ENC(lpad(sk_bin), SHA256(password))
enc_pk = AES_ECB_ENC(rpad(pk_bin), SHA256(password))
sk = AES_ECB_DEC(enc_sk, SHA256(password))
sk = AES_ECB_DEC(enc_sk, SHA256(password))
```


### Mempool

- transactions with invalid signatures will be dropped
-

### [API](./api/README.md)
