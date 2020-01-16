# Virtual State Channels

## Abstract

The Aeternity blockchain provides various means for scaling the transaction
throughput so it can accommodate billions of people. One of those is State
Channels. This document describes how the State Channels protocol can be
further improved in order to build Virtual State Channels.

## Introduction

Aeternity blockchain already has two-party State Channels built on a protocol
level. They allow producing off-chain transactions. They allow not just
exchanging tokens off-chain but also executing smart contracts. That results
in them not consuming either `gas`, or `fee` for their execution. Off-chain
transactions also don't need on-chain confirmations so their speed is bound by
the involved parties' computing power and network bandwidth. This allows
building cheap near real-time protocols while keeping the same amount of
trustlessness the blockchain already provides.

While this is already a great improvement to traditional blockchain solutions,
participants are still expected to interact with the chain for certain
milestone events: opening a channel, depositing or withdrawing tokens and
closing a channel. As with any on-chain transactions, the higher number of
confirmations a transaction has, the better fork-safety it has. In the context
of State Channels that results in long waiting times whenever the participants
need to modify the on-chain. This is to be improved with the introduction of
Virtual State Channels.

Regular State Channels, also here referred to as on-chain State Channels, use
the blockchain both as a source of truth and as an arbiter in disputes.
Virtual State Channels build on top of them allowing to use a third party - an
intermediary - as a source of truth or as an arbiter. It is crucial that, as
with regular State Channels, Virtual State Channel participants can protect
themselves from malicious acts. Since third parties providing Virtual State
Channel infrastructure can also act maliciously, at any point of time a
participant can bring a potential dispute on-chain and have it resolved there.
That way we keep Virtual State Channels as trustless as State Channels
themselves.

## Channels within channels

On-chain State Channels have a state. It is represented as a MPTree and has
the same structure as the on-chain state tree. A notable difference between
those would be that the off-chain state tree is limited just to accounts and
contracts. It does not allow having names, oracles or channels and the
corresponding trees are empty. The proposed Virtual State Channels solution
allows having channel objects stored in the off-chain state. This requires a
corresponding dispute mechanism that protects all parties' interests and
allows them to dispute the off-chain channel on-chain.

The intention is that instead of opening a State Channel on-chain,
participants use an intermediary. Both participants must have an already
opened State Channel with the intermediary. This existing State Channel can be
either on-chain or a virtual one - for clarity, we would refer to it as a
parent State Channel. They open a Virtual State Channel within their parent
State Channel's context and continue using it as they would an on-chain State
Channel. Once opened, all off-chain Virtual State Channel communication goes
directly from one participant to the other. The intermediary receives Virtual
State Channel updates only when required to take some action.

With on-chain State Channels participants lock tokens in the channel itself. A
similar approach is taken with Virtual State Channels: since participants are
to create Virtual State Channel objects in the states of their parent State
Channels with the intermediary, they all need to lock tokens in the new
Virtual State Channel. They must lock the same amount of tokens in both parent
State Channel states. A participant is representing herself in the Virtual
State Channel and she locks as many tokens as she would like to. In the scope
of the parent State Channel, the intermediary protects the interests of the
other Virtual State Channel's participant and locks the corresponding amount
of tokens from their behalf. This happens in both parent State Channels. As a
result of this is the intermediary locks tokens in both parent State Channels
and has an exposure as the total amount of tokens locked in the Virtual State
Channel.

##### Example

```
                          +-------------+
                          |   Ingrid    |
                          |-------------|
                          |             |
                          |  off-chain  |
                +--------+|    state    |+--------+
                |         |    trees    |         |
                |         |             |         |
        on-chain|         +-------------+         |on-chain
         channel|                                 |channel
                |                                 |
                |                                 |
                |                                 |
                |                                 |
                |                                 |
 +-------------+|                                 |+-------------+
 |   Alice     |+                                 +|     Bob     |
 |-------------|                                   |-------------|
 |             |            virtual                |             |
 |  off-chain  |+---------------------------------+|  off-chain  |
 |    state    |            channel                |    state    |
 |    trees    |                                   |    trees    |
 |             |                                   |             |
 +-------------+                                   +-------------+
```

Alice and Bob don't have an on-chain State Channel between themselves and want
to open a Virtual State Channel. They both have on-chain State Channels with
Ingrid. Alice wants to deposit 3 tokens to the newly formed AliceBob Virtual
State Channel, Bob wants to deposit 2 tokens there. In the AliceIngrid parent
State Channel a new channel object is created having AliceBob `channel_id`.
Alice deposits 3 tokens in it and Ingrid deposits 2 from Bob's behalf. If at
any moment Alice tries cheating Bob, it would mean cheating Ingrid and Ingrid
has the incentive to protect Bob. Similarly, in BobIngrid parent State Channel
a channel object is created with same `channel_id` and balances, it is just
Bob locks his 2 tokens and Ingrid locks 3 for Alice. The same incentive
applies that if Bob is to cheat Alice, he has to cheat Ingrid as well and she
has the incentive to protect Alice. Ingrid's exposure of locked tokens is `2 +
3 = 5`.

### Virtual State Channel object

The channel on-chain object holds various channel-related data, including
participants, total balances dedicated to the channel etc. It has all the
required information to safely close the channel, even in cases of a dispute.

#### Object structure

In cases of Virtual State Channels we produce a regular State Channel object
and wrap it in an object holding some additional information. It consists of
who the intermediary is and the initial token amounts dedicated by the
participant and the intermediary. An important detail is that the initial
token amounts for the participants are not according to the amounts they've
dedicated: it is the intermediary that has all of the tokens and the Virtual
State Channel participant has none. This plays an important role and it is
described later on.

##### Example

For this example we will be using some pseudo-structures. Those do not
necessarily represent real serialization and play mostly a visualization role.

If an on-chain AliceBob State Channel would look like:

```javascript=
{
   "id": "ch_...", // the Alice-Bob channel ID
   "initiator_id": "ak_...", // the address of Alice
   "responder_id": "ak_...", // the address of Bob
   "initiator_amount": 3, // Alice balance
   "responder_amount": 2, // Bob balance
   "channel_amount": 5 // the sum of the two amounts

}
```

The Virtual Alice Bob State Channel object where Ingrid is an intermediary
would be:

```javascript=
{
   "intermediary_id": "ak_...", // Ingrid's address
   "intermediary_amount": 5, // initial distribution of total tokens, dedicated to Ingrid
   "requester_amount": 0, // initial distribution of total tokens, dedicated to Alice
   "channel" :
      {  
         "id": "ch_...", // the Alice-Bob channel ID
         "initiator_id": "ak_...", // the address of Alice
         "responder_id": "ak_...", // the address of Bob
         "initiator_amount": 3, // Alice balance
         "responder_amount": 2, // Bob balance
         "channel_amount": 5 // the sum of the two amounts
      }
}
```

#### Object updates

The Virtual State Channel object is persisted in the state of the
corresponding parent State Channels and can be updated by providing off-chain
transactions that belong to the Virtual State Channel. Similar rules apply as
with on-chain State Channels: newer state replaces old one. Off-chain updates
contain a number `round` describing the point of time when the update had been
made. Since it is ever-incrementing, two off-chain updates can be compared. If
two share the same `round` and one is co-authenticated and the other had been
produced by some unilateral action, the former takes precedence over the
latter.

Virtual State Channel participants create and co-authenticate desired updates
and provide them to the intermediary in the respective parent State Channels.
In order for them to be applied there, the intermediary must also agree that
those are valid updates. If the intermediary refuses to cooperate, most of
those can be forcibly progressed on-chain. All of those will be explained in
detail.

A special case arises when both Virtual State Channel participants agree on an
off-chain update and one of them provides it to the intermediary while the
other does not. Since Channel state can only be updated with a mutual
agreement, it is up to the intermediary to decide how to proceede further. One
could reject the cooperating participants' update or treat the non-cooperating
one as a violation of the protocol and to bring it on-chain as a dispute.
Proposing the update to the non-cooperating party could impose a risk for the
intermediary so it is discouraged.

### Opening

Matching of participants and intermediaries is part of State Channel network
resolution process and its corresponding protocol. It is not part of this
whitepaper. For the scope of it we consider that participants have agreed upon
an intermediary they both have opened State Channels with.

Opening of a Virtual State Channel consists of participants: both participants
authenticate an off-chain transaction that is similar to the `channel_create`
one. We should not reuse the `channel_create` one because a potential
malicious intermediary could post it on-chain.

Once both Virtual State Channel participants authenticate the initial
off-chain transaction, independently of each other they both provide it to the
intermediary in their corresponding parent State Channels with her. Based on
this off-chain transaction, the Virtual State Channel is created in both
parent State Channel's states. This is enough for everyone to consider the
Virtual State Channel to be opened.

It is worth mentioning that the intermediary can reject opening the Virtual
State Channel and participants can not dispute that on-chain. It is up to the
State Channel peer to decide if they want to lock some tokens or not. The
situation is a bit more complicated if the intermediary receives an off-chain
transaction for Virtual State Channel creation from one of the participants
but not from the other. In that case the intermediary treat it as a violation
of the off-chain protocol and reject the first participant's Virtual Channel
creation attempt. Not allowing disputing Virtual Channel creation on-chain
prevents from all types of replay attacks.

### Closing

Contrary to on-chain context where State Channels are long lived because of
fees and confirmation times needed for opening, Virtual State Channels do not
benefit from that and are expected to be short lived: participants connect,
interact with each other off-chain and then close the Virtual State Channel.
If they need it once again, they could reopen it using either the same
intermediary or a different one. If they have a state they want to resume,
they could do so. One strong argument for short lived Virtual State Channels
would be that the intermediary locks tokens in them. They could charge an
interest for the locked amounts.

We distinguish two different cases in which channel according to if the
Virtual State Channel participants had reached an agreement regarding channel
closure of not.

#### Closing with a mutual agreement

If both Virtual State Channel participants agree on a final distribution of
tokens, they produce and co-authenticate an off-chain transaction that is
similar to the `channel_close_mutual` one. They both provide it to the
intermediary and once accepted in the parent State Channels, the Virtual State
Channel is considered as closed. What is more, once the intermediary accepts
this in one of the parent State Channels, the corresponding participant does
not have to wait for a confirmation that this is done in the other parent
State Channel.

If anyone refuses accepting the transaction in their parent State Channel,
this can be disputed on-chain.

Once the channel had been mutually closed in the parent State Channel, either
with on-chain participant's agreement or a dispute, the effects are instant:
Virtual State Channel tokens are redistributed according to the transaction
and the Virtual State Channel object is being deleted from the parent State
Channel's state.

#### Closing without an agreement

In on-chain State Channels is expected that one of the participants could stop
being cooperative: one could be refusing valid updates, one could be
non-responding or being malicious. In such cases participants are expected to
protect themselves with bringing this on-chain. If the other party is not
cooperating anymore, the safest approach would be simply closing the on-chain
State Channel using [the solo closing
sequence](./ON-CHAIN.md#channel_close_solo).

The same assumptions for having non-cooperative participants can be applied in
the context of Virtual State Channels: any of the other parties might be
missing or being malicious. Then one must protect themselves using a similar
sequence - the virtual state channel solo closing one. In that chase a Virtual
State Channel participant is expected to close the Virtual State Channel. This
is done using a procedure similar to the solo closing one, differences lying
in the transaction being an off-chain one and that the arbiter being used is
the intermediary.

If a participant wants to enter into a virtual solo closing sequence, one
produces a corresponding off-chain message, similar to the on-chain
`channel_close_solo_tx`. This is being solo authenticated and provided to the
intermediary. The Virtual State Channel object in their parent State Channel
is updated accordingly: provided `round` and `state_hash` had been used and
the Virtual State Channel enters in a `closing` state. This gives a
`lock_period` of on-chain keyblocks for the other party to provide an
off-chain `channel_slash_tx` alternative or off-chain force progress
transaction.

If a participant provides any of those to the intermediary, the latter is
expected to publish it in the other parent State Channel with the other
Virtual State Channel participant. This modifies the Virtual State Channel
object.

Once the `lock_period` timer had expired, an off-chain transaction, similar to
the `channel_settle_tx` is being posted in the parent State Channels that
finalizes the channel closing and redistributes tokens.

If anyone refuses accepting a valid off-chain closing/slashing/settling
transaction, this could be disputed on-chain. This makes all parties safe from
malicious refuses. One odd scenario would be an intermediary accepting a valid
off-chain transaction from the virtual solo closing sequence in one of the
parent State Channels while not publishing it to the other. This would allow
one of the participants closing the Virtual State Channel in one of the parent
State Channels, while the other participant is not even aware of it.  Since
newer channel state has the potential to overwrite an older one, that puts the
intermediary in an unfavourable situation: if the channel had been closed with
not-the-latest-state or if participants keep making off-chain transactions,
the other participant could close the Virtual State Channel unilaterally with
a newer state. The distribution of tokens could be different but the Virtual
State Channel had been already closed in the other on-chain State Channel and
it couldn't be disputed anymore. In that case the risk lies in the
intermediary and this puts an incentive on her side to behave according to the
protocol.

#### Close without a state

An edge scenario is when the Virtual State Channel had been opened and the
intermediary wants to close it but participants refuse to do so. Since the
Virtual State Channel internal state is known only to Virtual State Channel
participants, the intermediary doesn't have enough information for closing the
Virtual State Channel on-chain. Other State Channel solutions had reported
this as an attack vector known as Griefing - when Virtual State Channel
participants do not close their Virtual State Channel for a long period of
time, thus forcing the intermediary to keep their their tokens locked. 

In such case the protocol allows the intermediary to initiate the close of the
Virtual State Channel as if the token distribution is that the intermediary
gets all the tokens locked in the Virtual State Channel. The closing state is
considered to be before the initial one, having a `round=0`. If either
participant disagrees with this, they could provide a co-authenticated Virtual
State Channel off-chain state in an off-chain slash transaction. Since the
initial Virtual State Channel state has a `round=1`, any co-authenticated
state would work. This will modify the Virtual State Channel token
distribution but also provide the intermediary with a state one could use in
the other parent State Channel with the other participant, if one is to
provide there an older Virtual State Channel state.

### Deposit, withdrawal and snapshot

It is expected that participants could desire depositing more tokens in a
Virtual State Channel or withdrawing some out of it. Providing a non-closing
temporary state is also useful. For all of those there would be unique
off-chain updates provided to the parent State Channels in order to update the
Virtual State Channel object accordingly. Those off-chain udpates mirror the
State Channel on-chain transactions `channel_deposit_tx`,
`channel_withdraw_tx` and `channel_snapshot_solo_tx` and they all share a
common flow but some might be disputed and others - not.

For the virtual deposit and withdrawal, both participants agree on a certain
action to be implied on the Virtual State Channel. Since the withdrawal is
simply unlocking tokens from the channel, there is no need of agreement from
the intermediary and this action can be progressed on-chain if one refuses to.
This is not the case with deposit: while one of the Virtual State Channel
participants locks some of their tokens in their parent State Channel context,
in the other parent State Channel the intermediary is expected to lock the
same amount of tokens from their behalf. Since we can not force participants
into locking tokens, there must be a general agreement with the intermediary
as one could refuse to accept the off-chain transaction. That's why deposits
can not be force-progressed.

The situation with the snapshot is easier: anyone can produce a snapshot
anytime, as long as it is based on a Virtual State Channel State that has a
higher `round` than the one the Virtual State Channel object has in the parent
State Channel with the intermediary. The intermediary could provide this
snapshot in the other parent State Channel and if the other party refuses to
cooperate, this can be force-progressed on-chain.

### Forcing progress

If at any point of time a Virtual State Channel participant stops cooperating,
the other one can protect themselves using the intermediary was an arbiter.
This modifies the Virtual State Channel object in their parent State Chennel.
Then the intermediary is to get this valid forced progressed transaction in
their other parent State Channel. If the participant still refuses to
cooperate, this could be brought to the on-chain and be resolved there.

It is worth mentioning that if the other participant refuses the forced
progress, the intermediary probably should bring this on-chain. Otherwise
there is a risk of branching the Virtual State Channel's state: the
non-cooperative participant could provide a different forced progress on-chain
to invalidate the virtual one.

### Disputes

A general assumption is that clean dispute procedures and properly designed
smart contracts will incentivise people to follow the protocol. Cheating would
meaningless as it would yield no benefit for the cheating party. That is a
strong argument in favour of aeternity's State Channels as disputes are on a
protocol level and they act in a predefined and predictable manner. The same
will stand true for aeternity's Virtual State Channels as the old behaviour is
kept but yet enriched with the ability to force progress Virtual State Channel
off-chain transactions as well.

In order to keep transactions and their functionality easy to reason about,
the `channel_force_progress_tx` will not be reused. A new transaction type
will be implemented - `channel_vsc_force_progress` that will have similar
mechanics. It consists of:
* `payload` that defines the `round` and the `state_hash` the progress is
  based on. This is the context in which the Virtual State Channel object
  lives and not the Virtual State Channel state itself. It could be:
    * the latest on-chain persisted one: in this case the on-chain stored
      `round` and `state_hash` are used. The `payload` is empty
    * off-chain transaction with a greater `round` to the one currently
      persisted on-chain for this parent State Channel. The `payload` is a
      serializated off-chain transaction that belongs to that parent State
      Channel and its `round` and `state_hash` are used for defining the
      parent State Channels' state that the forced progress is being based
      upon.
* `poi` is a Proof of Inclusion that provides enough information for the
  forced progress to be applied. This would include the Virtual State Channel
  object but possibly accounts to which tokens are withdrawn might be needed
  as well.
* `update` is a Virtual State Channel off-chain update. This could be:
  * a co-authenticated off-chain withdraw
  * an unilaterally authenticated off-chain snapshot
  * an unilaterally authenticated settle
  * a co-authenticated off-chain mutual close
  * an unilaterally authenticated dispute. Those also provide a context for
    the execution: a `payload` that is either empty or a co-authenticated
    Virtual State Channel state, corresponding poi or full set of trees, next
    pair of Virtual State Channel's `state_hash` and `round`. Update types for
    disputes supported are:
    * solo close
    * slash
    * force progress
    * virtual force progress
* `state_hash` - the root of the parent State Channel state tree after the
  `update` had been applied on top of the `poi`
* `round`: parent State Channel's next round

Note that this allows force-progressing of contracts in a Virtual State
Channel. It also allows forcing state in a nested Virtual State Channel,
essentially allowing Virtual State Channels inside Virtual State Channels.


## Expected improvements

Introduction of Virtual State Channels enriches the protocol further allowing
different enhancements to it. Some notable ones would be:

### Off-chain speed

This will allow near-instant Virtual State Channel opening and closing. This
is a great improvement over on-chain State Channels as it allows trustless
transffer of value from anyone to anyone to be performed completely off-chain
using existing State Channels.

### Prices

The intermediary plays a crucial role in this architecture and those are
expected to be reimbursed for their work. Dispite this, it is expected that
the cost of their service would be much less expensive than the fees and gas
costs required by miners.

### Multiple intermediaries

The defined model allows Virtual State Channels to be established using
multiple intermediaries. There are different approaches of implementing this:
* Virtual State Channels within Virtual State Channels
* a chain of Virtual State Channels inside of on-chain State Channels

Both approaches have radically different contexts. Those are outside of the
scope of this document.

### New business modelds

One obvious new actor on the blockchain stage would be the intermediary: they
act as off-chain miners in the proof-of-state context of the State Channels.
They validate new off-chain transactions regarding the Virtual State Channels
and, since this requires computations, is computational work. Another piece of
their serivce is locking tokens and taking risk from behalf of Virtual State
Channel participants. It is expected that intermediaries might require some
sort of interest depending on the amount of locked tokens over time. The act
of participants not closing their Virtual State Channel for a long period of
time is usually called Griefing and since being outside of the scope of the
protocol is outside of this document. It is worth mentioning that this is
preventable. Still - in order for intermediaries to provide this service, it
must be properly compensated. It is up to the market to define exact
mechanisms for that.

Another emerging service might be the Channel Network provider. Since multiple
intermediaries are possible, there will be issues with intermediary total
amount of tokens throughput and congestion. There will be the need for proper
pathfinding through the State Channel network.

### Multi-participants channels

Introduction of Virtual State Channels allows developing new protocols on top
of them, one of which is the Channel entity with many participants. This can
be achieved using different architectures, but what would be common is sharing
some common state.

