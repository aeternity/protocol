# Nodes

This document will give an overview of the peer to peer network and how clients
are going to interact with the network.

```
            untrusted
full node <-----------> full node
               n:n
```

```
             untrusted
light node <-----------> full node
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

```

```


## Full nodes

The full nodes are the backbone of the network. It is them, who broadcast
transactions and verify them and one of our goals should be to have as many of
them as possible.

The majority of full nodes will most likely be provided by dApp developers in
order to ensure that their users have access to the network or by enthusiasts,
who want to secure the network.

As such, the default mode of operation for nodes should be to expose APIs, which
are "safe", i.e. they don't expose any methods that would let a remote user:

- use its keys for signing
- retrieve keys
- create accounts
- (***TODO*** exhaustive list)

(***TODO***: checkpoints + state pruning, maybe mention archive nodes)

## Light nodes

While full nodes receive everything, a light node will only want to track a
subset of the overall activity on chain, e.g. only transactions related to
accounts its operator manages. As such, a light node will have the same feature
set as a full node, e.g. be able to run contracts, verify blocks etc, but only
store a minimal amount of required data to do so. Instead of storing the state
locally, it uses the network as a distributed hash table, to request or look up
information.

Typically, light nodes will be ran in resource constrained environments, e.g.
mobile phones, embedded platforms, in browsers or slow networks. With that in
mind, we want to come up with a protocol, that allows these nodes to retain most
of the security guarantees of a full node, which verifies all transactions,
while requiring as little memory, CPU time and bandwidth as possible.

In order to keep track of the progress of the chain, a node will need to receive
at least all block headers. With this strategy, a node can verify that it
follows the correct, i.e. heaviest, chain but does rely on the full nodes to
verify that the transactions contained in a block are valid.
Just following block headers by itself is not worth all that much, what a user
actually cares about are transactions.

(***TODO***: MPT proofs of inclusion)

Light nodes are still part of the peer to peer network, therefore the peer to
peer synchronisation protocol should offer mechanisms to support these light
nodes.

- let peers specify filters for transactions they want to have relayed to them
	(or have headers include filters so peers can check themselves)



(***TODO***: figure out an incentive mechanism for full <-> light data sharing,
if at all possible. Can this be seen as trying to conserve a common good?)


### Motivation

Having light nodes is essential given our focus on state channels, since the
vast majority of users are not going to be able to run full nodes but still have
the same requirement to watch the chain for transactions related to their open
channels, e.g. to catch a cheating peer trying to publish outdated state.


## Wallets

A wallet is usually understood to be a piece of software controlled by a user,
that lets them control one or more accounts and interact with the blockchain.
The term is fairly ambiguous since any full or light node would fit the above
description.
In order to make the distinction meaningful, we're going to introduce further
constraints for wallets.

- might be synonymous with light node or just be light node + wallet
	functionality
- might not be part of p2p network

## Light * prerequisites

- request headers from peer
- filter peer data

## Peer discovery

### Kademlia

Kademlia is a well studied and fairly robust peer to peer system, which uses
the UDP protocol for its messages.

Switching TCP for UDP alleviates the problem of having many stuck/zombie TCP
connections for unresponsive nodes, although malicious nodes could still
advertise via UDP and then refuse a TCP connection or keep it half-open.

For the full description of the protocol see [Kademlia: A Peer-to-peer
information system based on the XOR Metric](http://pdos.csail.mit.edu/~petar/papers/maymounkov-kademlia-lncs.pdf).

#### Identities

Nodes in the original paper have a random, although they don't have to be
random, 160 bit ID.

In our case, this ID should be a 32 byte public key, which the node uses to
encrypt its communication with a given peer.
If a peer encrypts its messages with a key it has not advertised, then the
connection should be refused.

#### Distance metric

To cluster nodes and compute distance between nodes, Kademlia uses its XOR
metric, which is `d(x, y) = x ^ y`, with `^` being xor. Please see the original
paper for an explanation as to why this metric captures distances between two
160 bit numbers.

We change the distance metric to be `d(x, y) = blake2b(x) ^ blake2b(y)`, `x` and
`y` being the public keys.

#### Variables

A number of variables are used throughout the protocol to fine-tune its behaviour:

- bucket size `k`, e.g. 16
- concurrency of `FIND_NODE` requests `alpha`, e.g. 3
- routing table size `b`, e.g. 5

- bucket refresh every 3600 seconds
- timeout 300ms

#### Messages

The Kademlia protocol has four different kinds of messages:

- `PING` - check online status of a node
- `STORE` - instruct a node to store <k,v> pair
- `FIND_NODE` - returns k closest nodes
- `FIND_VALUE` - either returns the same as `FIND_NODE` or a value if it was `STORE`d before

Since we are not interested, at least not right now, in the Key-Value store,
the `STORE` and `FIND_VALUE` messages can either be ignored or just be used
to store empty strings.


#### Eclipse Attack

Whenever an adversary manages to surround an honest node with adversarial nodes
then we speak of eclipse attacks.

This attack is already sort of prevented by the `k` bucketing approach, since
buckets are spread out across distances of `2^i` and each bucket contains at
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
- nodes sending invalid transactions get added to grey list
- after repeated offence, get black listed and then removed
  from known nodes s.t. they don't get propagated
- local/global reputation vectors based on: Sabater, Jordi, and Carles Sierra. "Regret: A reputation model for gregarious societies." Fourth workshop on deception fraud and trust in agent societies. Vol. 70. 2001.


### Extensions


### Identities

We currently have no notion of identities other than a tuple of
`(IP address, port)`. Ideally, this would be `(IP address, port, id)` instead,
where the `id` some sort of cryptographic identifier, e.g. a public key.

### Misc

- currently there's no limit to the number of peers we accept


### Todo

- potentially add downlists (Improving the Performance and Robustness of Kademlia-based Overlay Networks)[]
- bloom filters for transactions/mempool
- don't send full mempool at once

## Syncing

### Full nodes

### Light nodes

A light node should start by requesting all block headers from its peers.

## APIs



## Users

We want to enable users to have full control over their funds while still
protecting them from theft and loss.

Ideally we'd like to encourage and enable as many users as possible to run
validating nodes plus manage their own keys, all in the spirit of "be your own
bank." Unfortunately, running such a full node will most likely require at least
some basic technical expertise and might even require more than commodity
hardware.


## Key management


## Encryption

Encryption is vital to fend off all sorts of network level attacks and guarantee
a base level of privacy.

OpenSSL comes with a lot of features we have no need for, at least for the peer
to peer network, therefore we are going to use a [Noise Protocol](http://noiseprotocol.org) based solution.

Curve25519-ChaChaPoly-1305

## Authentication

Public key encryption also gives us a rudimentary authorisation scheme, where
nodes can restrict access based on public keys, similar to how OpenSSH allows
users to configure authorised keys.


## Threat model

### Full node

- exploit in network stack leaking keys
- exposing sensitive API endpoints via public interfaces

### Users

- phishing
