# Aeternity Naming System


## Abstract

This document describes the first draft of the Aeternity Naming System,
short AENS.


## Motivation

Entities native to most blockchain systems are addressed or identified
by their hashes, which are generally `n` bit numbers displayed in a hex
or base64/base58 notation, all of which are somewhat unfriendly to the
humans trying to use these systems.


## Background

A solution to a similar problem is the Domain Name System, or DNS, which
should be familiar to most people, providing human readable names for IP
addresses. The issue with DNS is its centralization and it was conjectured
by [Zooko](https://en.wikipedia.org/wiki/Zooko%27s_triangle) that a
decentralized system can't have human-meaningful names while still being
secure. This conjecture has been proven to be false by a number of systems,
one example being [NameCoin](https://www.namecoin.org), which was debuted
in 2011. It allowed users to associate names with a number of key-value
pairs. The NameCoin network still exists today but sees barely any usage.

A more recent effort is ENS, the Ethereum Name Service, which enables users
to claim names via a set of smart contracts. ENS is currently running a two
year trial deployment, during which users can claim name with a `.eth`
postfix, e.g. `mywallet.eth`. ENS currently allows users to associate a single
32 byte array of data with a node, typically used for a hash.


## Overview

Names are part of a namespace, which works just like DNS, e.g. `mywallet.aet`
or `привет.aet` are part of the same `.aet` namespace.


## Governance

This first draft of the AENS is not going to have any governance mechanism but
will only allow registrations under a single namespace: `.aet`.
We will also not include mechanisms similar to the `sunrise` and `landrush`
periods, which are common for DNS, where registration is restricted to small
select groups and trademark holders in order to avoid name squatting, before
the general public can start claiming names.


## Mechanisms

It is unclear what a good mechanism for a naming system would look
like. If we imagine two actors both being interested in the same name,
what would a »fair« solution be to resolve this?

Fees are the main mechanism to discourage spam and squatting. This
initial version will burn the governance fee, in order to enable us
to change this behaviour in the future. If we start out by giving this
fee to miners, they will be very hesitant to accept any changes, which
will impact their income negatively. Thus starting out with burning
could allow us an easier path for future update to the fee structures.

Every entry in the `.aet` namespace pays the same amount of fees.

Each entry has a fixed expiration date on claim after which the entry should
transition into the `revoked` state. Once it reaches this state, the name
will be released, i.e. transition into the `unclaimed` state, after which
it could be claimed again.

To prevent the entry from expiring a user can, at any point before reaching
the expiration date, update the entry, which pushes the expiration date
into the future by the time delta of the registration time and the update
time, e.g. if a user posts an update one week after claiming their name,
the expiration date gets pushed one week further into the future.
The main motivation of this expiration date is to prevent situations where
the private keys, which control the name, are lost making the name unusable
as well.


## Specification

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD",
"SHOULD NOT", "RECOMMENDED",  "MAY", and "OPTIONAL" in this document are to be
interpreted as described in [RFC 2119](https://tools.ietf.org/html/rfc2119).


### AENS Entry

This is the entry as it should be stored by a node.

```
  name         size (bytes)
 ------------ ----
| owner      | 32 |
 ------------ ----
| expires_by | 32 |
 ------------ ----
| client_ttl | 8  |
 ------------ ----
| pointers   |    |
 ------------ ----
```

***owner***: the account, which controls this entry.

***expires_by***: the blockheight after which the entry goes
into the `revoked` state. This value MUST NOT be further than
50000 blocks into the future.

***client_ttl***: a suggestion as to how long any clients should
cache this information. (***TODO***: should have a reasonable
upper limit, e.g. 86400 seconds, and probably a different
name to not be confused with the general TTL for transactions)

This entry is only relevant for clients and has no conensus
impact.

***pointers***: a dictionary with all the values this entry
points towards, e.g. `{kind: "ipfs", data: "QmVcSqVEsvm5RR9mBLjwpb2XjFVn5bPdPL69mL8PH45pPC"}`.
This can have multiple entries, e.g. an ipfs hash which contains a
profile picture and an payment address asssociated with the name.


### Name

Names MUST be normalized according to IDNA2008 before hashing, as
described in [uts-46](https://unicode.org/reports/tr46) and SHOULD
be stored in their ASCII representation.
The parameters to be used for normalization and validation are:

```
UseSTD3ASCIIRules=true
NontransitionalProcessing=true
CheckHyphens=true
CheckBidi=true # important for registrars, to restrict names
CheckJoiners=true # important for registrars, to restrict names
```

See also [rfc3491](https://tools.ietf.org/html/rfc3491) and
[rfc3492](https://tools.ietf.org/html/rfc3492).

Names SHOULD be at most 253 characters long, in order to enable
interoperability with DNS.

***Note:*** For this first draft names MUST have `.aet` or `.test`
as a suffix, i.e. `mywallet.aet`.


### Namespaces/Labels

A name is split up into labels by the `FULL STOP (U+002E .)` character.
These labels will also be referred to as namespaces, e.g. `mywallet.aet`
can be understood as the `mywallet` namespace in the `aet` namespace.

Any label that is not at the top level, e.g. `aet`, MUST be longer than
three characters.

Labels SHOULD be at most 63 characters long and the full path
of all names and namespaces SHOULD be at most 253 characters
long, in order to enable interoperability with DNS.


### Registrars

A registrar controls who is allowed to claim names in their namespace
and under what circumstances they are allowed to do so.

The only available registrars for this AENS version will be hard-coded
ones, which own the `.`, `.aet` and `.test` namespaces.

The `.` namespace registrar is restricted and MUST NOT allow anyone to
claim any names in its namespace.

The `.aet` namespace registrar allows users to claim any name that is
valid according to the validation rules if the name is currently not
claimed and they pay the appropriate fee.

`.aet` will be exclusively available on the mainnet and `.test`
will be exclusive to the testnet.


### Commitment Scheme

Claiming a name requires a commitment scheme, which enables the claimant
to commit to a name and after the commitment has been accepted into the
chain, reveal the name to finish the process.

A commitment should be binding, i.e. the claimant cannot change
the value they commited to withouth changing the actual commitment
and hiding, so that a malicious miner learns nothing about the value
the claimant has commited until they chose to reveal that value. This
prevents malicious miners from front running, i.e. upon seeing a
claim transaction, including their own claim request for the same
name instead of the original claimant's one.


### Hashing

We are going to adopt the `NameHash` as defined by the ENS in
[EIP-137](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-137.md#namehash-algorithm)
using Blake2b (256 bits digest) instead.

```
def namehash(name):
  if name == '':
    return '\0' * 32
  else:
    label, _, remainder = name.partition('.')
    return Blake2b(namehash(remainder) + Blake2b(label))
```

Names are generally only referred to in hashed form.


### Protocol

```
                  expire
      unclaimed <-------- revoked
          | ^              ^^
          | |              || expire
          | | expire       ||
pre-claim | |              ||  _
          | |       revoke || | | transfer
          v |              || | v
     pre-claimed -------> claimed
                  claim    | ^
                           | |
                            -
                          update
```

Note that `expire` is not an explicit message that is part
of the protocol.


#### Pre-claim

Send a `pre-claim` transaction containing a hash commitment.
This transaction starts the claiming process.

```
 ------------ ----
| commitment | 32 |
 ------------ ----
```

A client interacting with the blockchain should generate a warning
if a user tries to claim a name that is not available.

The `pre-claim` has an implicit expiration attached to it. A
`pre-claim` MUST be considered invalid after 300 blocks, i.e.
about two days at 10 minute block time.

The hash commitment for the `pre-claim` is computed as follows:

```
commitment := Hash(NameHash(name) + name_salt)
```


#### Claim

```
 ---------------- ----
| name           | 63 |
 ---------------- ----
| fee            | 32 |
 ------------- -- ----
| name_salt      | 32 |
 ---------------- ----
```

Flow for a user:

1. (optional) wait `n` blocks, s.t. that the block including the `pre-claim` cannot be reversed whp
2. send `claim` transaction to reveal name and pay the associated fee

If the time delta of `pre-claim` and `claim` is bigger than 300 blocks,
then the `claim` MUST be rejected.

The `claim` transaction MUST be signed by the same private key as a
`pre-claim` transaction containing a commitment to the name and nonce.

A `claim` transaction MUST NOT be in included in the same block as its
`pre-claim`.

Note that the fee here is a distinct fee from the normal transaction fee.


#### Update

```
 ------------ ----
| hash       | 32 |
 ------------ ----
| expire_by  | 8  |
 ------------ ----
| client_ttl | 8  |
 ------------ ----
| pointers   |    |
 ------------ ----
```

The `update` transaction MUST be signed by the owner
of the name entry to be updated.

The `expire_by` MUST NOT be more than 36000 blocks into
the future.

`update` transaction may be used to extend the lease of the name.
We do not require an additional fee for extending the lease.

#### Transfer

```
 ------------ ----
| target     | 32 |
 ------------ ----
| hash       | 32 |
 ------------ ----
```

The `transfer` transaction MUST be signed by the owner
of the name entry to be transfered.


### Revoke

```
 ------------ ----
| hash       | 32 |
 ------------ ----
```

The revoke transaction MUST be signed by the owner
of a name entry.

After the `revoke` transaction has been included in the chain,
the name enters the `revoked` state. After a fixed timeout of
2016 blocks, the name will be available for claiming again.


## Storage

We are going to store the AENS entries in an ESMT and use the
hash of a name, as defined above, as a pointer to the entry data.
If there's no entry for a given hash then that pointer will point
to an empty hash or to the hash of that entry data otherwise.


## Launch

Giving users plenty time to prepare for a launch of the naming
system is of utmost importance given the allocation rules, i.e.
first come first serve, of this first draft.
This also includes giving users the proper tools, i.e. a GUI,
in order to level the playing field as to who is able to actually
register names.

Since we don't have an auction protocol just yet, we could hold
auctions on Ethereum to establish an initial allocation of names,
just like our ERC-20 token.


## (possible) Future extensions

### Registrars

A later version of the name service should allow every user to become
a registrar and encode their registration logic in a smart contract.
A simplification would be that registrars have to submit the claim
transaction themselves and just set the owner to whoever they want to
give the name to.

These sub-labels allow for further customisation and also for users to
associate with particular namespaces, e.g. a cryptographic cat breeding
game might associate a name entry with every of its cats such as
`unicorn.kitty.aet` and then transfering that name to the person, who
adopts the cat. The authorization policies for these will need some
flexibility seeing as the owner of a namespace might want to prevent
or allow users creating sub-sub-labels, e.g. the owner of `unicorn.kitty.aet`
creating `rarest.`unicorn.kitty.aet`.


### Auctions

Using (Vickrey) auctions instead of a simple, first come
first serve approach for new claims, might allow a better
mechanism for price discovery without having to go through
a secondary market.


### URI Schema

We are currently using the same schema as DNS, which might
be problematic since this comes with a big slew of expectations
as to what can and can't be done.

See [this post about problems of urls](https://noncombatant.org/2017/11/07/problems-of-urls/)
or [this IPFS spec issue](https://github.com/ipfs/specs/pull/152) for
some discussions.

### Decentralized name exchange

Having the exchange for names on chain would enable us to
transfer names in a trustless manner. Plus having the bids
recorded on chain could also facilitate better price discovery.


### Governance

Allowing users to register their own namespaces and become
registrars themselves, i.e. if I own `mywallet.aet`, I can
then allow others to register `name.mywallet.aet`.

Consider a voting mechanism to introduce new TLDs.


### Interoperability

- investigate possibility to integrate with ENS
- add interoperability with https://ipld.io
- add support for https://multiformats.io/multihash/


### Light clients

A light client might only be interested in the history or
integrity particular name and thus require some lightweight
mechanism for this, which is currently not possible.


### Fee lottery

It was suggested that the fees for the `.aet` namespace could
be distributed to random accounts via a lottery.


## References

[1] Kalodner, Harry A., et al. "An Empirical Study of Namecoin and Lessons for Decentralized Namespace Design." WEIS. 2015.

[2] Ali, Muneeb, et al. "Blockstack: A Global Naming and Storage System Secured by Blockchains." USENIX Annual Technical Conference. 2016.



