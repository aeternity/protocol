# Gossip

As explained in the [Sync](SYNC.md) document, any blockchain implementation
needs communication with peers in order to be truly useful. Apart from the lower
level details described in that document, there is the added dimension of
how peers are selected for communication, how connections to those peers are
maintained over time. This is the purpose of gossiping functionality.

## Initial Configuration

The initial set of peers is defined by configuration when starting the node.
This is a predefined set of peers that are automatically connected to upon
startup.

## Peers

A peer is identified by a URI consisting of the protocol 'aenode://', the public
key, an '@' character, the hostname or IP number, a ':' character and the Noise
port number the node is using. If the address contains a hostname, it will be
resolved to an IP. Example:

'''
aenode://pp$HryRGHJ7Ct3trkktVyVBgfhHL1J4EYSD9cScuMZDV61eSHrCZ@mynode.example.com:3015
'''

A node is uniquely identified by the triplet of public key, IP and port.
This means one IP can have several instanced of Epoch started at the same
time listening on different ports. In the case of several unique public keys for
the same IP and port, only one can work. This will be the public key
corresponding to the private key that is used for the Noise protocol listener
associated with the hostname and port.

Apart from being used in encryption via the Noise protocol, the public key is
also used to determine which node should keep its initiated connection open in
case two connections are opened (see [Gossiping of New Peers](#gossiping-of-new-
peers)).

### Gossiping of New Peers

Whenever a ping message is exchanged between peers, either a ping request or
ping response, the peers also attach a subset of neighboring peers they know of.
The node that generates the message populates the neighbor list with 30 peers
that are randomly selected from its pool of verified peers (see
[Peers Maintenance](#peers-maintenance)).

When a ping request is received from another peer, that peer is first checked
for acceptance. This includes verifying

1. It is not the local node itself
2. The peer is not on the blocked list
3. It doesn't already have an existing connection

(3) refers to the case where two peers have learned about each other separately
and are both trying to initiate a connection. The connections are both initiated
via Noise, but once they are connected each node checks if they already have a
connection to that same peer. If they do, they will keep it if their public key
is larger than their peers, and drop it if not. This ordering of keys is
arbitrary but achieves the effect of only ever being true at one node or the
other. Thus, only one connection is kept.

Once the peer is accepted, all the neighbors not already verified are added to
the unverified pool. If the ping comes from an incoming connection from an
unverified peer, the peer itself is added to the unverified pool too (see
[Peers Maintenance](#peers-maintenance) for more details).

When the gossip ping is received and responded to, the connection will be closed
if any of the following conditions are met:

* The connecting peer is not a verified peer yet (see [Concerns](#concerns)).
* The maximum number of concurrent connections has been reached.

### Peers Maintenance

The objectives of peer maintenance are:

1. Prevent peer poisoning (Sybil/eclipse attack)
2. Limit the number of active peer connections
3. (Optionally) cache the known peers between restart

To prevent an attacker from poisoning the list of peers, isolating the
node from the rest of the network, we make it impossible to predict
the set of peer's IP/port the attacker should control to fill enough of the list
for the attack to be statistically successful. In addition we randomize the
peer eviction to prevent an attacker from predicting it and replace all good
peers for there own compromised ones.

This is achieved by first categorizing peers in two pools:

1. The unverified pool contains all the peers received through gossip.
It ensures no Byzantine node can fill it completely by limiting the subset
of the pool it can affect; it prevents attackers from predicting the set of
IP/port they must use to successfully eclipse the node.

2. The verified pool contains the peers the node connected to explicitly after
passing through the filter of the unverified pool. It randomizes the peer
distribution to the eye of attackers, preventing them from predicting the
eviction algorithm.

Peers are considered verified when the node has been able to connect to
them using the Noise protocol. Incoming connections are still serviced for
gossip but are not considered verified to prevent an attacker from circumventing
the algorithm by connecting directly to the attacked node.

Both pools clusterized peers into multiple buckets; they select which one
an added peer belongs to based on a combination of the address of the node the
information is coming from, the address of the peer to be added and a secret
generated by the node for the purpose of randomizing the selection process.
See [Unverified Pool](#unverified-pool) and [Verified Pool](#verified-pool) for
more details on how the peers are added to the pools.

The peers received from configuration are added directly to the verified pool
and are marked as "trusted", meaning that they will never get downgraded to the
unverified pool even if the node cannot connect to them.

When started, the node will iteratively pick a random peer from the verified
pool and try connecting to it. If there are no more peers available in the
verified pool, a random one is picked from the unverified pool. If the
connection succeeds, an unverified peer is upgraded to the verified pool and
removed from the unverified pool. If the connection fails, the peer retry
counter and last retry time are updated. The node keeps picking peers and
connecting until the maximum number of concurrent connections is reached.

The peer retry counter and last retry time (initialized to `0` and `infinity`),
are used to filter out peers when picking them from the pools providing
exponential backoff. After N failed attempts, a verified peer that is not
marked as trusted is downgraded to the unverified pool and the counter and time
is reset; unverified peers are simply removed.

Connected peers will periodically be pinged, and their connection state
monitored. The ping interval is configurable and defaults to once every 120
seconds. If a ping fails, this is logged and the peer is scheduled for another
ping in the normal interval.

#### General Peer Status

Regardless of the peer already being in a pool or not, some information
about it is updated when it is received through the gossip protocol:

- Last gossiped time:

  This is used to downgrade peers that have not been gossiped for a long time.

- (optional) The counter of the number of time it has been seen:

  Every time the peer is received through the gossip protocol, a time-based
  windowed counter is incremented. e.g. a counter per day for the last N days.

  This is used to estimate the duplication of the peer in the unverified pool
  to favor the frequently seen peers during selection. The duplication is
  bounded and decreases exponentially.

#### Unverified Pool

The unverified pool is composed of 1024 buckets of up to 64 peers, resulting in
a maximum capacity of 65536 peers.

To prevent a rogue node to fill it with compromised peers, it uses the address
of the node gossiping the peers to select a subset of the bucket; then the added
peer address is used to select the bucket it belongs to. A secret known only by
the node is used to randomize the selection process so it cannot be predicted
by the attacker.

If a peer is not already in the verified pool, the steps to add it to the
unverified pool are:

1. If already in the unverified pool, all references are first removed to
prevent uncontrolled duplications.
2. A subset of 64 buckets are selected based on the secret and the IP of the
node that gossiped the peer; this limits the part of the pool that can be
changed by any given rogue node IP.
3. From this subset, 16 buckets are selected based on the secret and the IP of
the peer to be added; this randomizes the peer distribution preventing the
prediction of the way peers will be evicted.
4. From these 16 buckets, 8 are selected based on the secret and the port of the
added peer; this reduces the collisions between peers that share the same IP.
5. (optional) In function of the frequency the peer has seen (See
[General Peer Status](#general-peer-status)) it is added to 1 up to 8 of these
buckets; this favor peers that were gossiped more frequently when picking a new
one to connect to and possible upgrade to the verified pool.
6. If the bucket the peer has to be added to is full, one existing peer has to
be evicted. This is done by first cleaning all the peers that weren't gossiped
for a certain amount of time, then if the bucket is still full, by selecting a
random peer with a bias favoring peers that were added the longest time ago.
7. The eventually evicted peer is completely removed from the pool.

Only the IP of the source node is used to select a subset of the pool because
IP is an expensive resource while ports are comparatively cheap.

See [Bucket Selection](#bucket-selection) for more details on how the buckets
are selected from the secret and other discriminators.

#### Verified Pool

The verified pool is composed of 256 buckets of up to 64 peers, resulting in a
maximum capacity of 16384 peers.

To prevent attackers from predicting how good peers are evicted and replace them
by compromised peers, the eviction is done per-bucket; the buckets are selected
from the peer address and a secret to randomize the selection process.

When a peer is verified the first time by connecting to it using the Noise
protocol (only outgoing connections), it is removed from the unverified pool
and the steps to add it to the verified pool are:

1. A subset of 16 buckets are selected based on the secret and the IP of the
peer to be added.
2. From this subset single bucket is selected based on the secret and the port
of the peer to be added; the IP and port are different discriminators to prevent
peers sharing the same port to affect the whole pool.
3. If the bucket is full, one peer has to be evicted. This is done by first
cleaning the peers that weren't gossiped for a long time, and if the bucket is
still full, by selecting a random one with a bias toward the ones that are not
connected and the last connection was the longest time ago. Trusted peers are
never evicted.
4. The eventually evicted peer is added to the unverified pool; its retry
counter and last retry time are reset. If the node is connected to the evicted
peer, the connection is closed.

See [Bucket Selection](#bucket-selection) for more details on how the buckets
are selected from the secret and other discriminators.

#### Technical Details (WIP)

##### Constants

Feedback on the constant selection?

##### Bucket Selection

The selection of a subset from a list of buckets could be done in various
ways. The current idea is to hash the secret combined with the discriminator and
extract groups of bits from the resulting hash as indexes in the list.

I am not sure of cryptographic validity of this solution; this probably needs
a bit more research.

##### (optional) Peer Duplication in Unverified Pool

The duplication of peers in the unverified pool to favor selection of frequently
seen peers is marked as optional because I am not sure it is worth doing.

#### Known limitations

With the current constants:

- The maximum cumulated number of peers in the pools is from 24576 to 81920
depending on peer duplication in the unverified pool.
- The maximum number of connected peers is 16384; it will probably be lower due
to the clusterization and eviction algorithm.
- The maximum number of peers that can be added through gossip by peers sharing
the same IP is from 512 to 4016 depending on peer duplication in the unverified
pool.
- The maximum number of neighboring peers sharing the same IP a single node
can add through gossip is from 128 to 1024 depending on peer duplication in the
unverified pool.

#### Concerns (WIP)

- There is always a cost for updating an unverified gossiped peer:

  If a peer is not in the verified pool BUT already was in the unverified pool,
  it is always removed first and then added again using the information of
  the gossiping source to select the new buckets it belongs to.

- Ensure that with a bounded number of connections the cluster can be larger
than the maximum number of connection per node:

  The verified pool distribute and evict peers based on a secret different
  on each node; that should randomize the set of peers the node will connect to
  allowing nodes to form a mesh network.

- Ensure a new node can join a network where all existing nodes may have reach
there maximum number of connections.

  Open question...

#### Persistence

Persistence of the known peers is important in preventing Sybil/eclipse attacks.

If the node rebuild its list of peers from scratch every time it is restarted,
an attacker could use any other attack vector to crash the node or wait for
a scheduled restart and be the first to spam it with compromised addresses.

To support persistence, the verified pool or both pools could be dumped to disk
at regular intervals alongside the secret used for the bucket selection.
