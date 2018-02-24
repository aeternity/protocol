# Nodes

(can we do this without leaking meta-data for clients?)

```
               untrusted
light client <-----------> full node
                  n:n
```

```
       trusted
user <---------> local full node
         1:1
```

```
       trusted
user <---------> remote full node
         1:1
```

```
       trusted
user <---------> remote full node
         n:1
```


## Peer discovery

### Kademelia

Kademelia is a well studied and fairly robust peer to peer system, which
uses the UDP protocol for its messages.

Switching TCP for UDP eliviates the problem of having many stuck/zombie
TCP connections for unresponsive nodes, although malicious nodes could
still advertise via UDP and then refuse a TCP connection.

For the full description of the protocol see [Kademlia: A Peer-to-peer information system based on the XOR Metric](http://pdos.csail.mit.edu/~petar/papers/maymounkov-kademlia-lncs.pdf).

#### Identities

Nodes in the original paper have a random, although they don't have to be random,
160 bit ID.

In our case, this ID should be a 32 byte public key, which the node uses to encrypt
its communication.

#### Distance metric

To cluster nodes and compute distance between nodes, Kademelia uses its XOR metric,
which is `d(x, y) = x ^ y`, with `^` being xor. Please see the original paper for
an explanation as to why this metric captures distances between two 160 bit numbers.

We change the distance metric to be `d(x, y) = blake2b(x) ^ blake2b(y)`, `x` and `y`
being the public keys.

#### Variables

A number of variables are used throuhout the protocol to fine-tune its behaviour:

- bucket size `k`, e.g. 16
- concurrency of `FIND_NODE` requests `alpha`, e.g. 3
- routing table size `b`, e.g. 5

- bucket refresh every 3600 seconds
- timeout 300ms

#### Messages

The Kademelia protocol has four different kinds of messages:

- PING - check online status of a node
- STORE - instruct a node to store <k,v> pair
- FIND_NODE - returns k closests nodes
- FIND_VALUE - either returns the same as `FIND_NODE` or a value if it was `STORE`d before

Since we are not interested, at least not right now, in the Key-Value store,
the `STORE` and `FIND_VALUE` messages can either be ignored or just be used
to store empty strings.


#### Eclipse Attack

Whenever an adversary manages to surround an honest node with adverserial nodes
then we speak of eclipse attacks.

This attack is already sort of prevented by the `k` bucketing approach, since
buckets are spread out accross distances of `2^i` and each bucket contains at
most `k` entries. Additionally, buckets are filled once and then only touched
whenever a node disappears. Thus an attacker has to either target nodes, that
are new to the network or has to somehow partition the network via DDoS or BGP
based attacks.

To increase the difficulty of this attack, it should be unfeasible for nodes
to just arbitrarily choose their own IDs.

In order to prevent malicious parties from flooding the network with request
and potentially eclipse new nodes, we could also require nodes to attach the
solution to a Proof-Of-Work puzzle.

### Reputation

***TODO***

- requires better identities
- trade-off between computation/monitoring and enforcement
- PoW ID should have higher priority
- nodes sending invaliv transactions get added to grey list
- after repeated offense, get black listed and then removed
  from known nodes s.t. they don't get propagated
- local/global reputation vectors based on: Sabater, Jordi, and Carles Sierra. "Regret: A reputation model for gregarious societies." Fourth workshop on deception fraud and trust in agent societies. Vol. 70. 2001.


### Extensions


### Identities

We currently have no notion of identities other than a tuple of
`(IP address, port)`. Ideally, this would be `(IP address, port, id)`
instead, where the is some sort of cryptographic identifier, e.g.
a public key.

### Misc


- currently there's no limit to the number of peers we accept


### Todo

- potentially add downlists (Improving the Performance and Robustness of Kademlia-based Overlay Networks)[]
- bloom filters for transactions/mempool
- don't send full mempool at once

## Syncing

## Full nodes

The full nodes are the backbone of our network. It is them, who
broadcast transactions and verify them. One of our goals should
be to have as many of them as possible.

The majority of full nodes will most likely be provided by dApp
developers in order to ensure that their users have access to
AEternity network.

As such, the default mode of operation for nodes should be to
expose APIs, which are "safe", i.e. they don't expose any
methods that would let a remote user:

- use its keys for signing
- retrieve keys
- create accounts
- (***TODO*** exhaustive list)

## Light nodes

While full nodes receive everything, a light node will only want
to track a subset of the overall activity on chain, e.g. only
transactions related to accounts its operator manages.

Light nodes are still part of the peer to peer network and as such,
the peer to peer synchronization protocol should offer mechanisms
to support these light nodes:

- let peers specify filters for transactions they want to have
  relayed to them (or have headers include filters so peers can
  check themselves)
- (***TODO*** exhaustive list)

### Motivation

Having light nodes is essential giving our focus on state channels,
since the vast majority of users are not going to be able to run full
nodes but still have the same requirement to watch the chain for
transactions related to their open channels, e.g. to catch a cheating
peer trying to publish outdated state.

### Syncing

A light node should start by requesting all block headers from its
peers.


## Light wallets

- might be synonymous with light node or just be light node + wallet
  functionality
- might not be part of p2p network

## Light * prerequisites

- request headers from peer
- filter peer data

## APIs


## Users

We want to enable users to have full control over their funds while
still protecting them from theft and loss.

Ideally we'd like to encourage and enable as many users as possible
to run validating nodes plus manage their own keys, all in the spirit
of "be your own bank."


## Key management


## Encryption

Encryption is vital to fend off all sorts of network level attacks
and guarantuee a base level of privacy.

OpenSSL supports a lot of features we have no need for, at
least for the peer to peer network. A better approach would be
a [Noise Protocol](http://noiseprotocol.org) based solution.

Curve25519-ChaChaPoly-1305

## Authentication

Public key encryption also gives us a rudimentary authorization
scheme, where nodes can restrict access based on public keys,
similar to how OpenSSH allows users to configure authorized keys.


## Threat model

### Full node

- exploit in network stack leaking keys
- exposing sensitive API endpoints via public interfaces

### Users

- phishing
