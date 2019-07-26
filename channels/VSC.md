# Virtual State Channels

## State Channels

### Rationale

There are different approaches of scaling a blockchain's throughput and State
Channels are one of most promising ones. Although State Channels are usually
considered Layer 2 architecture, æternity has them integrated on a protocol
level. They provide much faster and cheaper transactions while keeping the same
level of trustlessness the blockchain already provides. You can read a detailed
discussion about æternity state channels
[here](https://github.com/aeternity/protocol/tree/master/channels).

### How do SCs work

The main idea behind Virtual State Channels is to be built upon the existing
infrastructure and abstractions. This will make it transparent for users whether
the environment they are using is actually an on-chain State Channel or a
Virtual one. This will ease adoption of Virtual State Channels as the very same
software will run in different contexts.

With this in mind, in order for us to explain in detail the nuts and bolts of
Virtual State Channels we must first dive deep into on-chain State Channels. I
will focus on the tricky parts regarding Virtual State Channels.

#### Alice and Bob

Let's have an Alice and a Bob. They open a State Channel on-chain using a
`channel_create` transaction. Then they wait a certain amount of confirmations
to be sure the opening transaction is safely burried deep enough in the chain
and only then do they proceed with using the channel.

```
  +-------------+      off-chain      +-------------+
  |   Alice     |+-------------------+|     Bob     |
  |-------------|       prtocol       |-------------|
  |             |                     |             |
  |  off-chain  |                     |  off-chain  |
  |    state    |                     |    state    |
  |    trees    |                     |    trees    |
  |             |                     |             |
  +-------------+                     +-------------+
```

Each channel has an ever changing state. It is represented by a set of MPTrees
that hold accounts, contracts and contract calls. This set of MPtrees can be
treated as one big MPTree that has a root hash. This is what we call a
`state_hash` of a channel and it identifies the channel's state at a certain
point of time. Since in essence the off-chain world is detached from the
on-chain world - we don't measure points of time with blocks but rather with
rounds: one round consists of a set of changes that are applied to the current
channel state and the newly produced `state_hash` is co-authenticated by both
participants. We must be able to make a reasoned decision comparing two states
as to _when_ they were produced: we must be able to order state changes. Thus we
also have an increment-only value we call `round`: it is the index of the round
of updates, starting with [1 at channel creation
time](https://github.com/aeternity/aeternity/blob/16ecd302e60f599bfe3cc5f5cf0f7ea5ea336874/apps/aechannel/src/aesc_create_tx.erl#L304-L306).
Then it is bumped at every successful round of updates. There is a neat parallel
with another State Channel's project: `round` in æternity corresponds to
`version` in [Perun](https://www.perun.network/).

Participants can produce rounds of channel updates that modify the state
sequentially: once one round is co-authenticated by both participants - or
alternatively, rejected by anyone of them - a new set of updates can be
initiated.

#### On-chain representation

In the on-chain trees we have an object that represents the channel. It has the
latest posted on-chain `state_hash` and `round`. In order for a newly posted
on-chain transaction for this channel to be valid - it must have a greater
`round` than the last one on-chain.

Although the main goal is to keep as much of the transactions as possible
off-chain, there are a few _bridges_ to the on-chain world: for example
participants can put more coins into the channel or they can withdraw some out
of it. Each on-chain transaction comes with a fee to be paid to the miners for
including it.

The on-chain representation will be important for later on, so we will dig a bit
deeper into it. So a channel object produced from a `channel_create` transaction
where the `initiator` dedicates 60 coins and the `responder` dedicates 40 coins
would look similar like this:

```javascript=
{  
   "id": "ch_abc...", // the channel ID
   "initiator_id": "ak_bca...", // the address of the initiator
   "responder_id": "ak_123...", // the address of the responder
   "initiator_amount": 60, // the amount the initiator initally had locked in the channel
   "responder_amount": 40, // the amount the responder initally had locked in the channel
   "channel_amount": 100, // the sum of the two amounts
   "channel_reserve": 1, // a value provided by participants in channel_create transaction
   "delegate_ids": [], // for this example we don't need delegates
   "state_hash": "st_456...", // the state_hash from channel_create transaction
   "round": 1, // this is the initial value
   "solo_round": 0, // this is the initial value
   "lock_period": 0, // this is the initial value
   "locked_until": 0 // this is the initial value
}
```

Note the amounts as we will revisit those with regard of Virtual State Channels

#### Disputes

The general assumption is if the protocol is clean and easy to use, this would
provide incentive for participants to follow it. Cheating would be meaningless
as it would yeld no benefit for the cheating party. That is a strong argument in
favour of aeternity's State Channels as disputes are on a protocol level and
they act in a predefined and predictable manner. You can read more about them
[here](https://github.com/aeternity/protocol/blob/master/channels/ON-CHAIN.md#disputing-updates).

A short version would be that a co-signed off-chain transaction with a greater
`round` overwrites one with a lower `round` and also states produced by a
`channel_force_progress` transactions can be discarded if they are not based on
the latest co-signed state. This uses the on-chain world as an arbiter and keeps
the State Channels trustless.

### Perks

This architecture is a great improvement to the on-chain transactions.

#### Soft-real time

In order for an off-chain transaction to be accepted, it is enough to be
co-authenticated by both parties. This allows making soft-real time applications
on the blockchain - one does not have to wait for the miner to include a block.
This means if Alice has a channel with Bob, she can pay for her coffee instantly
and Bob is as safe as it gets.

#### Off-chain transactions costs

Since both participants execute the off-chain transactions on their side - they
both consume equal amount of electricity. No fees are being paid for off-chain
transactions, no gas is being consumed for off-chain contract creation and
execution.

#### Improved privacy

If all parties follow the happy path, none of the channel's state will make it
on-chain. In this sense all contracts and transactions are private. Only the
final redistribution of tokens is made public.

It is worth noting that if someone misbehaves, the off-chain state may go to the
chain, making the latest state public. State Channels are not guaranteed to be
private in the unhappy path.

### Limitations

#### On-chain speed

Although off-chain transactions reach blazing speeds, every now and then the
participants may want to touch the chain. That would be when creating a channel
for example. In order for them to be be confident that the on-chain transaction
does not end up in a fork, they must wait for a certain amount of confirmations
to build up. In this regard the channel opening is not much different from a
regular on-chain transaction and participants are expected to wait for a few
generations.

#### Dispute costs

Since there are no costs for making off-chain transaction, this could provide an
incentive to use bigger and more computational heavy contracts off-chain. In
case of a dispute this could lead to force-progress transactions that require a
lot of gas to be paid to miners.

#### Privacy

In case of a dispute, a force-progress would put the latest off-chain state
on-chain, making any private information in the state trees public.

Furthermore, opening and closing a channel, even following the happy path, are
on-chain transactions that leave a trace on-chain of the interaction between the
two parties.

#### Multi-party channels

The current approach could be modified in order to allow multiple participants
in a state channel. Our concern is that this would either end up in a sequential
or centralized architecture, thus it is not part of the protocol. We will
revisit this in the Virtual State Channels section below.


## Enter Virtual State Channels

### Description

Let's have Alice, Bob and Ingrid. Alice and Bob want to open a channel between
themselves but for some reason they don't want to do it on-chain. Meanwhile,
they both have their own connection with Ingrid. Then they can use their
connections with her in order to establish a Virtual State Channel between
themselves:

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
 
That would mean that no transaction is posted on-chain when opening the Virtual
State Channel, and it is active and safe to use as soon as all three parties
have agreed upon it. The proposed solution results in using Ingrid as on-chain
State Channels use the on-chain. That means Alice and Bob would provide Ingrid
with all channel transactions they would usually post on-chain, using her as an
arbiter in potential disputes.

Some important notes:
* if Ingrid is malicious, at any time Alice or Bob can bring the off-chain
  channel on-chain. This is still trustless from their point of view
* if any of Alice and Bob or both of them are malicious, Ingrid has enough
  information to bring on-chain so she is safe and trustless
* the connection between Alice and Bob is direct: messages sent from one to the
  other do not go through Ingrid. Ingrid receives only what would in on-chain SC
  be on-chain transaction, all off-chain transactions are kept private between
  Alice and Bob
 
### How do VSC work

#### Network resolution

The network resolution (how does Alice decide to use Ingrid to connect to Bob)
is a big issue by its own. It must solve problems like registering of
intermediaries on a distributed service, using the smallest fees, chain
congestion and channel maximum amount and etc. This document focuses on the
on-chain protocol so it can be implemented in a safe mannner.

The network resolution is not in the scope of this document but one may note
that the Intermediary Service could also provide some version of routing, social
networking, vendor marketplace, etc.

#### Opening of a Virtual State Channel

The proposition to implement this is quite simple to explain but it has a few
twists: we just allow having SC inside SC. This is currently not allowed on an
off-chain protocol level and is not subject to on-chain disputes. The idea is to
change both protocols so channels within channels are part of on-chain disputes
with a safeguard mechanism for the intermediary.

The main twist is hidden in the channel objects that are kept in the on-chain
channels - both Alice and Ingrid dedicate amount of tokens according to the
channel opening parameters. Alice dedicates for herself while Ingrid dedicates
for Bob. The channel object created is the Alice-Bob one.

Since intermediaries are not part of the channel object but in the context of
their State Channel they must be part of a dispute mechanism, we wrap the
channel object in a respective data structure that defines who acts in behalf of
whom. This is used later on in closing to know who is awared what.

##### Example

We have the Alice-Ingrid-Bob scenario where Alice and Bob both have on-chain
channels with Ingrid and Alice and Bob want to open a Virtual State Channel. By
some mechanism (e.g. via Ingrid), Alice has found Bob, they've reached an
agreement that they want to open a Virtual State Channel, negotiated its
parameters and decided to use Ingrid as an intermediary. For the example, let's
have Alice dedicating 10 AE to the Virtual State Channel and Bob, 12 AE. The
total amount of tokens in the Alice-Bob VSC is 22 AE.

Alice and Bob produce an off-chain update similar to `channel_create`
transaction. They co-sign it with their authentication method used in their SC
with Ingrid. Signing off-chain updates themselves is a new mechanism in SC, as
we used to sign only off-chain transactions.

Then Alice provides this off-chain update to her SC with Ingrid. This update
creates the Alice-Bob Virtual Channel object in their state trees. Alice
dedicates to it from her off-chain balance the 10 AE she had already agreed to
open a VSC with Bob. Ingrid on the other hand dedicates the 12 AE that Bob had
promised. Since we want the channel object to look as expected, the wrapper
object reflects the balance contributed by 'requester' and 'intermediary'
respectively. The channel object looks like this:

```javascript=
{
   "intermediary_id": "ak_...", // which one is Ingrid
   "intermediary_amount": 12, // part of the total contributed by Ingrid
   "requester_amount": 10, // part of the total contributed by Alice
   "channel" :
      {  
         "id": "ch_...", // the Alice-Bob channel ID
         "initiator_id": "ak_...", // the address of Alice
         "responder_id": "ak_...", // the address of Bob
         "initiator_amount": 10, // Alice balance
         "responder_amount": 12, // Bob balance
         "channel_amount": 22 // the sum of the two amounts
      } ...
}
```

We could have an implicit logic that in the context of this particulat State
Channel, the `initiator` role is being played by the `requester` and the
`responder` role is being played by `intermediary`. That would mean that any
tokens dedicated for the VSC channel by the `initiator`, in the SC are dedicated
by the `requester` instead. Same goes with withdrawing tokens.

#### Making an off-chain update in a Virtual State Channel

Once the channel has been opened, participants have a direct connection between
each other and can produce off-chain updates and off-chain states as they would
in an on-chain State Channel. The only difference is their authentication method
is according to their on-chain channel with Ingrid.

##### Example

Alice has an open VSC with Bob. Alice wants to execute a smart contract in their
VSC, Alice produces the updates she desires and prepares a corresponding
off-chain transaction. It has the AB Virtual State Channel ID, the next `round`
and the newly calculated `state_hash`. Alice authenticates this transaction
according to her authentication method used in her on-chain State Channel with
Ingrid. She then gives it to Bob to co-authenticate. Bob does so according to
his authentication method in his on-chain State Channel with Ingrid. He then
returns the co-authenticated transaction to Alice and the update is finished.

It is worth noting that this closly resembles the on-chain State Channel
protocol. Also it is important to stress that none of the off-chain updates
reach Ingrid.

#### Depositing more tokens to a Virtual State Channel/withdrawing from a
Virtual State Channel

Alice and Bob produce an off-chain update similar to `channel_deposit` or
`channel_withdrawal` transactions. They co-sign it with their authentication
method used in their SC with the intermediary. 

Then they can provide this co-signed update to Ingrid and thus one of them can
(deposit more/withdraw some) tokens from their off-chain balances. This updates
the VSC object in both on-chain State Channels.

##### Example

Alice wants to put some more tokens to her off-chain balance in her Virtual
State Channel with Bob. She prepares an update that state she is to deposit 3AE
and it is co-authenticated by her and Bob. The update is given to Ingrid. She is
to agree to it in both on-chain State Channels she has but it yelds different
results:
* in Alice-Ingrid on-chain State Channel 3AE are moved from Alice's off-chain
  balance to the Alice-Bob channel
* in Bob-Ingrid on-chain State Channel 3AE are moved from Ingrid's off-chain
  balance to the Alice-Bob channel

In both channels the virtual channel object is modified to reflect the new
balances, for example in Alice-Ingrid channnel the AB channel object looks like
this:

```javascript=
{
   "intermediary_id": "ak_...",
   "intermediary_amount": 12,
   "requester_amount": 13,
   "channel":
      {  
         "id": "ch_...", // the Alice-Bob channel ID
         "initiator_id": "ak_...", // the address of Alice
         "responder_id": "ak_...", // the address of Bob
         "initiator_amount": 13, // Alice balance
         "responder_amount": 12, // Ingrid balance
         "channel_amount": 25, // the sum of the two amounts
         "responder_withdraw_id": "ak_..." // the address of Ingrid
         ...
      }
}
```

#### Closing a Virtual State Channel (happy path)

Whenever both parties have agreed upon a closing state, they produce a
co-authenticated update that acts similarly to `channel_mutual_close`
transaction but in the context of a State Channel. Provided in an on-chain State
Channel that has a channel with that ID in its state, it redistributes the
tokens from the channel and closes it.

##### Example

Alice and Bob decide on a closing state of their Virtual State Chanel. They
co-authenticate it and provide it to Ingrid. This redistributes the tokens
locked in the channel object to the different parties:
* in Alice-Ingrid State Channel Alice gets her tokens and Ingrid gets Bob's
* in Bob-Ingrid State Channel Bob gets his tokens and Ingrid gets Alice's

After that the channel object is being removed and the Virtual State Channel
between Alice and Bob is considered to be closed.

#### Closing a Virtual State Channel (unhappy path)

If one party wants to close a Virtual State Channel while the other refuses to
or is missing, we have a similar situation as the on-chain State Channel solo
closing sequence. We propose a similar solution: the closing party initiates a
closing sequence in their on-chain channel with the intermediary. It results in
modifying the channel object there with an appropriate on-chain height to be
reached in order for the channel to be solo-closed. Meanwhile the intermediary
does a corresponding operation with the other party, giving it time to provide a
newer off-chain state, using a on-chain forced progress if necessary.

It is not possible to reduce the amount of the other party in the VSC object
during a unilateral update, i.e. the 'requester' cannot reduce the
`intermediary_amount` and the 'intermediary' cannot reduce the
`requester_amount`. This is ultimately checked on-chain, if needed.

##### Example

Alice wants to close her Virtual State Channel with Bob, but Bob refuses. Alice
produces a solo update in her on-chain State Channel with Ingrid initiating a
solo-closing sequence of the Virtual State Channel. If Ingrid refuses this,
Alice can force it on-chain.

Ingrid takes this update provided by Alice and applies it to her on-chain State
Channel with Bob. If Bob refuses, this can be force-progressed as well.

This results in modifying the channel object in both state channels, initiating
a block height timer in which both Virtual State Channel participants can
provide Ingrid with yet newer off-chain states or forced progresses. As it
happens on-chain, a newer state overwrites any forced progress state produced on
top of an older state.

### Disputes

The main point is at any point of time, any participant can eject in a safe
manner.

#### Bob is not responding or missing

If there is a dispute between Alice and Bob or for the sake of the example Bob
refuses to co-authenticate the next state, Alice can produce an off-chain update
similar to force progress and bring it to Ingrid. This will produce the next
Alice-Bob VSC off-chain state in the Alice-Ingrid channel. This instantly makes
Alice safe. In order for Ingrid to be safe, she can propose to Bob to execute
the same update Alice had already provided her, this time in Ingrid-Bob's State
Channel. If Bob still refuses, Ingrid can produce an actual
`channel_force_progress` transaction that she posts on-chain in order for her to
enforce the contract execution in the Virtual State Channel, thus producing the
new Alice-Bob Virtual State Channel on-chain and at the same time producing the
next Ingrid-Bob off-chain state. The newly produced Ingrid-Bob state has in its
state the VSC's.

#### Ingrid is not responding or missing

If there is a new valid off-chain update that Ingrid refuses to accept, both
Alice and Bob can bring this on-chain via a `channel_force_progress` in a
similar mannner as [above](#Bob-is-not-responding-or-missing).

#### Actions that can be forced progressed

Not all actions can be forced progressed on-chain. The ones that are allowed:
* withdrawing tokens from a VCS - if the balance is co-authenticated by the two
  VSC parties. This limits the intermediary's exposure of locked tokens.
* execution of a contract in the VSC in a forced progress
* posting a co-signed off-chain state of the VCS in the on-chain SC (similar to
  `channel_snapshot` on-chain)
* mutual closing
* solo closing
* slash
* setttle

#### Actions that can not be forced progressed

Not all actions can be forced progressed on-chain. The ones that are not
allowed:
* channel creation
* depositing tokens in a VCS - even if it is co-authenticated by the two VSC
  parties. This increases the intermediary's exposure of locked tokens so we can
  not enforce it
* creation of a contract in the VSC in a forced progress

### Compensation

The work Ingrid does is:
* lock an equal amount of tokens as the VSC
* updating the off-chain state
* forcing progress

Note that the second task, updating the off-chain state, involves taking the
update from one channel and forwarding to the other. There is currently no
formalism for how this is to be done, or indeed checking whether it's done at
all. In order for Ingrid to have a incentive to perform this work, most probably
Ingrid might expect fees to be paid. This is outside of the scope of this
document.

### Multi-intermediary VSC

Let's have the following topology:
```
                              +----------+
                  +----------+| Ingrid 2 |+-------------+
                  |           +----------+              |
                  |                                     |
                  |I1I2 SC                              |I2I3 SC
                  |                                     |
                  |                                     |
                  +                                     +
             +----------+                          +----------+
       +----+| Ingrid 1 |                          | Ingrid 3 |+-+
       |     +----------+                          +----------+  |
       |                                                         |
       |AI1 SC                                                   |I3B SC
       |                                                         |
       +                                                         +
   +-------+                   AB VSC                         +-----+
   | Alice |+------------------------------------------------+| Bob |
   +-------+                                                  +-----+
   ```
Where:
* Alice has an open on-chain State Channel with Ingrid1, we will call it `AI1
  SC`
* Ingrid1 has an open on-chain State Channel with Ingrid2, we will call it `I1I2
  SC`
* Ingrid2 has an open on-chain State Channel with Ingrid3, we will call it `I2I3
  SC`
* Bob has an open on-chain State Channel with Ingrid3, we will call it `I3B SC`

Based on the desctiption of Virtual State Channel, Alice is able to open a
Virtual State Channel with Bob. We will call it `AB VSC`.

For this to happen Alice and Bob produce the VSC opening update that they would
if they were sharing only one intermediary. The catch here is the
authentications methods being used:
* Alice authenticates all `AB VSC` transactions and updates using her `AI1 SC`
  authentication method
* Bob authenticates all `AB VSC` transactions and updates using his `I3B SC`
  authentication method

Then they provide their intermediaries with this, as they would in a single
intermediary environment:
* Alice provies Ingrid1 with it
* Bob provies Ingrid3 with it

Then the Ingrids provide the next chain of the network with the update and etc.

At the end all network participants have inserted in their State Channel's
states the channel object that represents `AB VSC` and have all the means needed
to check incoming updates.

In this scenario, Ingrid1 will forward the updates to Ingrid3 via Ingrid2.
Ingrid2's role is strictly to forward all updates in each direction, most likely
retaining a fee for each operation. This fee can be covered by the fees required
by Ingrid1 and Ingrid2 respectively, but it's up to them to decide how this is
handled in practice.

### Alternative Multi-intermediary scenario (VSC-in-VSC)

An alternative way to route and set up Virtual State Channels through multiple
intermediaries would be the "VSC-in-VSC" model.

```
                              +----------+
                  +----------+| Ingrid 2 |+-------------+
                  |           +----------+              |
                  |                                     |
                  |I1I2 SC                              |I2I3 SC
                  |                                     |
                  |                                     |
                  +                                     +
             +----------+       I1-I3 VSC          +----------+
       +----+| Ingrid 1 |--------------------------| Ingrid 3 |+-+
       |     +----------+                          +----------+  |
       |                                                         |
       |AI1 SC                                                   |I3B SC
       |                                                         |
       +                                                         +
   +-------+                   AB VSC                         +-----+
   | Alice |+------------------------------------------------+| Bob |
   +-------+                                                  +-----+
```

In this case, `Ingrid 1` talks directly to `Ingrid 3` using a VSC, in a sense
more similarly to the initial scenario with just one `Ingrid`, in which case,
`Ingrid` maintains two VC endpoints and relays information informally, out of
scope for SC semantics. In this scenario, `Ingrid1` does the same thing, as does
`Ingrid3`.

A VSC object for the `I1-I3 VSC` in the `I1I2 CS` would look like:

```javascript=
{
    "intermediary_id": "ak_...", // Ingrid 2 pubkey
    "requester_id": "ak_..." // Ingrid 1 pubkey
    "intermediary_amount": 100, // I3B intermediary_amount + margin
    "requester_amount": 100, // AI1 intermediary_amount + margin
    "fee": ...,
    "channel":
        {
            "initiator": "ak_...", // Ingrid 1 pubkey
            "responder": "ak_...", // Ingrid 3 pubkey
            ...
        }
}
```

Interaction between `Ingrid1` and `Ingrid3` regarding the VSCs they service (not
necessarily just the `AB VSC`) could be represented by duplicating the VSC
objects in the respective channels with their clients (here e.g.: `AI1 SC` and
`I3B SC`), force-progressing updates if need be. `Ingrid2` will only get
involved whenever `Ingrid1` and/or `Ingrid3` want to close, deposit or withdraw
from `I1-I3 VSC`.

In this scenario, Ingrid1 can request forwarding by Ingrid3, and the other way
around, much in the same way that she would with Ingrid2 above. It's up to
Ingrid1 and Ingrid3 to agree on how any fees are split, and how much is
recovered from Alice and Bob via the fees explicit in the VSC object.

### Notion of time

Since the VSC object is split into two halves, which must be kept synchronized,
race conditions may arise. An example of such a race might be:
* Alice posts a `solo-close`, Ingrid accepts and starts a 'timer'
* The lock period expires
* Alice posts a `settle` to close the channel
* Before `Ingrid` gets to update the `IB SC`, `Bob` posts a `slash`, either not
  knowing, nor not caring, that the VSC is being closed.

The challenges here are (a) choosing a time reference, and (b) determining the
order of events. We can address both, but only partly, by viewing the blockchain
as a form of monotonously increasing referenced counter (the height), where each
block hash is strictly ordered.

When addressing the example scenario above, `Alice` would, when proposing the
`solo_close`; also note in the channel object the height until which it will be
locked. This is (hopefully) co-signed by `Ingrid` and forwarded to `Bob`, who
hopefully also signs it (i.e. co-signs the update from `Ingrid` on the `IB SC`.)

If `Bob` tries to sneak in a `slash` after the lock_period expires, it should be
rejected by `Ingrid` if the observed chain height has already reached the
`locked_until` height. Unfortunately for `Bob`, this will need to be judged at
the time of dispute, since there is no reliable way to prove that `Bob` issued
the update before the height was reached. `Bob` did agree to the lock_period,
and was given time to dispute the solo close. There will be an uncertainty
margin when close to the `locked_until` height that cannot be completely
eliminated.

### Example scenarios

In order to provide better understanding of the proposition above, we will go
through a few hypotetical scenarios when something goes bad. We will answer
_What shall X do in order to be safe?_ for each one of them

#### Alice is malicious

##### Alice provides Ingrid with an old state

At any point of time Alice can provide Ingrid with some Virtual State Channel
State that might not be the latest. Ingrid then uses it to update her State
Channel with Bob. In this case Bob can simply provide a newer state and they all
are safe. This is important esp. while resolving a solo closing using Ingrid as
an arbiter.

##### Alice refuses to cooperate with Ingrid

If Ingrid has a newer state than the one Alice had provided, or Ingrid has a
state produced by a valid force progress by Bob, Alice might decide not to
cooperate. In this case Ingrid simply brings the issue on-chain using a forced
progress.

##### Alice produces a force progress based on an old state

Ingrid receives a forced progress that seemsreasonable because the state it is
based on a is the latest she had seen so far. Ingrid accepts it as valid and
updates her Virtual State Channnel object in her channel with Alice. She then
proposes this in her channel with Bob. This puts Bob at risk so Bob must defend
himself by providing Ingrid with a newer co-authenticate Virtual State Channel
state. Ingrid can use this to overwrite the Virtual State Channel's object in
her on-chain State Channel with Alice now, either off-chain if Alice agrees, or
on-chain using a force progress.

##### Alice goes missing

If Alice goes missing, either Bob or Ingrid can initiate a solo-closing sequence
using forced progress. As with the on-chain protocol regarding State Channels,
this puts Alice at risk and it is up to her to defend herself.


#### Both Alice and Bob are malicious

There are a few interesting scenarios where Alice and Bob try outsmarting
Ingrid.

##### Both Alice and Bob refuse providing state for closing

In this case Ingrid has no state to use for a solo closing. She simply closes
the Virtual State Channel using the solo closing sequence either by Alice and
Bob agreement or forcing progress. The thing is that if neither Alice, nor Bob
provide state, Ingrid closes the Virtual State Channel using the opening state
which states that she claims all the tokens dedicated to it. If Alice does not
provide a state - she loses her stake. If Bob does not provide a state - he
loses his stake.

A corner case would be a race condition where Ingrid finalizes a channel with
Alice and only then Bob provides an off-chain state. The very worst case
possible for Ingrid would be Bob providing an off-chain state where Bob receives
all tokens, so let's dive deeper with a proper example:

In a Virtual State Channel opening time Alice dedicates 4 tokens to the Virtual
State Channel with Bob, Bob dedicates 6 so the total amount is 10.

In Alice-Ingrid on-chain State Channel Alice balance is reduced with 4 tokens
and Ingrid's one - with 6.  In Bob-Ingrid on-chain State Channel Bob's balance
is reduced with 6 tokens and Ingrid's one - with 4.

In both State Channels the Virtual Channel's initial object has 10 tokens that
are to be received by Ingrid if no state is provided.

Fast forward: Ingrid closes the Virtual State Channel with State Channel with
Alice and receives all 10 tokens, 6 of which were hers in the first place.
Ingrid now had taken 4 tokens from Alice. Then Bob shows a state which proves
that he is to get all 10 tokens in his State Channel with Ingrid and, since
Ingrid has no other state to provide, she agrees. Then Bob gets all 10 tokens in
his State Channel, getting 4 tokens more than he had put in the begging. For
Alice this is a zero sum.

#### Ingrid is malicious

If at any moment Alice suspects that Ingrid might be malicious, she must go
on-chain forcing progress, no matter if Bob is honest or not. Malicious
behaviour of Ingrid might look like:

* Ingrid is not responding
* Ingrid is not accepting incoming valid Virtual State Channel updates

