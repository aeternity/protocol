# Encoding scheme for API identifiers and byte arrays

The æternity node uses
[base58Check](https://en.bitcoin.it/wiki/Base58Check_encoding)
encoding for identifiers such as account and contract public
keys. Base58c is not well suited for encoding big byte arrays, so for
general byte arrays base64 is used.

The base64 encoded data is treated in the same way as the base58Check
encoded data, i.e., a checksum is postfixed to the binary data before
encoding. The checksum is the first four bytes of the sha256 hash of
the sha256 hash of the original byte array.

The following erlang snippet shows how the checksum can be computed,
and how it is added to the byte array that is to be encoded.

```erlang
add_check_bytes(Bin) when is_binary(Bin) ->
  <<Check:4/binary, _/binary>> = sha256(sha256(Binary)),
  <<Bin/binary, Check/binary>>.
```

Both identifiers and general byte arrays are prefixed with a two
letter tag and a separator (`_`), describing the type of data that is
encoded. For example an account pubkey could look as
`ak_2a1j2Mk9YSmC1gioUq4PWRm3bsv887MbuRVwyv4KaUGoR1eiKi`.

The tags are described below, together with the encoding method of the
tag.

| Prefix  | Encoding | Description |
| ---     | ---      | --- |
| ak      | base58   | Account pubkey |
| ba      | base64   | Byte array |
| bf      | base58   | Block Proof of Fraud hash |
| bs      | base58   | Block State hash |
| bx      | base58   | Block transaction hash |
| cb      | base64   | Contract byte array |
| ch      | base58   | Channel |
| cm      | base58   | Commitment |
| ct      | base58   | Contract pubkey |
| kh      | base58   | Key block hash |
| mh      | base58   | Micro block hash |
| nm      | base58   | Name |
| ok      | base58   | Oracle pubkey |
| oq      | base58   | Oracle query id |
| or      | base64   | Oracle response |
| ov      | base64   | Oracle query |
| pi      | base64   | Proof of Inclusion |
| pp      | base58   | Peer pubkey |
| sg      | base58   | Signature |
| ss      | base64   | State trees |
| cs      | base64   | Contract calls state tree |
| ck      | base64   | Contract state key |
| cv      | base64   | Contract state value |
| st      | base64   | State |
| th      | base58   | Transaction hash |
| tx      | base64   | Transaction |
