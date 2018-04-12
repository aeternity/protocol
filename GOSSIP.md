# Gossip

As explained in the [Sync](SYNC.md) document, any blockchain implementation
needs communication with peers in order to be truly useful. Apart from the lower
level details described in that document, there is the additional dimension of
how peers are selected for communication, how connections to those peers are
maintained over time. This is the purpose of gossiping functionality.

## Initial Configuration

The initial set of peers is defined from configuration when starting the node.
This is a predefined set of peers that are automatically connected to upon
startup.

## Peers

A peer is identified by a URI consisting of the protocol `aenode://`, the public
key, an `@` character, the hostname or IP number, a `:` character and the Noise
port number the node is using. Example:

```
aenode://pp$HryRGHJ7Ct3trkktVyVBgfhHL1J4EYSD9cScuMZDV61eSHrCZ@mynode.example.com:3015
```

A node is uniquely identified by the triplet of public key, hostname and port.
This means one hostname can have several instanced of Epoch started at the same
time listening on different ports. In the case of several unique public keys for
the same hostname and port, only one can work. This will be the public key
corresponding to the private key that is used for the Noise protocol listener
associated with the hostname and port.

Apart from being used in encryption via the Noise protocol, the public key is
also used to determine which node should keep its initiated connection open in
case two connections are opened (see [Gossiping of New Peers](#gossiping-of-new-
peers)).

### Maintenance of Existing Peers

An added peer is connected to using the Noise protocol. If the connection fails,
the connection attempt is retried with an increasing time interval between
attempts (up to 10 minutes). After seven attempts, the peer is removed. If the
peer is a predefined peer, it is never removed.

Known connected peers will periodically be pinged, and their connection state
monitored. The ping interval is configurable, and defaults to once every 120
seconds. If a ping fails, this is logged and the peer is scheduled for another
ping in the normal interval.

Once added to the list of known connected peers, a peer is never removed.

### Gossiping of New Peers

Whenever a ping message is exchanged between peers, either a ping request or
ping response, the peers also attach a subset of neighboring peers they know of.
The node that generates the message populates the neighbor list with 30 peers
that are randomly selected from the list of known and connected peers.

When a ping request is received from another peer, that peer is first checked
for acceptance. This includes verifying

1. It is not the local node itself
2. The peer is not in the block list
3. It doesn't already have an existing connection

(3) refers to the case where two peers have learned about each other separately
and are both trying to initiate a connection. The connections are both initiated
via Noise, but once they are connected each node checks if they already have a
connection to that same peer. If they do, they will keep it if their public key
is larger than their peers, and drop it if not. This ordering of keys is
arbitrary, but achieves the effect of only ever being true at one node or the
other. Thus, only one connection is kept.

Once the peer itself is accepted, all the neighbors are added to the known
peers of the current node. They will then be pinged just as any other known
peer.

There is no maximum limit to the number of peers that can be connected in a
node.
