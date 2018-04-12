# Sync

The most basic building block of any blockchain is a ledger to keep track of
state transitions. If all we care about is keeping this ledger on our local
machine, then there's not much more we have to do, but things tend to be more
interesting whenever there are more parties involved. As soon as there are
multiple parties involved, a distributed ledger is needed, which requires us to
communicate with others and exchange information about state transitions in
order to synchronise their local state machines.

This document describes how a set of peers can exchange information about state
transitions in a settings where peers might not trust each other or could
possibly even be acting maliciously.

With that in mind, we're going to have to come up with a protocol that minimises
attack surface while not (significantly) hampering the speed with which
information is spread.

There are a couple of dimensions along which we can tune our protocol:

- network bandwidth usage
- network latency for transaction/block propagation
- reliability (in the presence of adversaries)
- memory/CPU usage

but as is almost always the case, we cannot have the best of all of them.

Ideally, our protocol has knobs which let users configure it to fit their needs,
e.g. a node running on a mobile phone might want to reduce bandwidth at the cost
of increased latency or on the other side of the spectrum a strong node might
elect to reduce latency by using more network bandwidth and increased CPU usage.


## Incentives

The incentives for nodes to share transactions and blocks with other nodes are
weak and there is a body of research suggesting that for Nakamoto style
consensus it might even be in a miners' interest to not share new blocks right
away. [1][2] These shortcomings also incentivise centralisation of mining power,
which is something we would like to avoid.

Another example could a mining pool, which wants to receive information about
new blocks and transactions as fast as possible and thus might forego thoroughly
checking blocks for validity to reduce latency. This is clearly not in the
interest of the network.

(***TODO***: Come up with something similar to/based on TorCoin, or at least
mention it and give outlook for how it might be integrated.)

## Transport protocol

This initial version is going to have nodes using TCP connections. All
communication will be encrypted and authenticated to ensure both confidentiality
and integrity, which prevents adversaries from interfering with the protocol
and de-anonymisation of nodes to a degree.

For encryption and authentication we are going to use the [Noise
protocol](https://noiseprotocol.org/), with the exact protocol name being
`Noise_XK_25519_ChaChaPoly_Blake2b`, i.e. `XK` for handshakes, DH over
`Curve25519`, `ChaChaPoly` for symmetric encryption and the `Blake2b` hash
function. `XK` as a handshake pattern means that the initiator of the handshake
sends their static key to the responder and the initiator knows the static key
of the responder.

Each node is having a `Curve25519` key pair for P2P communication. The peer
discovery is bootstrapped by having a set of Aeternity peer addresses in the
node configuration and the node tries to connect to these peers after starting
up the node. Peer addresses looks like:
`aenode://pp$ttZZwTS2nzxg7pnEeFMWeRCfdvdxeRu6SgVyeALZX3LbdeiWS@31.13.249.0:3015`.


(***TODO***: Spell out the full protocol including key schedule etc.)



## Connections

```                  [open]
+--------------+ -----------> +--------------+
| Disconnected |              |   Requested  |
+--------------+ <----------- +--------------+
       ^          [reject]/          |
       |            [timeout]        | [accept]
       |                             |
       |                             v
       |                      +--------------+
       +--------------------- |   Accepted   |
           [disconnect]/      +--------------+
             [timeout]               |
                                     |
                                     |
                                     v
                              +--------------+
                              |
```


different connection pools

incoming vs. outgoing connections

## Block/Tx protocol


- announce new tx/block to peers
- peer asks for data if they don't have it
- don't have to send full block with all tx

- send header first

- if peer sends garbage they get penalty and after x they get disconnected



### Proof of work puzzle

The first message a connecting node needs to sent after establishing the secure
session is send its proof of work puzzle solution.

- this could either be interactive
	1. initiator connects to node
	2. responder sends challenge
	3. initiator disconnects
	4. initiator computes solution
	5. initiator connects again and provides solution
- or done offline
	- this might require a consensus value otherwise nodes wouldn't know what to
    expect

Problems could arise if an overly difficult pow puzzle is required by most nodes
because it might prevent the majority of people from running nodes and hurt the
health of the network.

```
A                      B
|---    pow_puzzle   -->|
|                       |
|                       |
|                       |
|                       |
|                       |
|                       |
|                       |
```


### Reputation

The sync protocol uses a very simple reputation system for peers, which will
only be used to punish peers sending garbage or misbehaving. Reputation is local
to a node and not shared with anyone.
Once an offending node reaches some threshold, e.g. 0, the offended node MAY
terminate the connection and SHOULD reject any further connection attempts by
the offender for a while, e.g. 24 hours.

Garbage in this content would be:

- invalid blocks
- invalid transactions
- ...

If the offender is motivated and willing to bring up more nodes, then the node
under attack MAY reduce the number of slots for connections that don't require
the solution to a proof of work puzzle.


## Configurables

- pow target
- pow wait timeout
- (listener interface, port)
- connection timeout
- #overall connections
- #incoming connections
- gossip pool size
- peers -> (blacklist, whitelist)

## Threat Model

Any threat model comes with a set of assumptions and attack vectors that are out
of scope.

The first assumption is, that our distributed ledger is a blockchain using Nakamoto style consensus with proof of work for leader election, with any
malicious miner not possessing more than 25% of the mining power of the network.
This guarantees the basic integrity of our ledger.
(***TODO***: Properly address selfish mining et al)

The protocol described here is not used to transmit any secrets, such as cryptographic keys controlling coins, but does make use of cryptographic keys
itself. For an adversary to get ahold of these means that they would be able to
initiate the protocol with a node using them. Given that the protocol is only
used to transmit public information and generating new keys is easy, this should
only be a minor inconvenience.
(***TODO***: This changes if we use them for authentication as well)

We do not consider any physical threats to nodes participating in the protocol,
under the above assumption and because it is generally considered to be a very
hard problem, trying to design protocols, which can deal with compromised endpoints[4]. Usage of secure enclaves and other special purpose hardware can be
considered for mitigation but will not be discussed here.

That is, we operate under the "Internet Threat Model" as outlined in Section 3
of RFC3552[4]:

> In general, we assume that the end-systems engaging in a protocol
> exchange have not themselves been compromised.  Protecting against an
> attack when one of the end-systems has been compromised is
> extraordinarily difficult.  It is, however, possible to design
> protocols which minimize the extent of the damage done under these
> circumstances.

> By contrast, we assume that the attacker has nearly complete control
> of the communications channel over which the end-systems communicate.
> This means that the attacker can read any PDU (Protocol Data Unit) on
> the network and undetectably remove, change, or inject forged packets
> onto the wire.  This includes being able to generate packets that
> appear to be from a trusted machine.  Thus, even if the end-system
> with which you wish to communicate is itself secure, the Internet
> environment provides no assurance that packets which claim to be from
> that system in fact are.

We restrict this model even further and exclude TCP and IP level (distributed)
denial of service attacks, e.g. SYN floods or any sort of amplification attacks.

### Transport

Transport messages are encrypted and authenticated using the Noise protocol. For
an in-depth discussion of the Noise protocol and its security guarantees, please
refer to the [documentation](https://noiseprotocol.org/noise.html), specifically
sections [7](https://noiseprotocol.org/noise.html#handshake-patterns) and
[14](https://noiseprotocol.org/noise.html#security-considerations).
Using encryption and authentication covers man-in-the-middle attacks, eavesdropping,


A Denial of Service (DoS) attack can be mounted at different layers, e.g. at the protocol or the node level.
- slowing down block propagation
	- incr. risk of forks
	- makes selfish mining even more profitable
- resource exhaustion for single node by using up all connections/filling up
  RAM

Security:

- eclipse attack -> accepting double spends

Privacy:

- anyone in the same network can basically see everything you do without encryption


Distributed Denial of Service (DDoS) attacks are out of scope given that these
are usually executed at layer lower that we are concerned with, although it
could be argued that using mix networks hide the IP addresses of parties
communicating and thus might mitigate one DDoS angle.




### Resource exhaustion


### Eclipse Attacks

Whenever an adversary manages to surround an honest node with adversarial nodes
then we speak of an eclipse attack.

In order to prevent malicious parties from flooding the network with requests
and potentially eclipse new nodes, we will require nodes to attach the
solution to a proof of work puzzle whenever they try to initiate a connection
to another node. This solution


### Privacy

## References

[1]: Eyal, Ittay, and Emin Gün Sirer. "Majority is not enough: Bitcoin mining is vulnerable." International conference on financial cryptography and data security. Springer, Berlin, Heidelberg, 2014.

[2]: Nayak, Kartik, et al. "Stubborn mining: Generalizing selfish mining and combining with an eclipse attack." Security and Privacy (EuroS&P), 2016 IEEE European Symposium on. IEEE, 2016.

[3]: Ghosh, Mainak, et al. A TorPath to TorCoin: proof-of-bandwidth altcoins for compensating relays. NAVAL RESEARCH LAB WASHINGTON DC, 2014.

[4]: Rescorla, E., and B. Korver. "RFC 3552: Guidelines for writing RFC text on security considerations." Internet Society Req. for Comm (2003).
