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

Names are part of a namespace, which works just like DNS, e.g. `mywallet.test`
or `привет.test` are part of the same `.test` namespace.


## Governance

Lima hard fork is introducing final `.chain` registration namespace.
It also retires `.test` namespace.
We will also not include mechanisms similar to the `sunrise` and `landrush`
periods, which are common for DNS, where registration is restricted to small
select groups and trademark holders in order to avoid name squatting, before
the general public can start claiming names.


## Mechanisms

It is unclear what a good mechanism for a naming system would look
like. If we imagine two actors both being interested in the same name,
what would a »fair« solution be to resolve this?

Fees are the main mechanism to discourage spam and squatting.
We lock the governance fee in an account without private key access.
Starting out with [locking](consensus/locking.md) could allow us an easier
path for future update to the fee structures, as it doesn't involve miners.

Every entry in the `.test` namespace pays the same amount of fees.
After Lima `.test` namespace is no longer available to claim.
Entries in `.chain` namespace are differentiated regarding fees by their length.

The new mechanism planted in Lima hard fork introduces auctions.
We make auction parameters depend on name length.

An auction starts when a valid claim transaction following preclaim transaction
has auction triggering parameter. Currently auction starts when revealed name
is 12 characters or shorter.

For the names subject to auction, a claim transaction is an attempt of a name claim.
It can be followed by another claim from an account different than one set in
preclaim for given name.

For names longer than 12 characters, a claim transaction sets ownership of a name.

There is finite amount of time when the follow up claim in an auction is allowed.
This time is expressed in height delta computed from function of length of the name.

The function will return higher value for shorter names. In practice it means
that the shorter the name, the longer another claim transaction is valid.
We are starting with extremely long time that makes claim for short name final.
It will protect attractive names until this functionality is exposed to larger audience.

Claim transaction becomes a bid in an auction.

Furthermore, the initial fee for name is a value of the function of
the name's length. It is decreasing function: for shorter names have higher initial
fee.

Also bidding by claim transaction is constrained by price progression.
Each next bid has to be higher by `X` tokens, determined by percent of the price
defined in governance.

All, functions, base fee, free length value and price progression may be subject
to changes with governance mechanism. Non-bidding path of the name claim is purposed
for development or testing.

Each entry has a fixed expiration date on claim after which the entry should
transition into the `revoked` state. Once it reaches this state, the name
will be released, i.e. transition into the `unclaimed` state, after which
it could be claimed again.

To prevent the entry from expiring a user can, at any point before reaching
the expiration date, update the entry, which pushes the expiration date
into the future by the time delta of the registration time and the update time,
e.g. if a user posts an update one week after claiming their name, the expiration
date gets pushed one week further into the future. The main motivation of this
expiration date is to prevent situations where the private keys, which control
the name, are lost, making the name unusable as well.


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
points towards.
This can have multiple entries, e.g. a payment address associated
with the name and an oracle address associated with the name.


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

***Note:*** For this first draft names MUST `.test` as a suffix, i.e. `mywallet.test`.


### Namespaces/Labels

A name is split up into labels by the `FULL STOP (U+002E .)` character.
These labels will also be referred to as namespaces, e.g. `mywallet.test`
can be understood as the `mywallet` namespace in the `chain` namespace.

Any label that is not at the top level, e.g. `chain`, MUST be longer than
three characters.

Labels SHOULD be at most 63 characters long and the full path
of all names and namespaces SHOULD be at most 253 characters
long, in order to enable interoperability with DNS.


### Registrars

A registrar controls who is allowed to claim names in their namespace
and under what circumstances they are allowed to do so.

The only available registrars up to Lima version will be hard-coded
ones, which own the `.` and `.test` namespaces.

From Lima we will support `.chain` and limit `.test` namespace.
`.test` names will expire without an option of updating TTL.
We will use expiration mechanism to purge `.test` names.

The `.` namespace registrar is restricted and MUST NOT allow anyone to
claim any names in its namespace.

The `.test` namespace registrar allows users to claim any name that is
valid according to the validation rules if the name is currently not
claimed and they pay the appropriate fee.


### Commitment Scheme

Claiming a name requires a commitment scheme, which enables the claimant
to commit to a name and after the commitment has been accepted into the
chain, reveal the name to finish the process.

A commitment should be binding, i.e. the claimant cannot change
the value they commited to without changing the actual commitment
and hiding, so that a malicious miner learns nothing about the value
the claimant has commited until they chose to reveal that value. This
prevents malicious miners from front running, i.e. upon seeing a
claim transaction, including their own claim request for the same
name instead of the original claimant's one.

After the claim transaction the aens protocol is carried in clear text,
in order to support auctions.


### Hashing

Names are generally only referred to in hashed form.

#### Until Lima hardfork
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

#### From Lima hardfork

From Lima we don't use `NameHash` anymore. Instead, it is a 32 byte Blake2b hash
of the IDNA encoded UTF-8 name.


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
pre-claimed|auction ---> claimed
         | ^    <timeout>  | ^
         | |               | |
          -                 -
        claim            update
```

The pointers field in the name entry:
* On `claim` transaction, is initialized to the empty dictionary.
* On `update` transaction, is replaced with the pointers in the transaction, keeping the order in the transaction.

Note that `expire` is not an explicit message that is part
of the protocol.


### Protocol fees and protection times

Here is the function of initial bidding price depending on name length for Lima hardfork.

```
 ------------- -------------
| name length | initial fee (unit 10^14) |
 ------------- -------------
| 31          | 3           |
 ------------- -------------
| 30          | 5           |
 ------------- -------------
| 29          | 8           |
 ------------- -------------
| 28          | 13          |
 ------------- -------------
| 27          | 21          |
 ------------- -------------
| 26          | 34          |
 ------------- -------------
| 25          | 55          |
 ------------- -------------
| 24          | 89          |
 ------------- -------------
| 23          | 144         |
 ------------- -------------
| 22          | 233         |
 ------------- -------------
| 21          | 377         |
 ------------- -------------
| 20          | 610         |
 ------------- -------------
| 19          | 987         |
 ------------- -------------
| 18          | 1597        |
 ------------- -------------
| 17          | 2584        |
 ------------- -------------
| 16          | 4181        |
 ------------- -------------
| 15          | 6765        |
 ------------- -------------
| 14          | 10946       |
 ------------- -------------
| 13          | 17711       |
 ------------- -------------
| 12          | 28657       |
 ------------- -------------
| 11          | 46368       |
 ------------- -------------
| 10          | 75025       |
 ------------- -------------
| 9           | 121393      |
 ------------- -------------
| 8           | 196418      |
 ------------- -------------
| 7           | 317811      |
 ------------- -------------
| 6           | 514229      |
 ------------- -------------
| 5           | 832040      |
 ------------- -------------
| 4           | 1346269     |
 ------------- -------------
| 3           | 2178309     |
 ------------- -------------
| 2           | 3524578     |
 ------------- -------------
| 1           | 5702887     |
 ------------- -------------
```

Here is the function of timeout required to close the auction.
It depends on name length. Timeout is expressed in blocks.
Non zero value means that there must be no follow up claim for
the number of blocks defined here.

```
 ------------- -------------
| name length | time out    |
 ------------- -------------
| 13+         | 0           |
 ------------- -------------
| 9-12        | 480         |
 ------------- -------------
| 5-8         | 14880       |
 ------------- -------------
| 1-4         | 29760       |
 ------------- -------------
```


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
| name_salt      | 32 |
 ---------------- ----|
| name_fee       | 32 |
 ---------------- ----
```

Flow for a user:

1. (optional) wait `n` blocks, s.t. that the block including the `pre-claim` cannot be reversed whp
2. send `claim` transaction to reveal name and pay the associated fee
3. (Lima) send follow up `claim` transaction as overbid to initial `claim`

From Lima transaction version is `2`.

The first `claim` after `pre-claim` transaction MUST be signed by the same private key as a
`pre-claim` transaction containing a commitment to the name and nonce.

If the time delta of `pre-claim` and `claim` is bigger than 300 blocks,
then the `claim` MUST be rejected.

If the time delta of subsequent `claim` is bigger than governance defined values
then this `claim` MUST be rejected.

If the `name_fee` doesn't meet governance requirements it MUST be rejected.

From Lima hardfork, the subsequent `claim` that takes part in auction MUST have `name_salt`
equal to `0`

From Lima hardfork only the first `claim` transaction MUST be signed by
the same private key as a `pre-claim` transaction containing a commitment to the name and nonce.

A `claim` transaction MUST NOT be in included in the same block as its
`pre-claim`.

The `claim` transaction, apart from standard transaction fee,
locks additional fee in a restricted account (account with no private key access).
See also [mechanisms section](#mechanisms).


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

The `expire_by` MUST NOT be more than 50000 blocks into
the future.

`update` transaction may be used to extend the lease of the name.
We do not require an additional fee for extending the lease.

The `pointers` field SHOULD NOT contain multiple entries with the same key.
The `pointers` can point to one of: account address, oracle id,
channel id or contract id.

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

Since we don't have an auction protocol at launch, we could hold
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
`unicorn.kitty.test` and then transfering that name to the person, who
adopts the cat. The authorization policies for these will need some
flexibility seeing as the owner of a namespace might want to prevent
or allow users creating sub-sub-labels, e.g. the owner of `unicorn.kitty.test`
creating `rarest.`unicorn.kitty.test`.


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
registrars themselves, i.e. if I own `mywallet.chain`, I can
then allow others to register `name.mywallet.chain`.

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

It was suggested that the fees for the `.chain` namespace could
be distributed to random accounts via a lottery.


## References

[1] Kalodner, Harry A., et al. "An Empirical Study of Namecoin and Lessons for Decentralized Namespace Design." WEIS. 2015.

[2] Ali, Muneeb, et al. "Blockstack: A Global Naming and Storage System Secured by Blockchains." USENIX Annual Technical Conference. 2016.
