# Gossip

As explained in the [Sync](SYNC.md) document, any blockchain implementation needs
communication with peers in order to be truly useful. Apart from the lower level
details described in that document, there is the additional dimension of how
peers are selected for communication, how connections to those peers are
maintained over time. This is the purpose of gossiping functionality.

## Initial Configuration

The initial set of peers is defined from configuration when starting the node.
This is a predefined set of peers that are automatically connected to upon
startup.

## Maintenance of Existing Peers

An added peer is connected to using the Noise protocol. If the connection fails,
the connection attempt is retried with an increasing time interval between
attempts (up to 10 minutes). After seven attempts, the peer is removed. If the
peer is a predefined peer, it is never removed.

Known connected peers will periodically be pinged, and their connection state
monitored. The ping interval is configurable, and defaults to once every 120
seconds. If a ping fails, this is logged and the peer is scheduled for another
ping in the normal interval.

Once added to the list of known connected peers, a peer is never removed.

## Gossiping of New Peers

Whenever a ping message is exchanged between peers, either a ping request or
ping response, the peers also attach a subset of neighboring peers they know of.
The node that generates the message populates the neighbor list with 30 peers
that are randomly selected from the list of known and connected peers.

When a ping request is received from another peer, that peer is first checked
for acceptance. This includes verifying

1. It is not the local node itself
2. The peer is not in the block list
3. It doesn't already have an existing connection

Once the peer itself is accepted, all the neighbors are added to the known
peers of the current node. They will then be pinged just as any other known
peer.

There is no maximum limit to the number of peers that can be connected in a
node.
