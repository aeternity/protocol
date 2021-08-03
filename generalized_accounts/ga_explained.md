# Generalized accounts - explained

Generalized accounts are motivated and described from a protocol perspective
[here](./README.md). However, there are several
pitfalls and important aspects that deserve a further discussion. We aim to
provide further guidance when it comes to generalized accounts here.

## Table of Contents
- [Transaction integrity](#transaction-integrity)
- [GA authentication](#ga-authentication)
- [ECDSA Example](#ecdsa-example)
- [PayingFor Example](#payingfor-example)

## Transaction integrity

For plain old accounts (POA) transaction integrity comes down to two things;
(1) the origin of the transaction - only the owner of an account may produce
transactions originating from the account, and (2) a transaction can only be
included once - i.e. it is not possible to include the same SpendTx twice to
get double payment. (1) is achieved by [crypotographic
signing](https://en.wikipedia.org/wiki/Digital_signature), aeternity uses
[EdDSA](https://en.wikipedia.org/wiki/EdDSA) signatures with
([Curve25519](https://en.wikipedia.org/wiki/Curve25519)). (2) is normally
achieved by adding a (sequential) *nonce* to the transaction, and then the
consensus algorithm only allows an account to "use" a nonce once.

In the aeternity blockchain when a transaction is prepared for inclusion a
suitable nonce is selected and included in the transaction, then the
transaction (`TX`) is serialized (`SerTX`) and hashed. The resulting hash is
then signed yielding a signature (`SigTX`); finally the serialized transaction
and the signature (`{SerTX, SigTX}`) is posted to the transaction mempool for
inclusion on chain.

## GA authentication

As described in [Generalized accounts](./README.md), GAs are mainly a
way to give more flexibility when it comes to transaction integrity, in
particular when it comes to signing. This is done by moving *both* the nonce
handling and signature checking to a smart contract that is attached to the
account.

This means that the workflow when preparing a transaction is altered. Here we
describe it in general terms, a concrete example can be found [further
down](#ecdsa-example). The underlying transactions (SpendTX, OracleRegisterTX,
...) are not changed, but since the nonce-handling is moved to the GA
authentication contract the basic TX is required to have `nonce = 0` (to
indicate that it isn't used). As with POAs the transaction is serialized and
hashed. Then comes the different part - now the *transaction hash*, and a
*nonce* (to avoid replay attacks) has to be combined and cryptographically
secured in some way. This is where *generic* comes in, anything that can be
produced and then later checked in the authentication contract (in a safe way!)
can be used. The resulting artifact should be a piece of contract
[Calldata](../contracts/aevm.md#initialization).
Finally, in order to post
the GA signed transaction to the transaction mempool, we have to prepare a
*GAMetaTX*, containing the serialized transaction and the calldata (and gas,
gas price, etc.)

## ECDSA Example

A concrete example of a GA authentication contract might provide further
insight. Here we use EcDSA (and `curve_secp256k1`) for signing, and we have the
same nonce handling as for POA, i.e. nonces have to be sequential.

```
contract ECDSAAuth =
  record state = { nonce : int, owner : bytes(20) }

  entrypoint init(owner' : bytes(20)) = { nonce = 1, owner = owner' }

  stateful entrypoint authorize(n : int, s : bytes(65)) : bool =
    require(n >= state.nonce, "Nonce too low")
    require(n =< state.nonce, "Nonce too high")
    put(state{ nonce = n + 1 })
    switch(Auth.tx_hash)
      None          => abort("Not in Auth context")
      Some(tx_hash) => Crypto.ecverify_secp256k1(to_sign(tx_hash, n), state.owner, s)

  function to_sign(h : hash, n : int) : hash =
    Crypto.blake2b((h, n))
```

### Contract state/initialization

The contract state contains the public key used for signing (`owner`) and the
current `nonce`. The public key is provided to the `init` function (called at
contract creation) and `nonce` is initialized to `1`.

### Authorization

The authorization function takes two parameters, the nonce and the signature.
The authorization function checks that the nonce is correct, and then proceeds
to fetch the TX hash from the contract environment using `Auth.tx_hash`. In
this example the signature is for the value `blake2b(tx_hash, nonce)` (i.e.
Blake2b hash of the tuple of the transaction hash and the nonce). The
authorization finally checks that the private key corresponding to `owner` was
used to sign this hash.

### Caveat - producing the right hash

It is trivial to produce the hash in the contract, `Crypto.blake2b((h, n))` -
but it is not as straigthforward to do it _outside_ the contract. After all it
is the Sophia ABI encoded tuple of a hash and an integer that is hashed. It
isn't impossible to figure this out, but there is an easier way... *Protip:*
Using the `dry-run` functionality we can call the contract off-chain and use
the `to_sign` function to produce exactly the right hash!

## PayingFor Example
One potential use-case for Generalized accounts is to be able to pay for
transactions in a more decentralized way. Using `PayingForTx` it is easy for
part A to get a transaction from part B, put it inside a `PayingForTx` and sign
it. And hence part A pays for the transaction of part B. **But** it requires
that A and B communicate directly, and that part A produces a signature. Imagine
a case where part A would like to (blindly) pay for all calls to a particular
contract given that they are made by a known account (perhaps a user of some
kind or something similar).

A very simplistic authentication contract that achieve this is listed here:
```
contract PayForExample =
  type set('a) = map('a, unit)
  record state = { the_contract : address, allowed_users : set(address) }

  entrypoint init(c : address, us : set(address)) =
    { the_contract = c, allowed_users = us }

  entrypoint authenticate() =
    switch(Auth.tx)
      None => abort("Not in Auth context")
      Some({tx = Chain.ContractCallTx(ct_addr, _),
            actor = who, paying_for = Some(_)}) =>
        require(ct_addr == state.the_contract, "Bad transaction - wrong contract")
        require(Map.member(who, state.allowed_users), "Bad transaction - not allowed account")
        true
      _ => abort("Bad transaction")
```

Note: in a realistic use-case it is probably advisable to have an admin
interface so that you can add (and remore) allowed users later on, etc.
