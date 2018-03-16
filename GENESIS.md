# Genesis

The genesis block of the Aeternity blockchain will contain the initial
distribution of coins.

## ERC20 token

After collecting funds via an ICO, Aeternity issued an ERC20 token `AET` on the
Ethereum blockchain. Such a token is, at the most fundamental level, just a
mapping from a set of Ethereum addresses to their respective balances and a
standardised interface to interact with the token. It is setup in such a way
that modifying the balance for a given address requires a valid signature of a
public key for that address.

The `AET` tokens function as IOUs for the the initial distribution of coins for
the Aeternity blockchain and they will be usable until `Mon Sep 02 19:56:09 2019 UTC` after which the smart contract should refuse any token transfers.

Given that the ERC20 token is transferable until late 2019, we are going to

1. have to take a snapshot at a target block
2. or have users burn their tokens, e.g. via sending them to the token contract
   itself,
   
in order to be able to come up with an initial distribution, since we do not
want to wait until the tokens are no longer transferable.

It is important to note, that users will need to withdraw their tokens from
(centralised) exchanges in either case if they do not want to have to rely on
these exchanges to start supporting the Aeternity blockchain and distribute
their coins accordingly.

## Snapshot

A snapshot is simply taking the state of the contract, that is the set of
`(address, balance)` pairs, and put those into the genesis block.

This is arguably the simplest solution but it comes with a couple of downsides.

First of all, it forces us to use the same address scheme as Ethereum, i.e. an
address is `KECCAK256(ECDSAPUBKEY(priv_key))[96:255]` or the rightmost 160 bit
of the the public keys' Keccak-256 hash, while the current plan is to use EdDSA/Ed25519 for signatures.
(***TODO***: Alternative would be to support multiple signature schemes? How
much would that increase verification effort/complexity?)

Second downside is that it promotes private key re-use, which is akin to re-using passwords, just worse, especially given the context and the fact that now
the security of their private keys relies on even more parties.


## Token burning

A more involved solution would be to have users actively burn their tokens and
supply the address that they want to use on the Aeternity chain.

The disadvantage of this approach is that it requires active involvement of the
users. That is, while the process can be automated easily, it still requires
users to initiate the process and issue a transaction on the Ethereum chain.

Since not all users would finish this process in time, as witnessed numerous
times for other projects, where people stop paying attention for months at a
time, a pair of smart contracts could be set up on the Ethereum and Aeternity chain, which could be used to hand out unclaimed coins. (***TODO:*** Give
detailed explanation for this)

## 